import pandas as pd
import joblib
import tensorflow as tf

# Load model and scalers
model = tf.keras.models.load_model("car_price_ann_model.keras")
scaler_X = joblib.load("scaler_X.pkl")
scaler_y = joblib.load("scaler_y.pkl")

# New customer data
new_customer = {
    "gender": 1,
    "age": 45,
    "annual Salary": 60000,
    "credit card debt": 8000,
    "net worth": 300000
}

new_customer_df = pd.DataFrame([new_customer])

# Scale and predict
new_customer_scaled = scaler_X.transform(new_customer_df)
pred_scaled = model.predict(new_customer_scaled)
pred_real = scaler_y.inverse_transform(pred_scaled)

print(
    "Predicted car purchase amount:",
    round(float(pred_real[0][0]), 2)
)
