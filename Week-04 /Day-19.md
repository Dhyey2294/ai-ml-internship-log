# Day 19 – 10 Feb 2026
## 🔵 Feature Engineering & Ground Truth Creation

## 🎯 Objective
To enhance raw nutrition values using density-based
metrics and generate health risk labels.

## 🔹 Work Done
- Created derived features:
  - Protein per calorie
  - Fat per calorie
  - Sugar per calorie
  - Fiber per calorie
  - Sodium per calorie

- Observed that foods with equal calories
  can differ drastically in nutritional quality.

- Built rule-based logic to simulate expert judgement.

Risk levels:
0 → Healthy  
1 → Moderate  
2 → Unhealthy  
3 → High Risk  

Example:
High sugar + high saturated fat → High Risk.

## ✅ Outcome
- Generated supervised labels without manual annotation.
- Prepared final dataset for ML training.

## 🧠 Learnings
Rule-based labeling is practical for MVP systems
when expert annotations are unavailable.

## 🔹 Code & Implementation
- Feature engineering & labeling:  
  [feature_label.py](../code/day-19-feature-label/feature_label.py)
