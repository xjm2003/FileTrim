import pytest

from filetrim.file_types import FileType, detect_file_type


def test_detect_file_type_for_supported_suffixes() -> None:
    assert detect_file_type("notes.txt") is FileType.TXT
    assert detect_file_type("README.md") is FileType.MD
    assert detect_file_type("paper.pdf") is FileType.PDF
    assert detect_file_type("resume.docx") is FileType.DOCX


def test_detect_file_type_rejects_unsupported_suffix() -> None:
    with pytest.raises(ValueError, match="Unsupported file type"):
        detect_file_type("archive.csv")
