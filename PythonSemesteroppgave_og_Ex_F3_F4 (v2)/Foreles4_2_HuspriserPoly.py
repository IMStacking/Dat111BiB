from Foreles4_0_Imports import *

df = pd.read_csv("House_Prices.csv")             # load data
df = df[['m2','house_type', 'standard', 'sales_price']]


print( df.iloc[0:5] )

df = df[(df["house_type"] == 2) & (df["standard"] > 3)]
m2s = df["m2"].values.reshape(-1, 1)             # m²
prices = df["sales_price"].values                # price

poly = PolynomialFeatures(degree=2)              # polynomial degree
m2s_poly = poly.fit_transform(m2s)               # transform

model = LinearRegression()                       # model
model.fit(m2s_poly, prices)                      # train

predict_m2 = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]   # hardcoded m²
predict_table = np.array(predict_m2).reshape(-1,1)             # prediction table
predict_poly = poly.transform(predict_table)                   # transform
predict_prices = model.predict(predict_poly)                   # predict

prediction_df = pd.DataFrame({                                 # dataframe
    "m2": predict_m2,
    "predicted_price": predict_prices
})

mae = mean_absolute_error(prices, model.predict(m2s_poly))     # MAE
r2  = r2_score(prices, model.predict(m2s_poly))                # R²

fig = plt.figure(figsize=(10,5))                               # figure
ax = fig.add_subplot(1,1,1)                                    # axis

ax.scatter(df["m2"], df["sales_price"], color="red", s=10, label="Training data")   # data
ax.plot(predict_m2, predict_prices, color="blue", linewidth=2, label="Polynomial fit")  # fit

ax.set_title(f"House Price vs m² (MAE {mae:.0f}, R² {r2:.3f})")                      # title
ax.set_xlabel("Size (m²)")                                                          # x-label
ax.set_ylabel("Price")                                                              # y-label
ax.grid(True)                                                                       # grid
ax.legend()                                                                         # legend

plt.show()                                                                          # display
