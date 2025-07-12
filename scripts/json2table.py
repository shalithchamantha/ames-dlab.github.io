import json
import frontmatter
import sys

def load_json(path):
    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)


def generate_md_table(json_data):
    columns = [
        "Key", "Dataset Name", "Description", "Version", "Created On",
        "Updated On", "Contributors", "Data Files", "Tags",
        "License", "Source", "Schema Version"
    ]
    md_lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |"
    ]

    for key, data in json_data.items():
        contributors = "<br>".join(f"{c['name']} ({c['role']})"
                                   for c in data.get("contributors", []))
        data_files = "<br>".join(f"{f['file_name']} ({f['file_type']})"
                                 for f in data.get("data_files", []))
        tags = ", ".join(data.get("tags", []))

        row_cells = [
            key,
            data.get("dataset_name", ""),
            data.get("description", "").replace("\n", " "),
            data.get("version", ""),
            data.get("created_on", ""),
            data.get("updated_on", ""),
            contributors,
            data_files,
            tags,
            data.get("license", ""),
            data.get("source", ""),
            data.get("schema_version", "")
        ]
        md_lines.append("| " + " | ".join(row_cells) + " |")
    return "Below is a list of available data sets.\n\n" + "\n".join(md_lines) + "\n"


def wrap_front_matter(content, title = "Dashboard", layout = "single", permalink = "/dashboard/"):
    post = frontmatter.Post(content, **{"title": title, "layout": layout, "permalink":permalink})
    return frontmatter.dumps(post)


def write_to_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main(in_json, out_md):
    data = load_json(in_json)
    md = generate_md_table(data)
    full = wrap_front_matter(md)
    write_to_file(out_md, full)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python json2table.py <input.json> <output.md>")
    main(sys.argv[1], sys.argv[2])

