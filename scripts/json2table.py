import json
import frontmatter

def generate_dashboard_md(
    json_path: str,
    output_md: str = "../docs/_pages/dashboard.md",
    title: str = "Dashboard",
    layout: str = "single",
    permalink: str = "/dashboard/"
):
    """
    Load dataset metadata from JSON and generate a Jekyll-ready Markdown file.

    Args:
        json_path: Path to your JSON file (e.g., 'datasets.json').
        output_md: Filename for the generated Markdown (default 'dashboard.md').
        title: YAML front-matter title.
        layout: Jekyll layout to apply.
        permalink: Page permalink.
    """
    # Load JSON
    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # Build Markdown table lines with headers and full columns
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

    # Assemble body with introduction and table
    body = "\n".join([
        "Below is a list of available data sets.",
        "",
        *md_lines,
        ""
    ])

    # YAML front matter metadata
    metadata = {
        "title": title,
        "layout": layout,
        "permalink": permalink
    }

    # Build Post and write to file using string output
    post = frontmatter.Post(body, **metadata)
    with open(output_md, "w", encoding="utf-8") as outf:
        outf.write(frontmatter.dumps(post))

  # print(f"Generated '{output_md}' with {len(json_data)} rows.")


if __name__ == "__main__":
    generate_dashboard_md("../docs/assets/js/all_metadata.json")

