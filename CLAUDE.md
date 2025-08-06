# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a collection of Jupyter notebooks focused on computer vision, image analysis, and data visualization for wildlife/animal research. The notebooks demonstrate various machine learning techniques including object detection, image classification, synthetic image generation, and data visualization using popular libraries like YOLOv5, ResNet50, Stable Diffusion, and matplotlib.

## Repository Structure

```
jupyter-notebooks/
├── Borealis_connection_test.ipynb          # Data downloading from Borealis repository
├── Create Synthetic Images/
│   ├── prompt-generator.ipynb              # Text prompt generation for synthetic images
│   └── stable-diffusion.ipynb              # Stable Diffusion image generation
├── Explore Large Image Datasets/
│   ├── image-filter.ipynb                  # Image filtering and processing
│   └── random-manual-review.ipynb          # Manual review tools for datasets
├── Object Classification and Localization/
│   ├── GEMINI.md                           # Documentation for classification notebooks
│   ├── bounding-boxes-coco-weights.ipynb   # COCO pre-trained model for object detection
│   ├── data-prep-fine-tuning.ipynb         # Data preparation for model fine-tuning
│   ├── dataset-sizes-classification-report.ipynb  # Performance analysis by dataset size
│   ├── dataset-sizes-confusion-matrix.ipynb       # Confusion matrices for different dataset sizes
│   ├── resnet50-bounding-boxes.ipynb       # ResNet50-based object detection
│   └── yolov5-localization-feature.ipynb   # YOLOv5 object localization implementation
└── Visualize Image Information/
    ├── 100-image-grid.ipynb                # Grid-based image visualization
    ├── close-encounters-network.ipynb      # Network visualization of image relationships
    ├── matplotlib-visualization.ipynb      # Standard matplotlib plotting for structured data
    ├── photo-select-tool.ipynb             # Interactive photo selection interface
    ├── random-interactive-image.ipynb      # Random image display with interactivity
    ├── sightings-bar-graph.ipynb          # Bar graph generation for sighting data
    └── tree-map.ipynb                     # Tree map visualization
```

## Common Development Tasks

### Running Notebooks
- All notebooks are designed to run in Google Colab environment
- Each notebook includes a Colab badge link for direct access
- Notebooks mount Google Drive for data access using `from google.colab import drive`

### Key Dependencies
Notebooks typically require these libraries (installed via pip within the notebooks):
- `torch`, `torchvision`, `torchaudio` - PyTorch ecosystem for deep learning
- `ultralytics` - YOLOv5/YOLOv8 implementation
- `tensorflow` - TensorFlow for ML operations
- `fiftyone` - Computer vision dataset management
- `pandas`, `numpy` - Data manipulation
- `matplotlib`, `plotly` - Data visualization
- `PIL` (Pillow) - Image processing
- `openpyxl` - Excel file handling

### Data Sources
- **Borealis Data Repository**: Public datasets accessed via API (no authentication required)
- **Google Drive**: Mounted storage for datasets and outputs
- **FiftyOne Zoo**: Pre-built computer vision datasets
- **Hugging Face**: Model repositories for Stable Diffusion

## Architecture Notes

### Computer Vision Pipeline
1. **Data Acquisition**: Notebooks use Borealis API or FiftyOne zoo datasets
2. **Preprocessing**: Image filtering, resizing, and augmentation
3. **Model Loading**: Pre-trained models (YOLOv5, ResNet50, Stable Diffusion)
4. **Inference**: Object detection, classification, or generation
5. **Visualization**: Annotated images, plots, and interactive displays

### Notebook Patterns
- **Google Drive Integration**: All notebooks mount `/content/drive` for file access
- **Error Handling**: Try-catch blocks for file operations and model loading
- **Modular Functions**: Reusable functions for image processing and visualization
- **Path Management**: Configurable input/output directory variables
- **Progress Tracking**: Print statements for processing status

### Model Integration
- **YOLOv5**: Object detection with bounding box annotations
- **ResNet50**: Feature extraction and classification
- **Stable Diffusion**: Text-to-image generation
- **COCO Pre-trained**: Transfer learning for object detection

## Data Flow
1. Datasets downloaded from Borealis or loaded from FiftyOne
2. Images processed and filtered based on requirements
3. Models applied for detection, classification, or generation
4. Results visualized and saved to Google Drive
5. Interactive tools provided for manual review and analysis