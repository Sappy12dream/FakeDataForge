# fake_data_generator/prebuilt.py
"""
Prebuilt schema generator: Users, Products, Orders.
"""

from datetime import datetime
from .schema import TableConfig, ColumnConfig
from .generator import DataGenerator
from . import prompts

def run_prebuilt():
    """
    Run the prebuilt schema generation flow:
    - Users
    - Products
    - Orders
    """
    print("\n--- Prebuilt Schema: Users, Products, Orders ---")
    out_dir = prompts.input_with_default("Enter output folder path", "./fake_data")

    # Row counts
    n_users = prompts.input_int("Number of Users", default=100, min_val=0)
    n_products = prompts.input_int("Number of Products", default=50, min_val=0)
    n_orders = 0
    if n_users > 0 and n_products > 0:
        n_orders = prompts.input_int("Number of Orders", default=200, min_val=0)
    else:
        print("Orders will have 0 rows because Users or Products is 0.")

    dg = DataGenerator(out_dir)

    # Table definitions
    users_cfg = TableConfig(
        name="Users",
        columns=[
            ColumnConfig("user_id", "pk"),
            ColumnConfig("name", "name"),
            ColumnConfig("email", "email"),
            ColumnConfig("address", "address"),
        ],
        n_rows=n_users,
    )

    products_cfg = TableConfig(
        name="Products",
        columns=[
            ColumnConfig("product_id", "pk"),
            ColumnConfig("name", "choice", choices=["Laptop", "Phone", "Tablet", "Camera"]),
            ColumnConfig("price", "number", num_min=100, num_max=2000),
        ],
        n_rows=n_products,
    )

    orders_cfg = TableConfig(
        name="Orders",
        columns=[
            ColumnConfig("order_id", "pk"),
            ColumnConfig("user_id", "fk", ref_table="Users", ref_column="user_id"),
            ColumnConfig("product_id", "fk", ref_table="Products", ref_column="product_id"),
            ColumnConfig("quantity", "number", num_min=1, num_max=5),
            ColumnConfig("order_date", "date", date_start=datetime(2023,1,1), date_end=datetime(2023,12,31)),
        ],
        n_rows=n_orders,
    )

    # Generate tables in dependency order
    for cfg in [users_cfg, products_cfg, orders_cfg]:
        rows = dg.generate_table(cfg)
        path = dg.write_csv(cfg, rows)
        print(f"✅ {cfg.name}.csv saved with {len(rows)} rows at {path}")
