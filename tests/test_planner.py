from pathlib import Path

from filetrim.execution.planner import RenamePlan, build_plan


def test_build_plan_returns_rename_plan() -> None:
    old_path = Path("example.pdf")

    plan = build_plan(
        old_path=old_path,
        new_filename="new-name.pdf",
        reason="test reason",
        dry_run=True,
    )

    assert isinstance(plan, RenamePlan)
    assert plan.old_path == old_path
    assert plan.new_path == Path("new-name.pdf")
    assert plan.reason == "test reason"
    assert plan.dry_run is True


def test_build_plan_places_new_file_in_same_directory() -> None:
    old_path = Path("/tmp/files/example.pdf")

    plan = build_plan(
        old_path=old_path,
        new_filename="renamed.pdf",
        reason="same directory check",
        dry_run=False,
    )

    assert plan.new_path == Path("/tmp/files/renamed.pdf")
    assert plan.old_path.parent == plan.new_path.parent