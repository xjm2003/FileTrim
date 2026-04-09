from filetrim.naming.builder import build_filename


def test_build_filename_assignment_example() -> None:
    text = "BIOSTAT 821\nFinal Project\nDue: April 24, 2026"
    result = build_filename(text, ".pdf")
    assert result == "2026-04-24-assignment-final-project.pdf"


def test_build_filename_handles_missing_date() -> None:
    text = "Resume\nEducation\nExperience"
    result = build_filename(text, ".docx")
    assert result == "resume-resume.docx"
