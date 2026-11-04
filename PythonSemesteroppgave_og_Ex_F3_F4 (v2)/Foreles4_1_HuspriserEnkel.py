from Foreles4_0_Imports import *

df = pd.read_csv("House_Prices.csv")             # load data
df = df[(df["house_type"] == 2) & (df["standard"] > 3)]

m2s = df["m2"].values.reshape(-1, 1)             # m²
prices = df["sales_price"].values                # price

model = LinearRegression()                       # model
model.fit(m2s, prices)                           # train

predict_prices = model.predict(m2s)              # predict
mae = mean_absolute_error(prices, predict_prices)  # MAE
r2  = r2_score(prices, predict_prices)             # R²

fig = plt.figure(figsize=(10,5))                 # figure
ax = fig.add_subplot(1,1,1)                      # axis

ax.scatter(m2s, prices, color="red", s=10, label="Training data")     # data
ax.plot(m2s, predict_prices, color="blue", linewidth=2, label="Fit")  # regression line

ax.set_title(f"House Price vs m² (MAE {mae:.0f}, R² {r2:.3f})")       # title
ax.set_xlabel("Size (m²)")                                            # x-label
ax.set_ylabel("Price")                                                # y-label
ax.grid(True)                                                         # grid
ax.legend()                                                           # legend

plt.show()                                                            # render
