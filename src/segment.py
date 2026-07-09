"""Segmentation utilities."""

from __future__ import annotations

import numpy as np
from scipy import ndimage as ndi
from skimage import morphology, segmentation


def compute_distance_map(binary_mask: np.ndarray) -> np.ndarray:
    """Compute distance from each foreground pixel to the background."""
    return ndi.distance_transform_edt(binary_mask)


def find_local_maxima(distance_map: np.ndarray) -> np.ndarray:
    """Identify local maxima in a distance map."""
    return morphology.local_maxima(distance_map)


def watershed_segmentation(binary_mask: np.ndarray) -> np.ndarray:
    """Segment foreground objects using local maxima and watershed."""
    distance = compute_distance_map(binary_mask)
    local_maxima = find_local_maxima(distance)
    markers = ndi.label(local_maxima)[0]
    labels = segmentation.watershed(-distance, markers, mask=binary_mask)
    return labels


def shuffle_labels(labels: np.ndarray, random_state: int = 42) -> np.ndarray:
    """Randomize label colors for easier visualization."""
    rng = np.random.default_rng(random_state)
    indices = np.unique(labels[labels != 0])
    indices = np.append([0], rng.permutation(indices))
    return indices[labels]
