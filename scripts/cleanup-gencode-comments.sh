#!/usr/bin/env sh

set -eu

# Buf doesn't have any option to remove the `buf:lint:ignore ...` comments when
# generating the code. We use this script to manually remove those lines after
# the code is generated.

# Clean Go files: remove the * buf:lint:ignore RULE pattern
find gen/ -type f -name '*.go' | while read -r file; do
    grep -v "// buf:lint:ignore" "$file" >tmp_file && mv tmp_file "$file"
done

# Clean TS files: remove the * buf:lint:ignore RULE pattern
find gen/ -type f -name '*.ts' | while read -r file; do
    grep -v "\* buf:lint:ignore" "$file" >tmp_file && mv tmp_file "$file"
done

# Clean JSON files: remove the \nbuf:lint:ignore RULE pattern
find gen/ -type f -name '*.json' | while read -r file; do
    awk '{gsub(/buf:lint:ignore [A-Z_]+\\n/, ""); print}' "$file" >tmp_file && mv tmp_file "$file"
done
