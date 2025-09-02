# fake_data_generator/prompts.py
"""
All input helpers for the CLI.
"""

from typing import List
from datetime import datetime

def input_with_default(prompt: str, default: str = "") -> str:
    val = input(f"{prompt} [{default}]: ").strip()
    return val if val else default

def input_int(prompt: str, default: int = 0, min_val: int = None, max_val: int = None) -> int:
    while True:
        val = input_with_default(prompt, str(default))
        try:
            val = int(val)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if min_val is not None and val < min_val:
            print(f"Value must be >= {min_val}")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be <= {max_val}")
            continue
        return val

def input_float(prompt: str, default: float = 0.0, min_val: float = None, max_val: float = None) -> float:
    while True:
        val = input_with_default(prompt, str(default))
        try:
            val = float(val)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if min_val is not None and val < min_val:
            print(f"Value must be >= {min_val}")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be <= {max_val}")
            continue
        return val

def input_date(prompt: str) -> datetime:
    while True:
        val = input(f"{prompt} (YYYY-MM-DD): ").strip()
        try:
            return datetime.strptime(val, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

def input_choice(prompt: str, options: List[str]) -> str:
    while True:
        val = input(f"{prompt} {options}: ").strip().lower()
        for opt in options:
            if val == opt.lower():
                return opt
        print("Invalid choice. Try again.")

def input_yesno(prompt: str, default: bool = False) -> bool:
    default_str = "y" if default else "n"
    val = input_with_default(f"{prompt} (y/n)", default_str).lower()
    return val.startswith("y")

def input_comma_separated(prompt: str, min_items: int = 1) -> List[str]:
    while True:
        val = input(f"{prompt} (comma-separated): ").strip()
        items = [x.strip() for x in val.split(",") if x.strip()]
        if len(items) < min_items:
            print(f"Please enter at least {min_items} item(s).")
            continue
        return items

def input_nullable(prompt: str, default: bool = False) -> bool:
    return input_yesno(f"{prompt} (Allow null values?)", default=default)
