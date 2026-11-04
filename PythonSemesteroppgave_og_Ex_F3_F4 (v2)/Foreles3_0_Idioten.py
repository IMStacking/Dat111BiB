import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

X =  np.array([50,100,150,200,250]).reshape(-1,1)
y =  [2_000,4_000,6_000,8_000,10_000]               # y = 40x

model = LinearRegression()                          # lineær modell
model.fit(X, y)                                     # tren på alle data -> y = f(x) = 2*x

y_pred = model.predict(X)                           # prediksjon
r2  = r2_score(y, y_pred)                           # R² = 1.0
mae = mean_absolute_error(y, y_pred)                # MAE = 0.0
print("R2         :", r2)                           # perfekt R²
print("MAE        :", round(mae,3))                 # perfekt MAE

x_new = np.array([25,75,125]).reshape(-1,1)
y_new = model.predict(x_new)

print("m2 =    :", x_new.T)                           # back to row
print("pris =  :", y_new)


