from filetrim.naming.sanitizer import sanitize_filename


def test_sanitize_filename_removes_invalid_chars() -> None:
    assert sanitize_filename("Final: Project?") == "final-project"


def test_sanitize_filename_collapses_spaces() -> None:
    assert sanitize_filename("Final   Project") == "final-project"


def test_sanitize_filename_limits_length() -> None:
    result = sanitize_filename("a" * 100, max_length=20)
    assert len(result) <= 20
