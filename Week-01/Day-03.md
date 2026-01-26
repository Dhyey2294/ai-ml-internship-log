# Day 03 – 21 Jan 2026

## 🔹 Focus
Face-specific embeddings, model export for Flutter/iOS, and debugging deployment issues.

## 🔹 What I Worked On
- Identified limitations of generic image embeddings for face similarity
- Researched and evaluated face-specific embedding models (e.g., MobileFaceNet)
- Switched to the LFW (Labeled Faces in the Wild) dataset for face-based evaluation
- Organized dataset structure for face detection and embedding workflows
- Explored face detection + face embedding pipeline

## 🔹 Model Export & Deployment
- Exported face embedding model to TensorFlow Lite (.tflite) format
- Verified TFLite model by checking input/output tensor shapes
- Tested inference using the TFLite interpreter
- Shared the final `.tflite` model with the Flutter team

## 🔹 Debugging & Environment Management
- Resolved NumPy ↔ TensorFlow compatibility issues
- Set up isolated virtual environments
- Fixed model loading and path resolution errors

## 🔹 Tools / Tech Used
- TensorFlow / Keras
- TensorFlow Lite
- Python
- MobileFaceNet
- LFW dataset

## 🔹 Outcome
- Delivered a working face embedding TFLite model
- Understood the importance of face-specific embeddings for accurate similarity grouping
- Gained hands-on experience with ML deployment, debugging, and cross-team collaboration

## 🔹 Code & Implementation
- TFLite export script:  
  [export_tflite.py](../code/code/day-03-face-embeddings/export_tflite.py)
- TFLite inference validation:  
  [test_tflite.py](../code/code/day-03-face-embeddings/test_tflite.py)
- Final face embedding model:  
  [mobilefacenet.tflite](../code/code/day-03-face-embeddings/mobilefacenet.tflite)




