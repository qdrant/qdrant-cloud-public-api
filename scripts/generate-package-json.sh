#!/usr/bin/env sh

set -eu

# first argument is version and we want to check it is a valid semver
if [ -z "${1:-}" ]; then
    echo "Usage: $0 <semver-version>"
    exit 1
fi
VERSION="$1"

jq --arg version "$VERSION" '.version = $version' package.example.json > tmp.$$.json && mv tmp.$$.json package.json
echo "Updated version to $VERSION in package.json"

# Check if the directories exist before searching
if [ ! -d "gen/typescript/legacy/qdrant/cloud" ]; then
    echo "Directory gen/typescript/legacy/qdrant/cloud does not exist"
    exit 1
fi

if [ ! -d "gen/typescript/strict/qdrant/cloud" ]; then
    echo "Directory gen/typescript/strict/qdrant/cloud does not exist"
    exit 1
fi

# Function to add export entry to package.json
add_export() {
    local key="$1"
    local js_path="$2"
    local ts_path="$3"
    
    jq --arg key "$key" \
       --arg js_path "$js_path" \
       --arg ts_path "$ts_path" \
       '.exports[$key] = {
         "import": $js_path,
         "types": $ts_path
       }' package.json > tmp.$$.json && mv tmp.$$.json package.json
}

# Function to convert .d.ts path to relative package paths
get_package_paths() {
    local dts_file="$1"
    local variant="$2"
    local js_path ts_path
    
    if [ "$variant" = "legacy" ]; then
        ts_path=$(echo "$dts_file" | sed 's|^gen/typescript/legacy/|./legacy/|')
    else
        ts_path=$(echo "$dts_file" | sed 's|^gen/typescript/strict/|./strict/|')
    fi
    js_path=$(echo "$ts_path" | sed 's/\.d\.ts$/.js/')
    
    echo "$js_path|$ts_path"
}

# Create temporary file for processing results
temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT

# Find all .d.ts files and process them
(find gen/typescript/legacy/qdrant/cloud -name "*.d.ts" -type f | sed 's|$| legacy|';
 find gen/typescript/strict/qdrant/cloud -name "*.d.ts" -type f | sed 's|$| strict|') | \
while read -r dts_file variant; do
    # Skip if corresponding .js file doesn't exist
    js_file=$(echo "$dts_file" | sed 's/\.d\.ts$/.js/')
    [ ! -f "$js_file" ] && continue
    
    # Get paths
    paths=$(get_package_paths "$dts_file" "$variant")
    js_path=$(echo "$paths" | cut -d'|' -f1)
    ts_path=$(echo "$paths" | cut -d'|' -f2)
    
    # Extract service and potential submodule from path
    if echo "$dts_file" | grep -q "qdrant/cloud"; then
        # Handle qdrant/cloud files with complex versioning logic
        if [ "$variant" = "legacy" ]; then
            rel_path=$(echo "$dts_file" | sed 's|gen/typescript/legacy/qdrant/cloud/||')
        else
            rel_path=$(echo "$dts_file" | sed 's|gen/typescript/strict/qdrant/cloud/||')
        fi
        service=$(echo "$rel_path" | cut -d'/' -f1)
        filename=$(basename "$dts_file" .d.ts)
        
        # Extract path components dynamically
        # Structure: service/[submodule1/submodule2/...]/version/file
        # Find the version (v1, v2, etc.) to split the path correctly
        path_parts=$(echo "$rel_path" | tr '/' '\n')
        
        # Find which part is the version by looking for v[0-9]+
        version=""
        version_index=0
        i=1
        for part in $path_parts; do
            if echo "$part" | grep -q "^v[0-9]\+$"; then
                version="$part"
                version_index=$i
                break
            fi
            i=$((i + 1))
        done
        
        if [ -z "$version" ]; then
            echo "ERROR: No version found in path $rel_path" >&2
            echo "ERROR" > "$temp_file"
            exit 1
        fi
        
        # Build submodule path (everything between service and version)
        submodules=""
        if [ "$version_index" -gt 2 ]; then
            # Extract submodules: everything from position 2 to version_index-1
            j=2
            while [ $j -lt "$version_index" ]; do
                submodule_part=$(echo "$rel_path" | cut -d'/' -f$j)
                if [ -z "$submodules" ]; then
                    submodules="$submodule_part"
                else
                    submodules="$submodules/$submodule_part"
                fi
                j=$((j + 1))
            done
        fi
        
        # Count files in the same directory to determine if we need specific filenames
        dir_path=$(dirname "$dts_file")
        file_count=$(find "$dir_path" -name "*.d.ts" ! -name "*_connectquery.d.ts" | wc -l | tr -d ' ')

        # Extract base filename without _pb suffix for cleaner export names
        base_filename=$(echo "$filename" | sed 's/_pb$//')

        # Generate export key and sort prefix
        if [ -z "$submodules" ]; then
            # Direct service: service/version/file (e.g., auth/v1/auth_pb.d.ts)
            if echo "$filename" | grep -q "_connectquery$"; then
                if [ "$file_count" -gt 1 ]; then
                    # Multiple files: include service name in connect-query path
                    service_name=$(echo "$filename" | sed 's/-.*_connectquery$//')
                    if [ "$variant" = "strict" ]; then
                        export_key="$service/$version/$service_name/connect-query/strict"
                    else
                        export_key="$service/$version/$service_name/connect-query"
                    fi
                    sort_prefix="$service-$version-$service_name-$variant-1"
                else
                    # Single file: keep existing behavior
                    if [ "$variant" = "strict" ]; then
                        export_key="$service/$version/connect-query/strict"
                    else
                        export_key="$service/$version/connect-query"
                    fi
                    sort_prefix="$service-$version-$variant-1"
                fi
            else
                if [ "$file_count" -gt 1 ]; then
                    # Multiple proto files: include filename for disambiguation
                    if [ "$variant" = "strict" ]; then
                        export_key="$service/$version/$base_filename/strict"
                    else
                        export_key="$service/$version/$base_filename"
                    fi
                    sort_prefix="$service-$version-$base_filename-$variant-0"
                else
                    # Single file: keep existing behavior
                    if [ "$variant" = "strict" ]; then
                        export_key="$service/$version/strict"
                    else
                        export_key="$service/$version"
                    fi
                    sort_prefix="$service-$version-$variant-0"
                fi
            fi
        else
            # Has submodules: service/submodule(s)/version/file (e.g., cluster/auth/v1/file.d.ts, serverless/collection/auth/v1/file.d.ts)
            submodules_normalized=$(echo "$submodules" | tr '/' '-')
            if echo "$filename" | grep -q "_connectquery$"; then
                if [ "$file_count" -gt 1 ]; then
                    # Multiple files: include service name in connect-query path
                    service_name=$(echo "$filename" | sed 's/-.*_connectquery$//')
                    if [ "$variant" = "strict" ]; then
                        export_key="$service/$submodules/$version/$service_name/connect-query/strict"
                    else
                        export_key="$service/$submodules/$version/$service_name/connect-query"
                    fi
                    sort_prefix="$service-$version-$submodules_normalized-$service_name-$variant-1"
                else
                    # Single file: keep existing behavior
                    if [ "$variant" = "strict" ]; then
                        export_key="$service/$submodules/$version/connect-query/strict"
                    else
                        export_key="$service/$submodules/$version/connect-query"
                    fi
                    sort_prefix="$service-$version-$submodules_normalized-$variant-1"
                fi
            else
                if [ "$file_count" -gt 1 ]; then
                    # Multiple proto files: include filename for disambiguation
                    if [ "$variant" = "strict" ]; then
                        export_key="$service/$submodules/$version/$base_filename/strict"
                    else
                        export_key="$service/$submodules/$version/$base_filename"
                    fi
                    sort_prefix="$service-$version-$submodules_normalized-$base_filename-$variant-0"
                else
                    # Single file: keep existing behavior
                    if [ "$variant" = "strict" ]; then
                        export_key="$service/$submodules/$version/strict"
                    else
                        export_key="$service/$submodules/$version"
                    fi
                    sort_prefix="$service-$version-$submodules_normalized-$variant-0"
                fi
            fi
        fi
    else
        # Handle non-qdrant files (google, buf, k8s.io) with simple path mapping
        if [ "$variant" = "legacy" ]; then
            rel_path=$(echo "$dts_file" | sed 's|gen/typescript/legacy/||')
        else
            rel_path=$(echo "$dts_file" | sed 's|gen/typescript/strict/||')
        fi
        
        # Remove .d.ts extension and _pb suffix for export key
        export_key=$(echo "$rel_path" | sed 's/\.d\.ts$//' | sed 's/_pb$//')
        
        # For strict variants, add /strict suffix
        if [ "$variant" = "strict" ]; then
            export_key="$export_key/strict"
        fi
        
        # Create sort prefix for consistent ordering
        sort_prefix="external-$(echo "$rel_path" | tr '/' '-' | sed 's/\.d\.ts$//')-$variant"
    fi
    
    echo "$sort_prefix|$export_key|$js_path|$ts_path"
done | \
sort | \
while IFS='|' read -r sort_prefix export_key js_path ts_path; do
    add_export "./$export_key" "$js_path" "$ts_path"
done

# Check if there was an error
if [ -f "$temp_file" ] && [ "$(cat "$temp_file")" = "ERROR" ]; then
    echo "Script terminated due to error in processing files"
    exit 1
fi

echo "Generated exports for package.json"
