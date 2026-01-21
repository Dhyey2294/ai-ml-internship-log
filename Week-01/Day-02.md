# Day 02 – 20 Jan 2026

## 🔹 Focus
Image embedding model selection, local inference benchmarking, and deployment feasibility for an iOS storage cleaner application.

## 🔹 What I Worked On
- Analyzed requirements for on-device image processing:
  - Local execution (no cloud dependency)
  - Fast inference time
  - Compatibility with Flutter and iOS
- Selected a MobileNet-based architecture for lightweight and fast image embeddings
- Set up a large-scale dataset (~5000 images) for realistic benchmarking
- Implemented image preprocessing pipeline (resize and normalization)
- Built an embedding model by removing the classification head and extracting feature vectors

## 🔹 Experiments & Benchmarking
- Benchmarked inference performance on CPU:
  - Measured total inference time
  - Calculated average inference time per image
- Observed ~90 ms per image for naive inference and improved timings with optimized runs
- Compared inference performance across different batch sizes (5000 vs 1000 images)

## 🔹 Tools / Tech Used
- Python
- TensorFlow / Keras
- OpenCV
- MobileNet architecture

## 🔹 Challenges Faced
- Balancing model accuracy with inference speed
- Identifying preprocessing and model loading bottlenecks

## 🔹 Outcome
- Confirmed MobileNet-based image embeddings are feasible for on-device execution
- Identified preprocessing and model initialization as key performance factors
- Gained clarity on expected inference latency for mobile deployment
