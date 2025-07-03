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

# Check if the directory exists before searching
if [ ! -d "gen/typescript/qdrant/cloud" ]; then
    echo "Directory gen/typescript/qdrant/cloud does not exist"
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
    local js_path ts_path
    
    ts_path=$(echo "$dts_file" | sed 's|^gen/typescript/|./|')
    js_path=$(echo "$ts_path" | sed 's/\.d\.ts$/.js/')
    
    echo "$js_path|$ts_path"
}

# Create temporary file for processing results
temp_file=$(mktemp)
trap 'rm -f "$temp_file"' EXIT

# Find all .d.ts files and process them
find gen/typescript/qdrant/cloud -name "*.d.ts" -type f | \
while read -r dts_file; do
    # Skip if corresponding .js file doesn't exist
    js_file=$(echo "$dts_file" | sed 's/\.d\.ts$/.js/')
    [ ! -f "$js_file" ] && continue
    
    # Get paths
    paths=$(get_package_paths "$dts_file")
    js_path=$(echo "$paths" | cut -d'|' -f1)
    ts_path=$(echo "$paths" | cut -d'|' -f2)
    
    # Extract service and potential submodule from path
    rel_path=$(echo "$dts_file" | sed 's|gen/typescript/qdrant/cloud/||')
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
    
    # Generate export key and sort prefix
    if [ -z "$submodules" ]; then
        # Direct service: service/version/file (e.g., auth/v1/auth_pb.d.ts)
        if echo "$filename" | grep -q "_connectquery$"; then
            export_key="$version/$service/connect-query"
            sort_prefix="$service-$version-1"
        else
            export_key="$version/$service"
            sort_prefix="$service-$version-0"
        fi
    else
        # Has submodules: service/submodule(s)/version/file (e.g., cluster/auth/v1/file.d.ts, serverless/collection/auth/v1/file.d.ts)
        submodules_normalized=$(echo "$submodules" | tr '/' '-')
        if echo "$filename" | grep -q "_connectquery$"; then
            export_key="$version/$service/$submodules/connect-query"
            sort_prefix="$service-$version-$submodules_normalized-1"
        else
            export_key="$version/$service/$submodules"
            sort_prefix="$service-$version-$submodules_normalized-0"
        fi
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
