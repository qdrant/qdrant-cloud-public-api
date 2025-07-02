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
    submodule=$(echo "$rel_path" | cut -d'/' -f2)
    version=$(echo "$rel_path" | cut -d'/' -f3)
    filename=$(basename "$dts_file" .d.ts)
    
    # Determine if this is a direct service or has submodules
    # Count how many levels deep we are (service/version/file vs service/submodule/version/file)
    num_levels=$(echo "$rel_path" | tr '/' '\n' | wc -l)
    
    if [ "$num_levels" -le 3 ]; then
        # Direct service: service/version/file (e.g., auth/v1/auth_pb.d.ts)
        if echo "$filename" | grep -q "_connectquery$"; then
            export_key="$service/connect-query"
            sort_prefix="$service-1"
        else
            export_key="$service"
            sort_prefix="$service-0"
        fi
    else
        # Has submodules: service/submodule/version/file (e.g., cluster/auth/v1/file.d.ts)
        if echo "$filename" | grep -q "_connectquery$"; then
            export_key="$service/$submodule/connect-query"
            sort_prefix="$service-$submodule-1"
        else
            export_key="$service/$submodule"
            sort_prefix="$service-$submodule-0"
        fi
    fi
    
    echo "$sort_prefix|$export_key|$js_path|$ts_path"
done | \
sort | \
while IFS='|' read -r sort_prefix export_key js_path ts_path; do
    add_export "$export_key" "$js_path" "$ts_path"
done

echo "Generated exports for package.json"