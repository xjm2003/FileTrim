import pytest

from filetrim.extractor.base import extract_content


def test_extract_content_rejects_unsupported_file_type() -> None:
    with pytest.raises(ValueError, match="Unsupported file type"):
        extract_content("archive.csv")
