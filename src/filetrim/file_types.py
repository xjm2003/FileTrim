from __future__ import annotations

from enum import Enum
from pathlib import Path


class FileType(str, Enum):
    TXT = "txt"
    MD = "md"
    PDF = "pdf"
    DOCX = "docx"


SUPPORTED_SUFFIXES = {
    ".txt": FileType.TXT,
    ".md": FileType.MD,
    ".pdf": FileType.PDF,
    ".docx": FileType.DOCX,
}


def detect_file_type(path: str | Path) -> FileType:
    """Return the supported file type for a path based on its suffix."""
    suffix = Path(path).suffix.lower()
    try:
        return SUPPORTED_SUFFIXES[suffix]
    except KeyError as exc:
        raise ValueError(f"Unsupported file type: {suffix or '<none>'}") from exc
