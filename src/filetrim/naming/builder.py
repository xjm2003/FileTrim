from filetrim.naming.sanitizer import sanitize_filename
from filetrim.naming.templates import TEMPLATES
from filetrim.processing.classifier import classify_document
from filetrim.processing.cleaner import normalize_text
from filetrim.processing.signals import extract_date, extract_title


def build_filename(text: str, suffix: str) -> str:
    """Build a proposed filename from extracted text and original suffix."""
    cleaned = normalize_text(text)
    category = classify_document(cleaned)
    title = extract_title(cleaned) or "untitled"
    date = extract_date(cleaned) or "undated"

    template = TEMPLATES[category]
    stem = template.format(
        date=date,
        category=category,
        title=title,
    )
    safe_stem = sanitize_filename(stem)
    return f"{safe_stem}{suffix}"
