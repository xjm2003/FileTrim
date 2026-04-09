from filetrim.processing.cleaner import normalize_text


def test_normalize_text_collapses_spaces() -> None:
    text = "BIOSTAT 821\n\nFinal   Project\nDue:   April 24, 2026"
    assert normalize_text(text) == "BIOSTAT 821\nFinal Project\nDue: April 24, 2026"
