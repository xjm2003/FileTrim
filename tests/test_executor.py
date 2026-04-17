from pathlib import Path

from filetrim.execution.executor import execute_plan, resolve_conflict
from filetrim.execution.planner import build_plan


def test_resolve_conflict_returns_original_path_when_available(tmp_path: Path) -> None:
    target = tmp_path / "renamed.txt"

    resolved = resolve_conflict(target)

    assert resolved == target


def test_resolve_conflict_appends_counter_when_target_exists(tmp_path: Path) -> None:
    target = tmp_path / "renamed.txt"
    target.write_text("already exists")

    resolved = resolve_conflict(target)

    assert resolved == tmp_path / "renamed_1.txt"


def test_resolve_conflict_increments_until_available(tmp_path: Path) -> None:
    (tmp_path / "renamed.txt").write_text("taken")
    (tmp_path / "renamed_1.txt").write_text("taken")
    (tmp_path / "renamed_2.txt").write_text("taken")

    resolved = resolve_conflict(tmp_path / "renamed.txt")

    assert resolved == tmp_path / "renamed_3.txt"


def test_execute_plan_dry_run_does_not_rename_file(tmp_path: Path) -> None:
    old_path = tmp_path / "old.txt"
    old_path.write_text("hello world")

    plan = build_plan(
        old_path=old_path,
        new_filename="new.txt",
        reason="dry run",
        dry_run=True,
    )

    result = execute_plan(plan)

    assert old_path.exists()
    assert result == tmp_path / "new.txt"
    assert not (tmp_path / "new.txt").exists()


def test_execute_plan_renames_file_when_not_dry_run(tmp_path: Path) -> None:
    old_path = tmp_path / "old.txt"
    old_path.write_text("hello world")

    plan = build_plan(
        old_path=old_path,
        new_filename="new.txt",
        reason="real execution",
        dry_run=False,
    )

    result = execute_plan(plan)

    assert not old_path.exists()
    assert result.exists()
    assert result.name == "new.txt"
    assert result.read_text() == "hello world"


def test_execute_plan_avoids_name_conflicts(tmp_path: Path) -> None:
    old_path = tmp_path / "old.txt"
    old_path.write_text("fresh file")

    existing_target = tmp_path / "new.txt"
    existing_target.write_text("existing file")

    plan = build_plan(
        old_path=old_path,
        new_filename="new.txt",
        reason="conflict handling",
        dry_run=False,
    )

    result = execute_plan(plan)

    assert existing_target.exists()
    assert result == tmp_path / "new_1.txt"
    assert result.exists()
    assert result.read_text() == "fresh file"
    assert not old_path.exists()