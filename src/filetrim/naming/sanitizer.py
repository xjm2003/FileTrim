import re


def sanitize_filename(name: str, max_length: int = 80) -> str:
    """Sanitize a filename stem into a safe slug-like string."""
    name = re.sub(r'[\\/:*?"<>|]+', "", name)
    name = name.strip().lower()
    name = re.sub(r"\s+", "-", name)
    name = re.sub(r"[-_]+", "-", name)
    name = name.strip("-_.")

    if len(name) > max_length:
        name = name[:max_length].rstrip("-_.")

    return name or "document"
