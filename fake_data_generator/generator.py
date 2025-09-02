# fake_data_generator/generator.py
"""
DataGenerator for Fake Data Generator.

Generates rows for tables based on TableConfig and ColumnConfig,
handles PK/FK relationships, nullable columns, and CSV export.
"""

from __future__ import annotations
import csv
import os
import random
import uuid
from datetime import timedelta
from typing import Dict, List

from faker import Faker
from .schema import TableConfig, ColumnConfig

fake = Faker()


class DataGenerator:
    def __init__(self, output_dir: str):
        self.output_dir = os.path.abspath(os.path.expanduser(output_dir))
        os.makedirs(self.output_dir, exist_ok=True)
        self.generated: Dict[str, List[dict]] = {}   # table_name -> list of rows

    # ---- generic helpers

    def _gen_value(self, col: ColumnConfig, current_table: str):
        """Generate a value for a column, respecting nullable and type."""
        if col.nullable and random.random() < col.null_prob:
            return None

        if col.col_type == 'pk' or col.col_type == 'fk':
            return str(uuid.uuid4())
        elif col.col_type == 'name':
            return fake.name()
        elif col.col_type == 'email':
            return fake.email()
        elif col.col_type == 'address':
            return fake.address().replace("\n", ", ")
        elif col.col_type == 'date':
            start, end = col.date_start, col.date_end
            if not start or not end or start > end:
                raise ValueError(f"Invalid date bounds for column '{col.name}'")
            delta_days = (end - start).days
            offset = random.randint(0, max(0, delta_days))
            return (start + timedelta(days=offset)).strftime("%Y-%m-%d")
        elif col.col_type == 'number':
            if col.num_min is None or col.num_max is None or col.num_min > col.num_max:
                raise ValueError(f"Invalid number bounds for column '{col.name}'")
            return random.randint(col.num_min, col.num_max)
        elif col.col_type == 'float':
            if col.float_min is None or col.float_max is None or col.float_min > col.float_max:
                raise ValueError(f"Invalid float bounds for column '{col.name}'")
            return round(random.uniform(col.float_min, col.float_max), 2)
        elif col.col_type == 'boolean':
            return random.choice([True, False])
        elif col.col_type == 'choice':
            if not col.choices:
                raise ValueError(f"No choices provided for column '{col.name}'")
            return random.choice(col.choices)
        else:
            return None

    # ---- table generation

    def generate_table(self, config: TableConfig) -> List[dict]:
        """Generate rows for a table respecting PK/FK and nullable rules."""
        fk_columns = [c for c in config.columns if c.col_type == 'fk']
        for fk in fk_columns:
            if not fk.ref_table or not fk.ref_column:
                raise ValueError(f"FK column '{fk.name}' must reference a table.column")
            if fk.ref_table not in self.generated or len(self.generated[fk.ref_table]) == 0:
                if config.n_rows > 0:
                    print(f"Warning: '{config.name}' references '{fk.ref_table}' with 0 rows. Setting row count to 0.")
                    config.n_rows = 0

        rows: List[dict] = []
        pk_col = config.pk_column()

        for _ in range(config.n_rows):
            row: dict = {}

            # Assign PK
            if pk_col:
                row[pk_col.name] = str(uuid.uuid4())

            # Assign other columns
            for col in config.columns:
                if col.col_type == 'pk':
                    continue
                if col.col_type == 'fk':
                    candidates = self.generated[col.ref_table]
                    ref_val = random.choice(candidates)[col.ref_column] if candidates else None
                    row[col.name] = ref_val
                else:
                    row[col.name] = self._gen_value(col, config.name)

            rows.append(row)

        self.generated[config.name] = rows
        return rows

    # ---- CSV export

    def write_csv(self, table: TableConfig, rows: List[dict]) -> str:
        """Write a table to CSV, preserving column order."""
        path = os.path.join(self.output_dir, f"{table.name}.csv")
        fieldnames = table.column_names()
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                row_clean = {k: ("" if v is None else v) for k, v in r.items()}
                writer.writerow(row_clean)
        return path
