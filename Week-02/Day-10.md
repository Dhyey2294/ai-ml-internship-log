# Day 10 – 29 Jan 2026
## 🟣 Model Inference, Evaluation & Metrics

## 🎯 Objective
To evaluate model performance and analyze inference behavior on real-world images.

## 🔹 Work Done
- Performed inference using the trained YOLOv8 classification model.
- Tested the model on validation data and unseen external images.
- Analyzed prediction confidence and class rankings.
- Evaluated performance on visually similar food items.

## ✅ Final Metrics Summary
- **Top-1 Accuracy:** ~76%
- **Top-5 Accuracy:** ~92%
- **Training Loss:** Steadily decreased across epochs, indicating stable convergence
- **Inference Speed:** ~4–7 ms per image
- **Training Framework:** YOLOv8 (Ultralytics) with PyTorch backend

## 🧠 Learnings
Inference evaluation on unseen data is crucial for understanding
real-world model behavior and reliability.

## 🔹 Code & Implementation
- Inference script:  
  [predict_food.py](../code/day-10-food-inference/predict_food.py)
