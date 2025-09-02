import typer
from pathlib import Path
from .reader import read_file
from .table import render_table

app = typer.Typer(help="Visualize CSV, Parquet, and Excel files in terminal.")

@app.command()
def view(input_file: str, max_rows: int = 20):
    """Visualize a file in table form (first max_rows rows)."""
    path = Path(input_file)
    if not path.exists():
        typer.echo(f"❌ File not found: {input_file}")
        raise typer.Exit(1)

    try:
        df = read_file(path)
        render_table(df, max_rows=max_rows)
    except Exception as e:
        typer.echo(f"❌ Error reading file: {e}")
        raise typer.Exit(1)
