import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# --- Load and train model ---
df_original = pd.read_csv("House_Prices.csv")        # original dataset
X = df_original[["m2", "standard"]]                  # features
y = df_original["sales_price"]                       # target
# print(X.head().values)
model = LinearRegression()
model.fit(X, y)                                      # make f(X)

y_pred = model.predict(X)                            # y_pred = f(X)  or f(m2,standard)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"\nMAE: {mae:.0f}, R2: {r2:.2f}")

# --- Pick 5 houses from dataset (evaluating) ---
df_samples = df_original.sample(5, random_state=42)            # random 5 houses
df_samples["predicted"] = model.predict(df_samples[["m2", "standard"]])  # append predicted to the dataframe
print("Test av 5 boliger fra datasettet:")
print(f"{'m2':>5} {'Std':>5} {'Salesprice':>10} {'Predicted':>10}")
for i, r in df_samples.iterrows():
    print(f"{r.m2:>5,.0f} {r.standard:>5} {r.sales_price:>10,.0f} {r.predicted:>10,.0f}")