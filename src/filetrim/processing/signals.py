import re
from datetime import datetime


def extract_title(text: str) -> str | None:
    """Extract a simple title candidate from the first meaningful lines."""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if not lines:
        return None

    for line in lines[:5]:
        lowered = line.lower()
        if re.fullmatch(r"[a-z]+\s+\d+", lowered):
            continue
        if re.match(r"^due[:\s]", lowered):
            continue
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", lowered):
            continue
        if len(line) >= 3:
            return line

    return lines[0]


def extract_date(text: str) -> str | None:
    """Extract and normalize one date candidate to YYYY-MM-DD."""
    patterns = [
        (r"\b(\d{4}-\d{2}-\d{2})\b", "%Y-%m-%d"),
        (r"\b(\d{2}/\d{2}/\d{4})\b", "%m/%d/%Y"),
        (r"\b([A-Z][a-z]+ \d{1,2}, \d{4})\b", "%B %d, %Y"),
        (r"\b([A-Z][a-z]{2} \d{1,2}, \d{4})\b", "%b %d, %Y"),
    ]

    for pattern, fmt in patterns:
        match = re.search(pattern, text)
        if match:
            raw = match.group(1)
            try:
                return datetime.strptime(raw, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue

    return None
