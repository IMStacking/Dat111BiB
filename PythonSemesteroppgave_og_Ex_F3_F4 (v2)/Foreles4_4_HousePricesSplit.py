from Foreles4_0_Imports import *

df = pd.read_csv('House_Prices.csv')                     # load data
X = df[['m2']]       # features
#X = df[['m2', 'standard', 'house_type', 'x', 'y']]       # features
y = df['sales_price']                                    # target

model = LinearRegression()                               # model
poly = PolynomialFeatures(degree=3)                      # polynomial degree

# Better in large sets ....
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.35, random_state=1234)             # split

model.fit(poly.fit_transform(X_train), y_train)          # train

y_pred = model.predict(poly.fit_transform(X))            # predict full set
mae = mean_absolute_error(y, y_pred)                     # MAE
r2  = r2_score(y, y_pred)                                # R²
print(f"Kjente data  MAE={int(mae)}, R2={r2:.2f}")       # title

y_test_pred = model.predict(poly.fit_transform(X_test))  # predict test set
mae_test    = mean_absolute_error(y_test, y_test_pred)   # MAE test
r2_test     = r2_score(y_test, y_test_pred)              # R² test
print(f"Ukjente data MAE={int(mae_test)}, R2={r2_test:.2f}")   # test metrics

n_test = 5
dfTest = X.iloc[:n_test]                                     # first 10 rows (features only)
dfTest["est"] = model.predict(poly.transform(dfTest)).astype(int)   # predicted price (int)
dfTest["sales_price"] = df.iloc[:n_test]["sales_price"]      # actual price

print(f"\nTest av de {n_test} første husene:\n")
print(dfTest)
