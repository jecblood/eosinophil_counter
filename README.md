# Biomedical Image Segmentation and Quantification Pipeline

A reproducible Python workflow for preprocessing microscopy-style images, segmenting objects/features, extracting region-level measurements, and exporting quantitative results for downstream analysis.

This project demonstrates practical biomedical image analysis and scientific computing skills using `numpy`, `scikit-image`, `scipy`, `matplotlib`, and `pandas`.

## Why this project matters

This repository demonstrates an end-to-end analytical workflow relevant to data science, biomedical image analysis, and scientific computing portfolios:

- Load and crop image data
- Extract color channels
- Denoise images using median filtering
- Apply gamma correction and thresholding
- Perform watershed-based segmentation
- Extract quantitative region properties
- Export measurements to CSV
- Generate reproducible visual summaries

## Repository structure

```text
biomedical-image-segmentation-pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── preprocess.py
│   ├── segment.py
│   ├── quantify.py
│   ├── visualize.py
│   └── run_pipeline.py
├── notebooks/
│   └── image_segmentation_workflow.ipynb
├── data/
│   └── .gitkeep
├── outputs/
│   └── .gitkeep
└── figures/
    └── .gitkeep
```

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/biomedical-image-segmentation-pipeline.git
cd biomedical-image-segmentation-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add an example image

Place an image file in the `data/` folder, for example:

```text
data/example_image.png
```

If the original image is unpublished, proprietary, patient-derived, or otherwise restricted, do **not** upload the raw image to GitHub. Instead, use a public example image or a synthetic/mock image for demonstration.

### 5. Run the pipeline

```bash
python src/run_pipeline.py --image data/example_image.png --output outputs/region_measurements.csv
```

Optional crop coordinates can be provided:

```bash
python src/run_pipeline.py \
  --image data/example_image.png \
  --output outputs/region_measurements.csv \
  --crop 580 4100 1900 5500
```

The crop format is:

```text
row_start row_end col_start col_end
```

## Workflow overview

1. Load an input image.
2. Optionally crop the region of interest.
3. Extract a selected color channel.
4. Apply median filtering to reduce noise.
5. Apply gamma correction for contrast adjustment.
6. Generate a binary foreground mask using thresholding.
7. Segment objects/features using watershed segmentation.
8. Extract region-level measurements with `skimage.measure.regionprops_table`.
9. Export measurements to a tab-delimited CSV file.
10. Save visual summary figures.

## Example resume bullet

> Developed a Python-based biomedical image segmentation pipeline using scikit-image, NumPy, SciPy, Matplotlib, and Pandas to preprocess image data, perform watershed segmentation, extract region-level features, and export reproducible quantitative measurement tables for downstream analysis.

## Skills demonstrated

- Python programming
- Biomedical image analysis
- Computer vision preprocessing
- Watershed segmentation
- Feature extraction
- Data export and reproducible workflows
- Scientific visualization

## Notes for hiring managers

This project shows how exploratory scientific code can be converted into a maintainable, reproducible analysis pipeline with clear documentation, modular functions, and command-line execution.

## License

MIT License. See `LICENSE` for details.
