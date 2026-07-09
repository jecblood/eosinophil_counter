"""Image loading and preprocessing utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple

import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage as ndi
from skimage import exposure, util

Crop = Tuple[int, int, int, int]


def load_image(image_path: str | Path) -> np.ndarray:
    """Load an image from disk."""
    image_path = Path(image_path)
    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    return mpimg.imread(image_path)


def crop_image(image: np.ndarray, crop: Optional[Crop] = None) -> np.ndarray:
    """Crop an image using row/column coordinates.

    Crop format: (row_start, row_end, col_start, col_end).
    If ``crop`` is None, the original image is returned.
    """
    if crop is None:
        return image
    row_start, row_end, col_start, col_end = crop
    return image[row_start:row_end, col_start:col_end, ...]


def extract_channel(image: np.ndarray, channel: int = 0) -> np.ndarray:
    """Extract a single color channel from an RGB/RGBA image.

    If an image is already 2D, it is returned unchanged.
    """
    if image.ndim == 2:
        return image
    if channel < 0 or channel >= image.shape[-1]:
        raise ValueError(f"Channel {channel} is outside image shape {image.shape}")
    return image[..., channel]


def denoise_median(channel_image: np.ndarray, size: int = 2) -> np.ndarray:
    """Apply a median filter to reduce image noise."""
    return ndi.median_filter(util.img_as_float(channel_image), size=size)


def apply_gamma(image: np.ndarray, gamma: float = 5.0) -> np.ndarray:
    """Apply gamma correction to adjust image contrast."""
    return exposure.adjust_gamma(image, gamma)


def threshold_image(image: np.ndarray, threshold: float = 0.65, invert: bool = True) -> np.ndarray:
    """Create a binary foreground mask from an image."""
    if invert:
        return image <= threshold
    return image >= threshold
