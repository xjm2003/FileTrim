from pathlib import Path

from filetrim.extractor.text_extractor import TextExtractor
from filetrim.file_types import FileType


def test_text_extractor_reads_txt_file(tmp_path: Path) -> None:
    sample = tmp_path / "notes.txt"
    sample.write_text("Line one\nLine two", encoding="utf-8")

    result = TextExtractor().extract(sample)

    assert result.file_type is FileType.TXT
    assert result.suffix == ".txt"
    assert result.text == "Line one\nLine two"
    assert result.metadata["source_name"] == "notes.txt"


def test_text_extractor_reads_markdown_file(tmp_path: Path) -> None:
    sample = tmp_path / "readme.md"
    sample.write_text("# Title\n\nParagraph", encoding="utf-8")

    result = TextExtractor().extract(sample)

    assert result.file_type is FileType.MD
    assert "# Title" in result.text
