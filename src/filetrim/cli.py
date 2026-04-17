from pathlib import Path

import typer

from filetrim.execution.executor import execute_plan
from filetrim.orchestrator import RenameOrchestrator

app = typer.Typer(help="Content-aware file renaming tool.")


@app.command()
def rename(
    path: str,
    dry_run: bool = typer.Option(
        True,
        "--dry-run/--execute",
        help="Preview rename without changing the file, or perform the rename.",
    ),
) -> None:
    """
    Rename a file based on extracted content.
    """
    file_path = Path(path)

    try:
        orchestrator = RenameOrchestrator()
        plan = orchestrator.propose_plan(file_path, dry_run=dry_run)
        final_path = execute_plan(plan)
    except Exception as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(code=1) from exc

    typer.echo(f"Reason: {plan.reason}")
    typer.echo(f"{plan.old_path.name} -> {final_path.name}")

    if plan.dry_run:
        typer.echo("Dry run only. No file was renamed.")
    else:
        typer.echo("Rename completed.")


if __name__ == "__main__":
    app()