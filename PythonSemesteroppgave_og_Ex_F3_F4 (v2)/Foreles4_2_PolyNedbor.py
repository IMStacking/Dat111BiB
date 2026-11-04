from Foreles4_0_Imports import *

np.random.seed(1234)                                          # seed
X_Km = np.linspace(0, 20, 21).reshape(-1, 1)                  # km values
y = 1500 + np.random.randint(-150, 450, size=X_Km.shape) + (X_Km-12)**2 * 7  # rain

poly = PolynomialFeatures(degree=4)                           # poly degree 1
X_poly = poly.fit_transform(X_Km)                             # expand

model = LinearRegression()                                    # model
model.fit(X_poly, y)                                          # fit

y_pred = model.predict(X_poly)                                # predict
mae = mean_absolute_error(y, y_pred)                          # MAE
r_score = r2_score(y, y_pred)                                 # R2

fig = plt.figure(figsize=(6,4))                              # fig
ax = fig.add_subplot(1,1,1)                                   # axis

ax.scatter(X_Km, y, color='blue', label='Train data')         # train pts
ax.scatter(X_Km, y_pred, color='red', label='Estimated')      # pred pts
ax.plot(X_Km, y_pred, color='red')                            # curve

ax.set_xlabel('km from Bergen')                               # x-label
ax.set_ylabel('Rain (mm)')                                    # y-label
ax.set_title(f'Linear Regression MAE:{mae:.2f}, R2:{r_score:.2f}')  # title
ax.legend()                                                   # legend

plt.show()                                                    # render
