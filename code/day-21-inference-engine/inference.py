import pandas as pd
import joblib

rf_model = joblib.load("nutrition_rf_model.pkl")

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


def explain_health_risk(nutrition_dict):
    reasons = []

    if nutrition_dict['sugars_g'] > 15:
        reasons.append("High sugar content")
    if nutrition_dict['saturated_fat_g'] > 5:
        reasons.append("High saturated fat")
    if nutrition_dict['sodium_mg'] > 600:
        reasons.append("High sodium level")
    if nutrition_dict['fiber_g'] > 5:
        reasons.append("Good fiber content")
    if nutrition_dict['protein_g'] > 20:
        reasons.append("Good protein amount")

    if not reasons:
        reasons.append("Within normal nutritional ranges")

    return reasons


def recommend_food(food_row, health_risk_label, goal="general_health"):

    if health_risk_label == 3:
        return {
            "goal": goal,
            "recommendation": "Not Recommended",
            "reason": ["High health risk food"]
        }

    return {
        "goal": goal,
        "recommendation": "Recommended"
    }


def analyze_food(nutrition_dict, goal="general_health"):

    food_df = pd.DataFrame([nutrition_dict])
    kcal = max(food_df.loc[0, 'energy_kcal'], 1)

    food_df['protein_ratio'] = food_df['protein_g'] / kcal
    food_df['fat_ratio'] = food_df['fat_g'] / kcal
    food_df['sugar_ratio'] = food_df['sugars_g'] / kcal
    food_df['fiber_ratio'] = food_df['fiber_g'] / kcal
    food_df['sodium_density'] = food_df['sodium_mg'] / kcal

    model_input = food_df[features]

    pred = rf_model.predict(model_input)[0]
    prob = max(rf_model.predict_proba(model_input)[0])

    labels = ["Healthy", "Moderate", "Unhealthy", "High Risk"]

    return {
        "health_risk": {
            "category": labels[pred],
            "confidence": round(float(prob), 2)
        },
        "why_this_prediction": explain_health_risk(nutrition_dict),
        "personalized_advice": recommend_food(food_df.iloc[0], pred, goal)
    }
