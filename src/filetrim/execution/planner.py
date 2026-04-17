from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RenamePlan:
    old_path: Path
    new_path: Path
    reason: str
    dry_run: bool = True


def build_plan(
    old_path: Path,
    new_filename: str,
    reason: str,
    dry_run: bool = True,
) -> RenamePlan:
    """
    Build a rename plan without mutating the filesystem.
    """
    return RenamePlan(
        old_path=old_path,
        new_path=old_path.with_name(new_filename),
        reason=reason,
        dry_run=dry_run,
    )