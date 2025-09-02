# file_converter/reader.py
from pathlib import Path
import pandas as pd

SUPPORTED_FORMATS = ["csv", "parquet", "xlsx", "xls"]

def read_file(file_path: Path) -> pd.DataFrame:
    """
    Read a file and return a pandas DataFrame.
    Supports CSV, Parquet, XLSX, XLS.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    ext = file_path.suffix.lower().replace(".", "")
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported input format: {ext}. Supported: {SUPPORTED_FORMATS}")

    if ext == "csv":
        return pd.read_csv(file_path)
    elif ext == "parquet":
        return pd.read_parquet(file_path)
    elif ext in ["xlsx", "xls"]:
        return pd.read_excel(file_path)
