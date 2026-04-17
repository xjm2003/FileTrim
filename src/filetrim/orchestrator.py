from pathlib import Path

from filetrim.execution.planner import RenamePlan, build_plan
from filetrim.extractor.docx_extractor import DocxExtractor
from filetrim.extractor.pdf_extractor import PdfExtractor
from filetrim.extractor.text_extractor import TextExtractor
from filetrim.file_types import FileType, detect_file_type
from filetrim.naming.builder import build_filename
from filetrim.naming.sanitizer import sanitize_filename
from filetrim.processing.classifier import classify_document
from filetrim.processing.cleaner import normalize_text


class RenameOrchestrator:
    """
    Coordinates the end-to-end rename pipeline:
    file type detection -> extraction -> cleaning -> classification
    -> filename generation -> sanitization -> rename plan
    """

    def __init__(self) -> None:
        self.extractors = {
            FileType.TXT: TextExtractor(),
            FileType.MD: TextExtractor(),
            FileType.PDF: PdfExtractor(),
            FileType.DOCX: DocxExtractor(),
        }

    def propose_plan(self, path: Path, dry_run: bool = True) -> RenamePlan:
        """
        Generate a RenamePlan for the given file.
        """
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {path}")

        file_type = detect_file_type(path.name)
        extractor = self.extractors[file_type]

        extracted = extractor.extract(path)
        text = normalize_text(extracted.text)

        # Keep classification explicit for logging / reason text,
        # even if build_filename already contains some internal heuristics.
        doc_type = classify_document(text)

        built_name = build_filename(text, path.suffix)

        # Be conservative: sanitize only the stem and preserve the suffix.
        built_path = Path(built_name)
        safe_stem = sanitize_filename(built_path.stem)
        safe_name = safe_stem + built_path.suffix.lower()

        reason = f"generated from extracted content ({doc_type})"

        return build_plan(
            old_path=path,
            new_filename=safe_name,
            reason=reason,
            dry_run=dry_run,
        )