"""Preprocessing utilities for RNA and ATAC data."""

from __future__ import annotations

from pathlib import Path


def make_directory(path: str | Path) -> Path:
    """Create a directory and return its path."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def summarize_dataset(adata, name: str) -> None:
    """Print a quick summary for a dataset."""
    print(f"{name}: cells={adata.n_obs}, genes/features={adata.n_vars}")
