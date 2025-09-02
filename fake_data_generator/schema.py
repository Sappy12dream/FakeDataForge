# fake_data_generator/schema.py
"""
Schema definitions for Fake Data Generator.

Contains TableConfig and ColumnConfig dataclasses, including support for:
- Primary keys (pk)
- Foreign keys (fk)
- Nullable columns
- Faker-backed types (name, email, address)
- Date, number, float, boolean, choice types
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

ColumnType = str  # 'pk' | 'fk' | 'name' | 'email' | 'address' | 'date' | 'number' | 'float' | 'boolean' | 'choice'

@dataclass
class ColumnConfig:
    name: str
    col_type: ColumnType
    # Nullable support
    nullable: bool = False        # If True, column can have null values
    null_prob: float = 0.2        # Probability of null if nullable

    # FK reference
    ref_table: Optional[str] = None
    ref_column: Optional[str] = None

    # Date bounds
    date_start: Optional[datetime] = None
    date_end: Optional[datetime] = None

    # Number bounds
    num_min: Optional[int] = None
    num_max: Optional[int] = None

    # Float bounds
    float_min: Optional[float] = None
    float_max: Optional[float] = None

    # Choice options
    choices: Optional[List[str]] = None

@dataclass
class TableConfig:
    name: str
    columns: List[ColumnConfig]
    n_rows: int

    # Helper: get PK column
    def pk_column(self) -> Optional[ColumnConfig]:
        for c in self.columns:
            if c.col_type == 'pk':
                return c
        return None

    # Helper: get column names in order
    def column_names(self) -> List[str]:
        return [c.name for c in self.columns]
