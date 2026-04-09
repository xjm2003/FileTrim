from __future__ import annotations

from pathlib import Path

import fitz

from filetrim.extractor.base import BaseExtractor
from filetrim.file_types import FileType, detect_file_type
from filetrim.models import ExtractedContent


class PdfExtractor(BaseExtractor):
    supported_types = (FileType.PDF,)

    def extract(self, path: str | Path) -> ExtractedContent:
        source_path = Path(path)
        file_type = detect_file_type(source_path)

        if not self.can_extract(file_type):
            raise ValueError(f"PdfExtractor does not support: {file_type}")

        with fitz.open(source_path) as document:
            page_text = [page.get_text("text").strip() for page in document]

        text = "\n".join(chunk for chunk in page_text if chunk)
        return ExtractedContent(
            source_path=source_path,
            file_type=file_type,
            suffix=source_path.suffix.lower(),
            text=text,
            metadata={
                "page_count": str(len(page_text)),
                "source_name": source_path.name,
            },
        )
