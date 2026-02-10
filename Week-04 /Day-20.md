# Day 20 – 11 Feb 2026
## 🟣 Random Forest Model Training & Evaluation

## 🎯 Objective
To train a machine learning classifier capable of
predicting the health risk level of foods.

## 🔹 Work Done
- Selected Random Forest classifier because:
  - Works well for tabular data
  - Handles nonlinear interactions
  - Robust to noise
  - Provides feature importance

- Used stratified 80/20 split.
- Applied balanced class weighting.
- Trained model with 200 trees.

- Evaluated using:
  accuracy, precision, recall, F1, confusion matrix.

## 📊 Performance
- Achieved ~99% accuracy.
- Excellent reliability across all categories.
- Strong identification of risky foods.

## ✅ Outcome
- High confidence model ready for inference.

## 🧠 Learnings
Good feature design often contributes more
than complex model architectures.

## 🔹 Code & Implementation
- Model training pipeline:  
  [train_rf.py](../code/day-20-model-training/train_rf.py)
