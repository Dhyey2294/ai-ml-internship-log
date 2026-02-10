import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

df = pd.read_csv("nutrition_labeled.csv")

features = [
    'energy_kcal',
    'saturated_fat_g',
    'sugars_g',
    'fiber_g',
    'sodium_mg',
    'cholesterol_mg',
    'protein_ratio',
    'fat_ratio',
    'sugar_ratio',
    'fiber_ratio',
    'sodium_density'
]

X = df[features]
y = df['health_risk_label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight='balanced',
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

# Evaluation
y_pred = rf_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model
joblib.dump(rf_model, "nutrition_rf_model.pkl")

print("Model training completed.")
