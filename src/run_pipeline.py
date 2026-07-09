"""Command-line entry point for the segmentation pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path

from config import DEFAULT_CHANNEL, DEFAULT_GAMMA, DEFAULT_MEDIAN_FILTER_SIZE, DEFAULT_THRESHOLD
from preprocess import apply_gamma, crop_image, denoise_median, extract_channel, load_image, threshold_image
from quantify import region_properties_to_dataframe, save_measurements
from segment import watershed_segmentation
from visualize import plot_area_histogram, plot_channels, plot_segmentation_overlay


def parse_args():
    parser = argparse.ArgumentParser(description="Biomedical image segmentation and quantification pipeline")
    parser.add_argument("--image", required=True, help="Path to input image")
    parser.add_argument("--output", default="outputs/region_measurements.csv", help="Path to output measurements file")
    parser.add_argument("--crop", nargs=4, type=int, metavar=("ROW_START", "ROW_END", "COL_START", "COL_END"), help="Optional crop coordinates")
    parser.add_argument("--channel", type=int, default=DEFAULT_CHANNEL, help="Color channel to analyze: 0=red, 1=green, 2=blue")
    parser.add_argument("--gamma", type=float, default=DEFAULT_GAMMA, help="Gamma correction value")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help="Threshold for foreground mask")
    parser.add_argument("--median-size", type=int, default=DEFAULT_MEDIAN_FILTER_SIZE, help="Median filter size")
    return parser.parse_args()


def main():
    args = parse_args()
    output_path = Path(args.output)
    figures_dir = Path("figures")
    figures_dir.mkdir(exist_ok=True)

    image = load_image(args.image)
    image = crop_image(image, tuple(args.crop) if args.crop else None)

    if image.ndim == 3 and image.shape[-1] >= 3:
        plot_channels(image, figures_dir / "rgb_channels.png")

    channel_img = extract_channel(image, channel=args.channel)
    denoised = denoise_median(channel_img, size=args.median_size)
    gamma_corrected = apply_gamma(denoised, gamma=args.gamma)
    binary_mask = threshold_image(gamma_corrected, threshold=args.threshold, invert=True)

    labels = watershed_segmentation(binary_mask)
    df = region_properties_to_dataframe(labels, intensity_image=channel_img)
    save_measurements(df, output_path)

    plot_segmentation_overlay(channel_img, labels, figures_dir / "segmentation_overlay.png")
    plot_area_histogram(df, figures_dir / "area_histogram.png")

    print(f"Saved measurements to: {output_path}")
    print(f"Number of segmented regions: {len(df)}")
    print("Saved figures to: figures/")


if __name__ == "__main__":
    main()
