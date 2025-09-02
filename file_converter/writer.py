# file_converter/writer.py
from pathlib import Path
import pandas as pd

SUPPORTED_FORMATS = ["csv", "parquet", "xlsx", "xls"]

def write_file(file_path: Path, df: pd.DataFrame, fmt: str = None):
    """
    Write a pandas DataFrame to a file.
    
    Args:
        file_path: Output file path (Path or str).
        df: pandas DataFrame to write.
        fmt: Optional; output format. If None, inferred from file_path suffix.
    
    Supported formats: CSV, Parquet, XLSX, XLS
    """
    file_path = Path(file_path)
    fmt = fmt.lower() if fmt else file_path.suffix.lower().replace(".", "")

    if fmt not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported output format: {fmt}. Supported: {SUPPORTED_FORMATS}")

    if fmt == "csv":
        df.to_csv(file_path, index=False)
    elif fmt == "parquet":
        df.to_parquet(file_path, engine="pyarrow", index=False)
    elif fmt in ["xlsx", "xls"]:
        df.to_excel(file_path, index=False)
