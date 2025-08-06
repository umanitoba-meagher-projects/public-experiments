This directory contains Jupyter notebooks for object classification and localization tasks.

Here's a breakdown of the files:

*   **`bounding-boxes-coco-weights.ipynb`**: Demonstrates how to use a model pre-trained on the COCO dataset to predict bounding boxes for objects in images.
*   **`data-prep-fine-tuning.ipynb`**: Contains code for preparing image data for fine-tuning a custom object detection model. This includes steps like data augmentation and creating data loaders.
*   **`dataset-sizes-classification-report.ipynb`**: Analyzes the impact of dataset size on model performance. It generates a classification report with metrics like precision, recall, and F1-score for models trained on different sized datasets.
*   **`dataset-sizes-confusion-matrix.ipynb`**: Visualizes the performance of classification models trained on different dataset sizes by generating confusion matrices.
*   **`resnet50-bounding-boxes.ipynb`**: Implements an object detection model using the ResNet50 architecture to predict bounding boxes.
*   **`yolov5-localization-feature.ipynb`**: Shows how to use the YOLOv5 model for object localization, detecting objects in images and extracting their bounding box coordinates.