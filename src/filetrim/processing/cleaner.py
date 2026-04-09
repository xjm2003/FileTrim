import re


def normalize_text(text: str) -> str:
    """Normalize whitespace while preserving line structure."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    cleaned_lines = [re.sub(r"\s+", " ", line).strip() for line in lines]
    nonempty = [line for line in cleaned_lines if line]
    return "\n".join(nonempty)
