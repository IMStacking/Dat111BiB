from Foreles4_0_Imports import *


np.random.seed(1234)
X = np.linspace(0, 30, 81).reshape(-1, 1)                     # synthetic X
y = ( 1800 + np.random.randint(-100, 100, X.shape)
    + 200 * np.sin((X-10)/3) )                                # wave: down → up → down


poly = PolynomialFeatures(degree=4)
poly.fit(X)                                             # learn polynomial expansion

model = LinearRegression()
model.fit(poly.transform(X), y)                              # fit model

fig = plt.figure(figsize=(10, 4))                             # fig
ax = fig.add_subplot(1, 1, 1)                                 # axis

ax.scatter(X, y, color='blue', label='Train')
ax.plot(X, model.predict(poly.transform(X)), color='red', label='Curve')

# Check model quality
y_pred = model.predict(poly.transform(X))                # predict
mae = mean_absolute_error(y, y_pred)                     # MAE
r2  = r2_score(y, y_pred)                                # R2
ax.set_xlabel('km from Bergen')                               # x-label
ax.set_ylabel('Rain (mm)')                                    # y-label
ax.set_title(f'MAE:{int(mae)}  R2:{r2:.2f}')                  # title
ax.legend()                                                   # legend

plt.show()                                                    # render
