import pandas as pd

# Load dataset
df = pd.read_excel("merged all.xlsx")

# Selected important nutrients
selected_features = [
    'energy_kcal',
    'protein_g',
    'fat_g',
    'carbohydrate_g',
    'saturated_fat_g',
    'sugars_g',
    'fiber_g',
    'sodium_mg',
    'cholesterol_mg'
]

df_ml = df[selected_features].copy()

# Fill missing values
df_ml = df_ml.fillna(0)

# Save cleaned base file
df_ml.to_csv("nutrition_base.csv", index=False)

print("Data preparation completed.")
