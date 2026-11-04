import matplotlib.pyplot as py
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
y_nedbor = [
    2500, 2650, 2300, 2550, 2100,
    2250, 1900, 2050, 1750, 1850,
    1600, 1700, 1500, 1650, 1400,
    1550, 1450, 1600, 1350, 1500
]
X_km = np.linspace(0, 30, len(y_nedbor))      # km fra sentrum .. (0,1,2...
fig = py.figure(figsize=(10,4))
ax = fig.add_axes((0.1,0.14,0.8,0.8))

model = LinearRegression()                    # tren lineær modell
X = X_km.reshape(-1,1)                        # put list into 1st column feauture 2D table.
model.fit(X, y_nedbor)                        # Train the model.
y_pred = model.predict(X)

ax.scatter(X_km, y_nedbor, color="blue")
ax.scatter(X_km, y_pred, color="green")
ax.plot(X_km, y_pred, color="red")
ax.legend(["real", "predicted", "regression line"])

mae = mean_absolute_error(y_nedbor, y_pred)      # MAE
r2 = r2_score(y_nedbor, y_pred)                  # R²

ax.set_title(f"Nedbør fra Bergen Sentrum MAE:{mae:.0f} R2:{r2:.1f}")
ax.set_xlabel("km fra sentrum")
ax.set_ylabel("mm nedbør")
py.show()
