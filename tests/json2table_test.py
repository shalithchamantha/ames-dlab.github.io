import sys
sys.path.insert(0,"scripts")

import json
import frontmatter
import pytest
import json2table


def test_load_json(tmp_path):
    # Prepare a temporary JSON file
    data = {"x": 42}
    test_file = tmp_path / "test.json"
    test_file.write_text(json.dumps(data), encoding="utf-8")

    result = json2table.load_json(str(test_file))
    assert result == data


def test_generate_md_table_simple():
    sample = {
        "foo": {
            "dataset_name": "FooDS",
            "description": "A description\nwith newline.",
            "version": "1.0",
            "created_on": "2025-01-01",
            "updated_on": "2025-06-01",
            "contributors": [{"name": "Alice", "role": "owner"}],
            "data_files": [{"file_name": "foo.csv", "file_type": "csv"}],
            "tags": ["alpha", "beta"],
            "license": "MIT",
            "source": "http://example.com",
            "schema_version": "1.2"
        }
    }

    md = json2table.generate_md_table(sample)
    # Check table header
    assert "| Key | Dataset Name | Description | Version | Created On | Updated On | Contributors | Data Files | Tags | License | Source | Schema Version |" in md
    # Check row values
    assert "| foo | FooDS | A description with newline." in md
    assert "Alice (owner)" in md
    assert "foo.csv (csv)" in md
    assert "alpha, beta" in md


def test_wrap_front_matter():
    body = "Sample body\n"
    fm = json2table.wrap_front_matter(body, title="T", layout="L", permalink="/p/")
    parsed = frontmatter.loads(fm)
    assert parsed.metadata["title"] == "T"
    assert parsed.metadata["layout"] == "L"
    assert parsed.metadata["permalink"] == "/p/"
    assert parsed.content.strip() == "Sample body"


def test_write_to_file(tmp_path):
    out = tmp_path / "out.md"
    content = "Hello!"
    json2table.write_to_file(str(out), content)
    assert out.read_text(encoding="utf-8") == content


def test_main_creates_file(tmp_path, monkeypatch):
    json_path = tmp_path / "meta.json"
    md_path = tmp_path / "out.md"
    sample = {"a": {"dataset_name": "A", "description": "", "version": "", "created_on": "", "updated_on": "",
                    "contributors": [], "data_files": [], "tags": [], "license": "", "source": "", "schema_version": ""}}
    json_path.write_text(json.dumps(sample), encoding="utf-8")

    # Run main
    json2table.main(str(json_path), str(md_path))
    content = md_path.read_text(encoding="utf-8")
    parsed = frontmatter.loads(content)
    assert "a | A |" in parsed.content

