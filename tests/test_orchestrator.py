from pathlib import Path

import pytest

from filetrim.orchestrator import RenameOrchestrator


def test_orchestrator_raises_for_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "missing.txt"
    orchestrator = RenameOrchestrator()

    with pytest.raises(FileNotFoundError, match="File not found"):
        orchestrator.propose_plan(missing, dry_run=True)


def test_orchestrator_raises_for_directory(tmp_path: Path) -> None:
    directory = tmp_path / "folder"
    directory.mkdir()

    orchestrator = RenameOrchestrator()

    with pytest.raises(ValueError, match="Path is not a file"):
        orchestrator.propose_plan(directory, dry_run=True)


def test_orchestrator_generates_expected_plan_for_txt_file(tmp_path: Path) -> None:
    sample = tmp_path / "raw_notes.txt"
    sample.write_text("BIOSTAT 821\nFinal Project\nDue: April 24, 2026")

    orchestrator = RenameOrchestrator()
    plan = orchestrator.propose_plan(sample, dry_run=True)

    assert plan.old_path == sample
    assert plan.new_path.parent == sample.parent
    assert plan.new_path.name == "2026-04-24-assignment-final-project.txt"
    assert plan.reason == "generated from extracted content (assignment)"
    assert plan.dry_run is True


def test_orchestrator_generates_expected_plan_for_docx_like_content(
        tmp_path: Path
        ) -> None:
    # This test stays on TXT so it does not depend on generating a DOCX fixture here.
    sample = tmp_path / "resume.txt"
    sample.write_text("Resume\nEducation\nExperience\nSkills")

    orchestrator = RenameOrchestrator()
    plan = orchestrator.propose_plan(sample, dry_run=True)

    assert plan.old_path == sample
    assert plan.new_path.suffix == ".txt"
    assert plan.new_path.name == "resume-resume.txt"
    assert "resume" in plan.reason