from pathlib import Path

import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, RidgeCV
from sklearn.metrics import r2_score, mean_absolute_error

def build_and_train_model():
    global model, poly

    data_file = Path(__file__).resolve().parent / "House_Prices.csv"
    df = pd.read_csv(data_file)

    y = df["sales_price"]
    X = df[y_columns].copy()
    X["x2"] = X["x"] ** 1.5
    X["y2"] = X["y"] ** 1.5

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=42)

    best_mae = float("inf")
    best_degree = None

    for degree in (1, 2, 3):
        candidate_poly = PolynomialFeatures(degree=degree, include_bias=False)
        X_train_poly = candidate_poly.fit_transform(X_train)
        X_val_poly = candidate_poly.transform(X_val)

        candidate_model = LinearRegression()
        candidate_model.fit(X_train_poly, y_train)
        y_pred = candidate_model.predict(X_val_poly)

        mae = mean_absolute_error(y_val, y_pred)
        r2 = r2_score(y_val, y_pred)
        print(f"Grad {degree} | MAE: {mae:,.2f} | R²: {r2:.3f}")

        if mae < best_mae:
            best_mae = mae
            best_degree = degree
            model = candidate_model
            poly = candidate_poly

    print(f"Best av de tre: grad {best_degree} (MAE: {best_mae:,.2f})")
def predict_price(x, y, m2:int,house_type, standard) -> float:
    # Build a single sample
    x_house = pd.DataFrame([[x, y,m2,house_type,standard]],columns=y_columns)
    x_house['x2'] = x_house['x']**1.5 # Weith position more.
    x_house['y2'] = x_house['y']**1.5
    x_poly = poly.transform(x_house)
    pred = model.predict(x_poly)[0]
    return float(pred)


y_columns=["x","y","m2","house_type","standard"]
p_degree = 3
model = LinearRegression()

poly = PolynomialFeatures(degree=p_degree)
build_and_train_model()

print(f"m2  {predict_price(100,100, 200,1, 1)}") # just test one..
