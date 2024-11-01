"""Utility module for loading Coursera course data.

This module provides functions to load and manage Coursera course data
from CSV files, ensuring compatibility across different operating systems
and project structures.
"""

import os
from pathlib import Path
from typing import Optional, Union

import pandas as pd


def load_coursera_data(
    dataset_file_path: Union[str, Path] = Path("data") / "coursera_data.csv",
    encoding: Optional[str] = None
) -> pd.DataFrame:
    """Load Coursera data from a CSV file.

    Reads a CSV file containing Coursera data and returns it as a pandas
    DataFrame. Utilizes pathlib.Path for cross-platform compatibility.

    Project structure:
        coursera-courses-eda/
        ├── data/
        │   └── coursera_data.csv
        ├── notebooks/
        └── src/
            └── coursera_courses_eda/
                └── utils.py

    Args:
        dataset_file_path: Path to the CSV file. Defaults to
            'data/coursera_data.csv' in the project root. Accepts both
            string and Path inputs with forward or backward slashes.
        encoding: Optional; the encoding to use for reading the file.
            If None, the system default encoding is used.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded Coursera data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: Propagates any exception encountered during file reading,
            augmented with additional system information.

    Examples:
        Load data using default path:
            df = load_coursera_data()

        Load data with a specific path:
            df = load_coursera_data("data/coursera_data.csv")

        Load data using Path object:
            df = load_coursera_data(Path("data") / "coursera_data.csv")
    """
    try:
        path = Path(dataset_file_path)
        current_dir = Path.cwd()

        if current_dir.name == 'notebooks':
            project_root = current_dir.parent
        else:
            project_root = current_dir

        if not path.is_absolute():
            path = project_root / path

        path = path.resolve()

        if not path.is_file():
            raise FileNotFoundError(
                f"Dataset file not found at: {path}\n"
                f"Current directory: {current_dir}\n"
                f"Project root: {project_root}\n"
                f"Operating system: {os.name}\n"
                "Ensure you're running from the project root or notebooks directory."
            )

        return pd.read_csv(path, encoding=encoding)

    except Exception as error:
        raise type(error)(
            f"{error}\n"
            f"Operating system: {os.name}\n"
            f"Current directory: {Path.cwd()}\n"
            f"Attempted path: {path}"
        ) from error
