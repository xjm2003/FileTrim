from pathlib import Path

from typer.testing import CliRunner

from filetrim.cli import app

runner = CliRunner()


def test_cli_rename_dry_run(tmp_path: Path) -> None:
    sample = tmp_path / "notes.txt"
    sample.write_text("BIOSTAT 821\nFinal Project\nDue: April 24, 2026")

    result = runner.invoke(app, ["rename", str(sample), "--dry-run"])

    assert result.exit_code == 0
    assert "Reason: generated from extracted content (assignment)" in result.output
    assert "notes.txt -> 2026-04-24-assignment-final-project.txt" in result.output
    assert "Dry run only. No file was renamed." in result.output
    assert sample.exists()


def test_cli_rename_execute(tmp_path: Path) -> None:
    sample = tmp_path / "notes.txt"
    sample.write_text("BIOSTAT 821\nFinal Project\nDue: April 24, 2026")

    result = runner.invoke(app, ["rename", str(sample), "--execute"])

    assert result.exit_code == 0
    assert "Rename completed." in result.output
    assert not sample.exists()
    assert (tmp_path / "2026-04-24-assignment-final-project.txt").exists()