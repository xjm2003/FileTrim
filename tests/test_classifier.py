from filetrim.processing.classifier import classify_document


def test_classify_assignment() -> None:
    text = "BIOSTAT 821 Final Project Due: April 24, 2026"
    assert classify_document(text) == "assignment"


def test_classify_resume() -> None:
    text = "Resume\nEducation\nExperience\nSkills"
    assert classify_document(text) == "resume"


def test_classify_document_default() -> None:
    text = "Random notes without strong keywords"
    assert classify_document(text) == "document"
