import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Larger spread in x
x_m2s = np.array([30, 50, 70, 90, 110]).reshape(-1, 1)

# Mostly linear, one point deliberately off
y_train = np.array([3.0, 4.3, 6.7, 9.0, 11.8]).reshape(-1, 1)

model = LinearRegression()
model.fit(x_m2s, y_train)

y_pred = model.predict(x_m2s)

r2 = r2_score(y_train, y_pred)
mae = mean_absolute_error(y_train, y_pred)

print(f"R²  = {r2:.6f}")
print(f"MAE = {mae:.6f}")

fig, ax = plt.subplots(figsize=(6, 4))

ax.scatter(x_m2s, y_train, color="blue", label="Training points")
ax.plot(x_m2s, y_pred, color="red", linewidth=2, label="Regression line")

ax.set_title(f"House Prices: R² = {r2:.2f}, MAE = {mae:.3f}")
ax.set_xlabel("m²")
ax.set_ylabel("Price (millions)")
ax.legend()
ax.grid(True)

plt.show()