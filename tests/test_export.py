import os
from scraper.export import export_csv, export_tsv, export_markdown

sample = {
    "Camping": {
        "url": "https://example.com",
        "requirements": ["Req 1", "Req 2"]
    }
}

def test_export_csv(tmp_path):
    out = tmp_path / "out.csv"
    export_csv(sample, out)
    assert out.exists()

def test_export_tsv(tmp_path):
    out = tmp_path / "out.tsv"
    export_tsv(sample, out)
    assert out.exists()

def test_export_markdown(tmp_path):
    out = tmp_path / "out.md"
    export_markdown(sample, out)
    assert out.exists()

