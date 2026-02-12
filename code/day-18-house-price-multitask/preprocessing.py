import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


def load_and_prepare_data(path="train.csv"):
    df = pd.read_csv(path)

    y_price = df["SalePrice"]
    X = df.drop(columns=["SalePrice", "Id"])

    # Missing values
    numeric_features = X.select_dtypes(include=[np.number]).columns
    categorical_features = X.select_dtypes(include=["object"]).columns

    imputer = SimpleImputer(strategy="median")
    X[numeric_features] = imputer.fit_transform(X[numeric_features])

    for col in categorical_features:
        X[col] = X[col].fillna("Missing")

    # One hot encoding
    X = pd.get_dummies(X, drop_first=True)

    # Classification labels
    y_class = pd.qcut(y_price, q=3, labels=[0, 1, 2]).astype(int)

    class_map = {
        0: "Low Price",
        1: "Medium Price",
        2: "High Price"
    }

    X_train, X_val, y_reg_train, y_reg_val, y_cls_train, y_cls_val = train_test_split(
        X, y_price, y_class,
        test_size=0.2,
        random_state=42,
        stratify=y_class
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)

    y_reg_train_log = np.log1p(y_reg_train)
    y_reg_val_log = np.log1p(y_reg_val)

    return (
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
    )
