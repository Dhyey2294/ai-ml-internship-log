import numpy as np
from tensorflow.keras.models import load_model

from preprocessing import load_and_prepare_data

(
    X_train_scaled,
    X_val_scaled,
    y_reg_train_log,
    y_reg_val_log,
    y_cls_train,
    y_cls_val,
    scaler,
    class_map,
    X_val,
    y_reg_val,
) = load_and_prepare_data()

model = load_model("house_price_multitask.keras")

price_log_pred, class_pred = model.predict(X_val_scaled)

price_pred = np.expm1(price_log_pred).flatten()
price_true = y_reg_val.values

real_mae = np.mean(np.abs(price_pred - price_true))
real_rmse = np.sqrt(np.mean((price_pred - price_true)**2))
real_mape = np.mean(np.abs((price_true - price_pred) / price_true)) * 100

print("\nFINAL REGRESSION METRICS")
print("MAE:", int(real_mae))
print("RMSE:", int(real_rmse))
print(f"MAPE: {real_mape:.2f}%")

class_pred_labels = np.argmax(class_pred, axis=1)
class_accuracy = np.mean(class_pred_labels == y_cls_val)

print(f"\nClassification Accuracy: {class_accuracy*100:.2f}%")
