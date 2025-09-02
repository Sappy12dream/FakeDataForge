# fake_data_generator/__init__.py
"""
Fake Data Generator Package

Modules:
- cli.py      : Typer CLI entrypoint
- generator.py: Data generation logic
- schema.py   : Table/column schema definitions
- prompts.py  : Interactive prompts for user input
- prebuilt.py : Prebuilt schema flow
- custom.py   : Custom schema flow
"""

__version__ = "0.1.0"

# Optional: expose the CLI app for setuptools entry point
from .cli import app
