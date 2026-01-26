# Day 02 – 20 Jan 2026

## 🔹 Focus
Image embedding model selection, local inference benchmarking, and deployment feasibility for an iOS storage cleaner application.

## 🔹 What I Worked On
- Analyzed requirements for on-device image processing:
  - Local execution without cloud dependency
  - Fast inference time for large image collections
  - Compatibility with Flutter and iOS platforms
- Selected a MobileNet-based architecture for lightweight and efficient image embeddings
- Set up a large-scale dataset (~5000 images) to simulate real-world usage
- Implemented image preprocessing steps including resizing and normalization
- Built an embedding model by removing the classification head and extracting feature vectors

## 🔹 Experiments & Benchmarking
- Performed CPU-based inference benchmarking
- Measured total inference time and calculated average time per image
- Observed approximately 90 ms per image during naive inference
- Compared performance across different batch sizes (5000 images vs 1000 images)
- Noted performance improvements when reducing batch size and optimizing execution

## 🔹 Tools / Tech Used
- Python
- TensorFlow / Keras
- OpenCV
- MobileNet architecture

## 🔹 Challenges Faced
- Balancing embedding quality with inference speed
- Identifying preprocessing and model initialization as performance bottlenecks
- Managing inference time for large image collections

## 🔹 Outcome
- Confirmed that MobileNet-based image embeddings are suitable for on-device execution
- Identified preprocessing and model loading as key factors affecting latency
- Gained clarity on expected inference time for mobile deployment

## 🔹 Code & Implementation
- Image embedding extraction and inference:  
  [image_embedding.py](../code/day-02-image-embeddings/image_embedding.py)
- Performance benchmarking script:  
  [benchmark.py](../code/day-02-image-embeddings/benchmark.py)



