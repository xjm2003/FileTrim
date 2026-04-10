from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from filetrim.file_types import FileType, detect_file_type
from filetrim.models import ExtractedContent


class BaseExtractor(ABC):
    supported_types: tuple[FileType, ...] = ()

    def can_extract(self, file_type: FileType) -> bool:
        return file_type in self.supported_types

    @abstractmethod
    def extract(self, path: str | Path) -> ExtractedContent:
        """Extract plain text and minimal metadata from a supported file."""


def get_extractor(path: str | Path) -> BaseExtractor:
    file_type = detect_file_type(path)

    if file_type in (FileType.TXT, FileType.MD):
        from filetrim.extractor.text_extractor import TextExtractor

        return TextExtractor()
    if file_type is FileType.PDF:
        from filetrim.extractor.pdf_extractor import PdfExtractor

        return PdfExtractor()
    if file_type is FileType.DOCX:
        from filetrim.extractor.docx_extractor import DocxExtractor

        return DocxExtractor()

    raise ValueError(f"No extractor available for file type: {file_type}")


def extract_content(path: str | Path) -> ExtractedContent:
    return get_extractor(path).extract(path)
