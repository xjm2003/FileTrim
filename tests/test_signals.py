from filetrim.processing.signals import extract_date, extract_title


def test_extract_title_returns_first_meaningful_line() -> None:
    text = "BIOSTAT 821\nFinal Project\nDue: April 24, 2026"
    assert extract_title(text) == "Final Project"


def test_extract_date_normalizes_long_month_format() -> None:
    text = "BIOSTAT 821\nFinal Project\nDue: April 24, 2026"
    assert extract_date(text) == "2026-04-24"
