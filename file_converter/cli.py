# file_converter/cli.py
from pathlib import Path
import typer
from .reader import read_file
from .writer import write_file

app = typer.Typer(help="Convert files between CSV, Parquet, and Excel formats.")

@app.command()
def convert(
    input_file: str = typer.Argument(..., help="Path to input file"),
    output_file: str = typer.Option(None, "-o", "--output", help="Path to output file")
):
    """
    Convert a file between supported formats.
    """
    input_path = Path(input_file)
    if not input_path.exists():
        typer.echo(f"❌ Input file '{input_file}' does not exist.")
        raise typer.Exit(code=1)

    try:
        df = read_file(input_path)
    except Exception as e:
        typer.echo(f"❌ Failed to read input file: {e}")
        raise typer.Exit(code=1)

    if output_file:
        output_path = Path(output_file)
    else:
        # Default: CSV → Parquet, others → CSV
        default_ext = ".parquet" if input_path.suffix.lower() == ".csv" else ".csv"
        output_path = input_path.with_suffix(default_ext)

    try:
        write_file(output_path, df)
    except Exception as e:
        typer.echo(f"❌ Failed to write output file: {e}")
        raise typer.Exit(code=1)

    typer.echo(f"✅ Converted '{input_file}' → '{output_path}'")
