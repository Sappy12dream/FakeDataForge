from pathlib import Path
import pandas as pd

SUPPORTED_FORMATS = ["csv", "parquet", "xlsx", "xls"]

def read_file(file_path: Path) -> pd.DataFrame:
    ext = file_path.suffix.lower().replace(".", "")
    if ext not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {ext}")
    if ext == "csv":
        return pd.read_csv(file_path)
    elif ext == "parquet":
        return pd.read_parquet(file_path)
    else:
        return pd.read_excel(file_path)
