# Day 06 – 24 Jan 2026
## 🔵 ANN Model Training, Evaluation & Deployment

## 🎯 Objective
To build, train, evaluate, and prepare an ANN regression model
for real-world car purchase amount prediction.

## 🔹 Work Done

### 6️⃣ ANN Model Architecture (TensorFlow / Keras)
- Built a Sequential ANN model with:
  - Input layer: 64 neurons (ReLU)
  - Hidden layers: 32 and 16 neurons (ReLU)
  - Dropout layers (0.2) for regularization
  - Output layer: 1 neuron (regression output)
- Optimizer: Adam
- Loss function: Mean Squared Error (MSE)

### 7️⃣ Model Training with Optimization
- Used `EarlyStopping` callback:
  - Monitored validation loss
  - Patience: 15 epochs
  - Restored best model weights
- Trained model for up to 100 epochs.
- Prevented overfitting and unnecessary training.

### 8️⃣ Model Evaluation
- Generated predictions on test data.
- Inverse-transformed predictions to original scale.
- Evaluated model using:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² Score

### 📊 Final Performance
- R² Score ≈ 0.98
- Low MAE and RMSE indicating high prediction accuracy.

### 9️⃣ Real-World Prediction
- Created a new customer input using a dictionary.
- Converted input into a DataFrame to preserve feature order.
- Applied trained scalers and generated realistic predictions.

### 🔟 Training Visualization
- Plotted training vs validation loss.
- Verified:
  - Stable convergence
  - No overfitting
  - Correct early stopping behavior

### 1️⃣1️⃣ Model & Scaler Persistence
- Saved trained ANN model:
  - `car_price_ann_model.keras`
- Saved preprocessing objects:
  - `scaler_X.pkl`
  - `scaler_y.pkl`
- Ensured reproducibility and deployment readiness.

## 🧠 Learnings
- Feature scaling is essential for ANN regression stability.
- Early stopping significantly improves generalization.
- Saving models and scalers is crucial for real-world deployment.
