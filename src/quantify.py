"""Region measurement and export utilities."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from skimage import measure


def region_properties_to_dataframe(labels, intensity_image=None) -> pd.DataFrame:
    """Convert segmentation region properties to a pandas DataFrame."""
    properties = [
        "label",
        "area",
        "bbox",
        "centroid",
        "eccentricity",
        "equivalent_diameter_area",
        "extent",
        "major_axis_length",
        "minor_axis_length",
        "perimeter",
        "solidity",
    ]
    table = measure.regionprops_table(labels, intensity_image=intensity_image, properties=properties)
    return pd.DataFrame(table)


def save_measurements(df: pd.DataFrame, output_path: str | Path, sep: str = "\t") -> None:
    """Save measurements to a delimited text file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, sep=sep, index=False)
