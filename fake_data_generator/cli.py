# fake_data_generator/cli.py
"""
CLI entrypoint for Fake Data Generator using Typer.
"""

import typer
from datetime import datetime
from typing import List

from .schema import TableConfig, ColumnConfig
from .generator import DataGenerator
from . import prompts
from .prebuilt import run_prebuilt as prebuilt_flow
from .custom import run_custom as custom_flow

app = typer.Typer(help="Generate fake CSV datasets with PK/FK relationships.")

# -------------------------------
# Main CLI entry
# -------------------------------

@app.command()
def main():
    """
    Interactive CLI menu.
    """
    print("\n=== Fake Data Generator ===")
    print("1) Prebuilt schema (Users, Products, Orders)")
    print("2) Custom schema")
    print("3) Exit")

    choice = prompts.input_with_default("Enter choice", "1")
    if choice == "1":
        prebuilt_flow()
    elif choice == "2":
        custom_flow()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice.")
