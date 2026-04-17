from pathlib import Path

from filetrim.execution.executor import execute_plan
from filetrim.orchestrator import RenameOrchestrator


def test_end_to_end_dry_run_pipeline_for_txt_file(tmp_path: Path) -> None:
    sample = tmp_path / "notes.txt"
    sample.write_text("BIOSTAT 821\nFinal Project\nDue: April 24, 2026")

    orchestrator = RenameOrchestrator()
    plan = orchestrator.propose_plan(sample, dry_run=True)
    final_path = execute_plan(plan)

    assert sample.exists()
    assert final_path == tmp_path / "2026-04-24-assignment-final-project.txt"
    assert not final_path.exists()


def test_end_to_end_execute_pipeline_for_txt_file(tmp_path: Path) -> None:
    sample = tmp_path / "notes.txt"
    sample.write_text("BIOSTAT 821\nFinal Project\nDue: April 24, 2026")

    orchestrator = RenameOrchestrator()
    plan = orchestrator.propose_plan(sample, dry_run=False)
    final_path = execute_plan(plan)

    assert not sample.exists()
    assert final_path.exists()
    assert final_path.name == "2026-04-24-assignment-final-project.txt"
    assert final_path.read_text() == "BIOSTAT 821\nFinal Project\nDue: April 24, 2026"


def test_end_to_end_execute_pipeline_handles_conflicts(tmp_path: Path) -> None:
    sample = tmp_path / "notes.txt"
    sample.write_text("BIOSTAT 821\nFinal Project\nDue: April 24, 2026")

    existing = tmp_path / "2026-04-24-assignment-final-project.txt"
    existing.write_text("older file")

    orchestrator = RenameOrchestrator()
    plan = orchestrator.propose_plan(sample, dry_run=False)
    final_path = execute_plan(plan)

    assert existing.exists()
    assert final_path.exists()
    assert final_path.name == "2026-04-24-assignment-final-project_1.txt"
    assert not sample.exists()