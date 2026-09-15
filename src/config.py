from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

RNA_FILE = RAW_DATA_DIR / "rna_counts.h5ad"
ATAC_FILE = RAW_DATA_DIR / "atac_counts.h5ad"
