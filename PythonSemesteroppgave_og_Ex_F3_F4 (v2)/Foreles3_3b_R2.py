import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

x_hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y_grades = np.array([3.5, 3.6, 3.8, 5.1, 5.6])

model = LinearRegression().fit(x_hours, y_grades)
y_pred = model.predict(x_hours)

r2 = r2_score(y_grades, y_pred)
y_mean = np.mean(y_grades)

ss_res = np.sum((y_grades - y_pred) ** 2)
ss_tot = np.sum((y_grades - y_mean) ** 2)

fig, ax = plt.subplots(figsize=(8, 7))

ax.scatter(x_hours, y_grades, color="blue", s=80, label="Actual")
ax.plot(x_hours, y_pred, color="red", lw=2, label="Regression line")
ax.axhline(y_mean, color="black", ls="--", label=f"Mean = {y_mean:.2f}")

for xi, yi, yp in zip(x_hours.flatten(), y_grades, y_pred): # Code to write rectangels
    side_res = max(0.01, abs(yi - yp))
    ax.add_patch(Rectangle((xi, min(yi, yp)), side_res, side_res,
                           facecolor="green", alpha=0.3))
    ax.text(xi + side_res/2,
            min(yi, yp) + side_res/2,
            f"{side_res**2:.2f}",
            ha="center", va="center", fontsize=8)

    side_tot = max(0.01, abs(yi - y_mean))
    ax.add_patch(Rectangle((xi - side_tot, min(yi, y_mean)),
                           side_tot, side_tot,
                           facecolor="orange", alpha=0.4))
    ax.text(xi - side_tot/2,
            min(yi, y_mean) + side_tot/2,
            f"{side_tot**2:.2f}",
            ha="center", va="center", fontsize=8, color="red")
    ax.plot([xi, xi], [yi, yp], "g--", alpha=0.8)

ax.set_title(
    f"R² = 1 - SS_res/SS_tot\n (green=SS_res, orange=SS_tot)\n"
    f"SS_res={ss_res:.2f}, SS_tot={ss_tot:.2f}, R²={r2:.3f}"
)

ax.set_xlabel("Studietid")
ax.set_yticks([1, 2, 3, 4, 5, 6])
ax.set_yticklabels(["F=1", "E=2", "D=3", "C=4", "B=5", "A=6"])
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()