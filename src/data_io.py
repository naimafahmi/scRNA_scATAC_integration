"""Helpers for loading and saving data objects."""

from __future__ import annotations

from pathlib import Path

import anndata as ad


def load_h5ad(path: str | Path):
    """Load an AnnData object from disk."""
    return ad.read_h5ad(path)


def save_h5ad(adata, path: str | Path) -> None:
    """Save an AnnData object to disk."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    adata.write_h5ad(path)
