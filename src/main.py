"""Main entry point for the scRNA/scATAC integration workflow."""

from pathlib import Path


def main() -> None:
    """Replace this with your analysis pipeline entry point."""
    project_root = Path(__file__).resolve().parent.parent
    data_dir = project_root / "data"

    print(f"Project root: {project_root}")
    print(f"Data directory: {data_dir}")
    print("Ready to build your workflow.")


if __name__ == "__main__":
    main()
