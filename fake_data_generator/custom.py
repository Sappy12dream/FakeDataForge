# fake_data_generator/custom.py
"""
Custom schema generator.
"""

from datetime import datetime
from .schema import TableConfig, ColumnConfig
from .generator import DataGenerator
from . import prompts

def run_custom():
    """
    Run the custom schema flow.
    """
    print("\n--- Custom Schema ---")
    out_dir = prompts.input_with_default("Enter output folder path", "./fake_data")
    table_configs = []
    existing_tables = {}

    while True:
        table_name = prompts.input_with_default(
            "Enter table name (Enter empty to finish)", ""
        )
        if not table_name:
            break
        if table_name in existing_tables:
            print("Table name already exists.")
            continue

        n_cols = prompts.input_int(f"Number of columns in '{table_name}'", default=3, min_val=1)
        columns = []
        has_pk = False

        for i in range(n_cols):
            print(f"\nColumn {i+1}/{n_cols} for table '{table_name}':")
            col_name = prompts.input_with_default("Column name", f"col{i+1}")

            col_type = prompts.input_choice(
                "Column type",
                ["pk", "fk", "name", "email", "address", "date", "number", "float", "boolean", "choice"]
            )

            # PK enforcement
            if col_type == "pk":
                if has_pk:
                    print("Table already has a PK. Choose another type.")
                    col_type = prompts.input_choice(
                        "Pick type",
                        ["fk", "name", "email", "address", "date", "number", "float", "boolean", "choice"]
                    )
                else:
                    has_pk = True
                    columns.append(ColumnConfig(col_name, "pk"))
                    continue

            # Nullable support
            nullable = prompts.input_nullable("Allow null values?", default=False)

            # FK handling
            if col_type == "fk":
                if not existing_tables:
                    print("No previous tables to reference. Choose another type.")
                    col_type = prompts.input_choice(
                        "Pick type",
                        ["name", "email", "address", "date", "number", "float", "boolean", "choice"]
                    )
                else:
                    pk_targets = [(t.name, t.pk_column().name) for t in table_configs if t.pk_column()]
                    print("Available FK targets:")
                    for idx, (tn, cn) in enumerate(pk_targets, start=1):
                        print(f"{idx}. {tn}.{cn}")
                    target_idx = prompts.input_int("Select target by number", default=1, min_val=1, max_val=len(pk_targets))
                    ref_table, ref_column = pk_targets[target_idx-1]
                    columns.append(ColumnConfig(col_name, "fk", nullable=nullable, ref_table=ref_table, ref_column=ref_column))
                    continue

            # Date type
            if col_type == "date":
                start = prompts.input_date("Start date")
                end = prompts.input_date("End date")
                while end < start:
                    print("End date cannot be before start date.")
                    end = prompts.input_date("End date")
                columns.append(ColumnConfig(col_name, "date", nullable=nullable, date_start=start, date_end=end))
                continue

            # Number type
            if col_type == "number":
                min_v = prompts.input_int("Min value", 0)
                max_v = prompts.input_int("Max value", max(1, min_v))
                columns.append(ColumnConfig(col_name, "number", nullable=nullable, num_min=min_v, num_max=max_v))
                continue

            # Float type
            if col_type == "float":
                min_f = prompts.input_float("Min value", 0.0)
                max_f = prompts.input_float("Max value", 1.0)
                columns.append(ColumnConfig(col_name, "float", nullable=nullable, float_min=min_f, float_max=max_f))
                continue

            # Boolean type
            if col_type == "boolean":
                columns.append(ColumnConfig(col_name, "boolean", nullable=nullable))
                continue

            # Choice type
            if col_type == "choice":
                choices = prompts.input_comma_separated("Enter comma-separated choices")
                columns.append(ColumnConfig(col_name, "choice", nullable=nullable, choices=choices))
                continue

            # Faker-backed types
            if col_type in ("name", "email", "address"):
                columns.append(ColumnConfig(col_name, col_type, nullable=nullable))

        n_rows = prompts.input_int(f"Number of rows for '{table_name}'", default=100, min_val=0)
        tcfg = TableConfig(name=table_name, columns=columns, n_rows=n_rows)
        table_configs.append(tcfg)
        existing_tables[table_name] = tcfg
        print(f"Configured table '{table_name}' with {len(columns)} columns.\n")

    if not table_configs:
        print("No tables defined.")
        return

    dg = DataGenerator(out_dir)
    for cfg in table_configs:
        rows = dg.generate_table(cfg)
        path = dg.write_csv(cfg, rows)
        print(f"✅ {cfg.name}.csv saved with {len(rows)} rows at {path}")
