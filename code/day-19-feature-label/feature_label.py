import pandas as pd

df = pd.read_csv("nutrition_base.csv")

df['energy_kcal'] = df['energy_kcal'].replace(0, 1)

df['protein_ratio'] = df['protein_g'] / df['energy_kcal']
df['fat_ratio'] = df['fat_g'] / df['energy_kcal']
df['sugar_ratio'] = df['sugars_g'] / df['energy_kcal']
df['fiber_ratio'] = df['fiber_g'] / df['energy_kcal']
df['sodium_density'] = df['sodium_mg'] / df['energy_kcal']


# Rule-based labeling
def assign_health_risk(row):

    if row['sugars_g'] > 15 and row['saturated_fat_g'] > 5:
        return 3

    elif row['fat_g'] > 20 or row['sodium_mg'] > 600:
        return 2

    elif row['fiber_g'] > 5 and row['protein_ratio'] > 0.08:
        return 0

    else:
        return 1


df['health_risk_label'] = df.apply(assign_health_risk, axis=1)

df.to_csv("nutrition_labeled.csv", index=False)

print("Feature engineering and labeling completed.")
