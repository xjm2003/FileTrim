from pathlib import Path

from filetrim.execution.planner import RenamePlan


def resolve_conflict(path: Path) -> Path:
    """
    If the target path already exists, append _1, _2, ... before the suffix.
    """
    if not path.exists():
        return path

    parent = path.parent
    stem = path.stem
    suffix = path.suffix
    counter = 1

    while True:
        candidate = parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def execute_plan(plan: RenamePlan) -> Path:
    """
    Execute a rename plan.

    Returns the final target path. In dry-run mode, no file is changed.
    """
    target = resolve_conflict(plan.new_path)

    if plan.dry_run:
        return target

    plan.old_path.rename(target)
    return target