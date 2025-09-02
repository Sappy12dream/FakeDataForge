Fake Data Generator & File Converter

A Python CLI toolkit for generating fake datasets with PK/FK relationships and converting files between CSV, Parquet, and Excel formats. Ideal for testing, prototyping, or data pipeline development.

Features
1. Fake Data Generator

Generate tables with primary keys (PK) and foreign keys (FK).

Support for multiple column types:

pk, fk, name, email, address, number, float, boolean, choice, date.

Configure nullable columns.

Custom number of rows per table.

Export datasets to CSV files.

Prebuilt example schema: Users, Products, Orders.

2. File Converter

Convert files between supported formats:

CSV ↔ Parquet ↔ Excel (.xlsx, .xls)

Automatic format detection based on file extension.

Simple CLI interface for quick conversions.

Installation
# Clone the repository
git clone https://github.com/yourusername/FakeDataForge.git
cd FakeDataForge

# Install in editable mode
pip install -e .

CLI Usage
Fake Data Generator
# Launch the interactive CLI
fakegen


Options:

Prebuilt schema (Users, Products, Orders)

Custom schema

Exit

Follow the prompts to configure tables, columns, types, and row counts.

File Converter
# Convert a file (auto output name if -o not provided)
convertfile input.csv
convertfile input.xlsx -o output.parquet


Supported input/output formats: csv, parquet, xlsx, xls.

Examples

Generate prebuilt data:

fakegen
# Choose "1" for prebuilt schema


Custom table example:

Table: Customers

Columns:

customer_id (pk)

name (name)

email (email)

signup_date (date)

Convert CSV to Parquet:

convertfile ./fake_data/Customers.csv -o ./fake_data/Customers.parquet

Dependencies

Python >= 3.8

Faker

Typer

pandas

pyarrow
 (for Parquet support)

python-dotenv (optional for future env configs)

Project Structure
FakeDataForge/
├─ fake_data_generator/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ schema.py
│  ├─ generator.py
│  ├─ prompts.py
│  ├─ prebuilt.py
│  └─ custom.py
├─ file_converter/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ reader.py
│  └─ writer.py
├─ pyproject.toml
├─ README.md
└─ setup.cfg (optional)

License

MIT License © Sapna Singh Khatik