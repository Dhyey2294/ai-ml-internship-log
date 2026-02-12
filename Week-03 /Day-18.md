# Day 18 – 07 Feb 2026
## 🏠 Multi-Task House Price Prediction using Deep Learning

## 🎯 Objective
To build a unified neural network capable of simultaneously:
- Predicting the exact sale price of a house (regression)
- Categorizing the property into price segments (Low / Medium / High)

This simulates real-world real estate systems where both
numerical valuation and market positioning are required.

## 🔹 Work Done
- Loaded the House Prices dataset (1460 records, 79 features).
- Separated regression target → SalePrice.
- Removed identifier column.

### Data Preprocessing
- Numerical missing values → filled using median.
- Categorical missing values → replaced with "Missing".
- Applied one-hot encoding.
- Final feature space expanded to 260+ inputs.

### Target Engineering
- Created price categories using quantiles:
  0 → Low  
  1 → Medium  
  2 → High

### Train / Validation Strategy
- 80 / 20 split.
- Stratified by price category.
- Ensured fair distribution across segments.

### Feature Scaling
- Applied StandardScaler.

### Regression Stabilization
- Used log(1 + price) transformation
  to reduce skew and improve convergence.

---

## 🧠 Model Architecture
Built using TensorFlow / Keras Functional API.

Shared backbone:
Dense → BatchNorm → Dropout stacks

Two output heads:
- Regression → 1 neuron (price)
- Classification → Softmax (3 classes)

Regularization used:
✔ L2 weight decay  
✔ Dropout  
✔ Batch normalization  

---

## ⚙️ Training Strategy
Optimizer → Adam  

Loss:
- Regression → MSE
- Classification → Sparse categorical crossentropy

Loss weights:
- Price → 0.7
- Class → 0.3

Callbacks:
- Early stopping
- Learning rate reduction

---

## 📊 Final Performance (Latest Run)

### Regression
MAE ≈ $43K  
RMSE ≈ $104K  
MAPE ≈ 25%

### Classification
Accuracy ≈ 79%

The system correctly predicts price segments
for ~8 out of 10 houses.

---

## 🧪 Example Prediction
Predicted price and category closely matched
ground truth for randomly sampled validation houses,
demonstrating good practical usability.

---

## ✅ Outcome
- Successfully implemented multi-task learning.
- One shared model performs two business tasks.
- Pipeline is reproducible and deployment-ready.

---

## 🧠 Learnings
- Multi-output networks allow efficient feature sharing.
- Regression benefits from log transformation.
- Proper preprocessing is crucial for tabular deep learning.
- Balancing losses between tasks affects performance.

---

## 🔹 Code & Implementation
- Preprocessing pipeline:  
  [preprocessing.py](../code/day-18-house-price-multitask/preprocessing.py)

- Model architecture:  
  [model.py](../code/day-18-house-price-multitask/model.py)

- Training script:  
  [train.py](../code/day-18-house-price-multitask/train.py)

- Evaluation & metrics:  
  [evaluate.py](../code/day-18-house-price-multitask/evaluate.py)
