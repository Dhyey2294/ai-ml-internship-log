# Day 18 – 09 Feb 2026
## 🟢 Nutrition Intelligence – Dataset Setup & Preparation

## 🎯 Objective
To prepare a structured nutrition dataset that can be used
for machine learning based health risk prediction.

## 🔹 Work Done
- Loaded merged nutritional database (~12,706 foods).
- Reviewed available macronutrients:
  energy, protein, fat, carbohydrates,
  saturated fat, sugars, fiber, sodium, cholesterol.

- Selected nutrients most relevant to health impact.
- Replaced missing values with zero to maintain
  a consistent numeric feature space.
- Generated a clean ML-ready dataset.

## ✅ Outcome
- Reliable and standardized dataset prepared.
- Ready for feature engineering and modeling.

## 🧠 Learnings
Data cleaning and consistency are critical for building
stable health intelligence systems.

## 🔹 Code & Implementation
- Dataset preprocessing:  
  [data_prep.py](../code/day-18-data-prep/data_prep.py)
