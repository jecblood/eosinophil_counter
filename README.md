# Biomedical Image Segmentation and Quantification Pipeline


A reproducible Python workflow for preprocessing microscopy images, segmenting objects/features, extracting region-level measurements, and exporting quantitative results for downstream analysis.

This pipeline was originally developed to identify and quantify eosinophils in colorectal tissue stained with hematoxylin and eosin (H&E). Example images used during development were obtained from open-access resources associated with The Cancer Genome Atlas (TCGA). Raw TCGA image files are not included in this repository. Users who wish to reproduce the workflow with TCGA data should download images directly from the official data repository and follow the applicable data access, usage, attribution, and citation requirements.

TCGA/GDC access information:  
https://www.cancer.gov/ccg/access-data

##Dependencies

`numpy`, `scikit-image`, `scipy`, `matplotlib`, and `pandas`.

## Core functions

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
3. Extract a selected color channel. (Red for eosinophils)
4. Apply median filtering to reduce noise.
5. Apply gamma correction for contrast adjustment.
6. Generate a binary foreground mask using thresholding.
7. Segment objects/features using watershed segmentation.
8. Extract region-level measurements with `skimage.measure.regionprops_table`.
9. Export measurements to a tab-delimited CSV file.
10. Save visual summary figures.


## License

MIT License. See `LICENSE` for details.


## Acknowledgments

This project was adapted from the SciPy 2018 tutorial "Image Analysis in Python with SciPy and scikit-image", presented by Stéfan van der Walt, Juan Nunez-Iglesias, and Joshua Warner. The workflow has been reorganized and adapted into a modular biomedical image segmentation pipeline with command-line execution, documentation, and quantitative measurement export.

Tutorial reference:  
van der Walt, S., Nunez-Iglesias, J., & Warner, J. (2018). Image Analysis in Python with SciPy and scikit-image. SciPy 2018 Tutorial. https://www.youtube.com/watch?v=pZATswy_IsQ

scikit-image citation:  
van der Walt, S., Schönberger, J. L., Nunez-Iglesias, J., Boulogne, F., Warner, J. D., Yager, N., Gouillart, E., Yu, T., & the scikit-image contributors. (2014). *scikit-image: Image processing in Python*. PeerJ, 2, e453. https://doi.org/10.7717/peerj.453

