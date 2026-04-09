from pathlib import Path

import fitz

from filetrim.extractor.pdf_extractor import PdfExtractor
from filetrim.file_types import FileType


def test_pdf_extractor_reads_text_pdf(tmp_path: Path) -> None:
    sample = tmp_path / "sample.pdf"

    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Final Project\nDue: April 24, 2026")
    document.save(sample)
    document.close()

    result = PdfExtractor().extract(sample)

    assert result.file_type is FileType.PDF
    assert result.suffix == ".pdf"
    assert "Final Project" in result.text
    assert result.metadata["page_count"] == "1"
