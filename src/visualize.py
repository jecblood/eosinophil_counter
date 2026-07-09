"""Visualization utilities for image segmentation workflows."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from skimage import measure


def show_image(image: np.ndarray, title: Optional[str] = None, cmap: str = "gray", figsize=(8, 8)):
    """Display an image with axes hidden."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(image, cmap=cmap)
    ax.axis("off")
    if title:
        ax.set_title(title)
    return fig, ax


def plot_channels(image: np.ndarray, output_path: Optional[str | Path] = None):
    """Plot RGB channels separately."""
    if image.ndim < 3 or image.shape[-1] < 3:
        raise ValueError("plot_channels expects an RGB or RGBA image")
    titles = ["Red channel", "Green channel", "Blue channel"]
    fig, axes = plt.subplots(1, 4, figsize=(16, 5))
    for ax in axes:
        ax.axis("off")
    for i in range(3):
        axes[i].imshow(image[..., i], cmap="gray")
        axes[i].set_title(titles[i])
    axes[3].imshow(image[..., :3])
    axes[3].set_title("RGB image")
    if output_path:
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
    return fig, axes


def plot_segmentation_overlay(image: np.ndarray, labels: np.ndarray, output_path: Optional[str | Path] = None):
    """Overlay segmentation contours on an image."""
    contours = measure.find_contours(labels, level=0.5)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(image, cmap="gray")
    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=1)
    ax.axis("off")
    ax.set_title("Segmentation overlay")
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
    return fig, ax


def plot_area_histogram(df, output_path: Optional[str | Path] = None):
    """Plot a histogram of segmented object areas."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df["area"], bins=100)
    ax.set_xlabel("Area (pixels)")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of segmented object areas")
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
    return fig, ax
