from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from filetrim.file_types import FileType


@dataclass(slots=True)
class ExtractedContent:
    """Unified extraction result used by downstream processing."""

    source_path: Path
    file_type: FileType
    suffix: str
    text: str
    metadata: dict[str, str] = field(default_factory=dict)
