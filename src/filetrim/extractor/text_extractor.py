from __future__ import annotations

from pathlib import Path

from filetrim.extractor.base import BaseExtractor
from filetrim.file_types import FileType, detect_file_type
from filetrim.models import ExtractedContent


class TextExtractor(BaseExtractor):
    supported_types = (FileType.TXT, FileType.MD)

    def extract(self, path: str | Path) -> ExtractedContent:
        source_path = Path(path)
        file_type = detect_file_type(source_path)

        if not self.can_extract(file_type):
            raise ValueError(f"TextExtractor does not support: {file_type}")

        text = source_path.read_text(encoding="utf-8")
        return ExtractedContent(
            source_path=source_path,
            file_type=file_type,
            suffix=source_path.suffix.lower(),
            text=text,
            metadata={"source_name": source_path.name},
        )
