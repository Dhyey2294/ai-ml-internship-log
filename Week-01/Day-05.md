# Day 05 – 23 Jan 2026
## 🟣 Car Purchase Amount Prediction using ANN

## 🎯 Objective
To understand the regression problem and build a complete data preprocessing
pipeline for predicting car purchase amount using customer data.

## 🔹 Work Done

### 1️⃣ Data Loading & Exploration
- Loaded dataset using Pandas.
- Inspected dataset structure using `head()`, `shape`, and `info()`.
- Checked for duplicate records and verified column data types.
- Identified target variable: car purchase amount.

### 2️⃣ Data Cleaning
- Removed irrelevant and non-numeric columns:
  - Customer name
  - Customer email
  - Country
- Retained only meaningful numerical features for model training.

### 3️⃣ Feature & Target Separation
- Defined feature set (X):
  - Gender
  - Age
  - Annual Salary
  - Credit Card Debt
  - Net Worth
- Defined target variable (y):
  - Car Purchase Amount

### 4️⃣ Train-Test Split
- Split dataset into training and testing sets using `train_test_split`.
- Configuration:
  - Test size: 20%
  - Random state: 42 (for reproducibility)

### 5️⃣ Feature Scaling
- Applied `StandardScaler`:
  - `scaler_X` for input features
  - `scaler_y` for target variable
- Used `fit_transform()` only on training data.
- Used `transform()` on test data to prevent data leakage.

## 🧠 Learnings
Proper data cleaning and feature scaling are critical for achieving
stable and accurate ANN regression performance.

## 🔹 Code & Implementation
- Data preprocessing and scaling:  
  [preprocess_data.py](../code/day-05-ann-preprocessing/preprocess_data.py)

