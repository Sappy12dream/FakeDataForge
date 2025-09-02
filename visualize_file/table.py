from rich.console import Console
from rich.table import Table
import pandas as pd

console = Console()

def render_table(df: pd.DataFrame, max_rows: int = 20):
    """Render DataFrame as a terminal table (first max_rows)."""
    table = Table(show_header=True, header_style="bold magenta")
    for col in df.columns:
        table.add_column(str(col))

    for _, row in df.head(max_rows).iterrows():
        table.add_row(*[str(v) for v in row.values])

    console.print(table)

    if len(df) > max_rows:
        console.print(f"... {len(df) - max_rows} more rows not shown", style="dim")
