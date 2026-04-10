import os
import re

def natural_key(string_):
    """Helper to sort strings with numbers naturally (v1, v2, v10)."""
    return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', string_)]

def extract_services():
    service_list = []
    # Matches 'service ServiceName {' and captures preceding comments
    pattern = re.compile(r"((?://.*\n)+)?\s*service\s+(\w+)\s*\{", re.MULTILINE)
    
    # Strictly filtering for serverless only
    SKIPLIST = ["serverless"]

    for root, _, files in os.walk("."):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), ".")
            
            # Skip only if "serverless" is in the path or filename
            if any(term in relative_path.lower() for term in SKIPLIST):
                continue
                
            if file.endswith(".proto"):
                # Extract version from directory (e.g., proto/v1/auth.proto -> v1)
                parent_dir = os.path.basename(root)
                version = parent_dir if re.match(r'v\d+', parent_dir) else "v0"

                with open(relative_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    for match in pattern.finditer(content):
                        comment, name = match.groups()
                        
                        # Skip only if "serverless" is in the service name
                        if any(term in name.lower() for term in SKIPLIST):
                            continue

                        description = "No description provided."
                        if comment:
                            description = " ".join([l.strip("// ").strip() for l in comment.strip().split("\n")])
                        
                        service_list.append({
                            "name": name,
                            "path": relative_path,
                            "version": version,
                            "description": description
                        })

    # Sort: Primary = Name (alphabetical), Secondary = Version (v1, v2...)
    # This keeps v1 and v2 of the same service together in the table.
    return sorted(service_list, key=lambda x: (x["name"], natural_key(x["version"])))

def generate_markdown_table(services):
    lines = [
        "| Service Name | Version | Description |",
        "| --- | --- | --- |"
    ]
    for s in services:
        version_display = "N/A" if s["version"] == "v0" else s["version"]
        lines.append(f"| [{s['name']}]({s['path']}) | **{version_display}** | {s['description']} |")
    return "\n".join(lines)

def update_readme(new_table):
    file_path = "README.md"
    anchor = "Below is a list of the primary services available:"
    
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if anchor not in content:
        return

    # Targets the anchor and the table block, ensuring content after is preserved
    table_pattern = re.escape(anchor) + r"(\s*\n\s*\| Service Name \|.*?\|(?=\n\n|\n[^\s|]|$))?"
    
    replacement = f"{anchor}\n\n{new_table}"
    updated_content = re.sub(table_pattern, replacement, content, count=1, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    services = extract_services()
    table = generate_markdown_table(services)
    update_readme(table)
    print(f"Successfully updated README with {len(services)} services (Filtered: 'serverless').")
