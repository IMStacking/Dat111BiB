from Foreles4_0_Imports import *
df = pd.read_csv('House_Prices.csv')            # load data

fig = plt.figure(figsize=(10,6))                # plot size
ax = fig.add_axes((.1, .10, .85, .8))           # axes position
ax.set_xlabel('Feature 1 - m2')                 # x-label
ax.set_ylabel('Feature 2 - Standard 4=top)')    # y-label
ax.set_ylim(0.5,4.5)

poly = PolynomialFeatures(degree=4)             # polynomial degree
X = df[['m2', 'standard']]                      # features
y = df['sales_price']                           # target

model = LinearRegression()                      # model
model.fit(poly.fit_transform(X) ,   y)          # train

y_pred = model.predict(poly.fit_transform(X))   # predict test set
mae = mean_absolute_error(y, y_pred)            # MAE
r2 = r2_score(y, y_pred)                        # R²
ax.set_title(f"Bolig i Bergen (Estimert/Solgt for) - Mae={int(mae)}, R2={r2:.2f}")  # title

# --- Test 15 new houses -, pick from original set --
dfTest = df[['m2', 'standard']].iloc[100:120]
dfTest["Estimated"] = model.predict(poly.fit_transform(dfTest))                  # predictions for the 15 houses
dfTest["sales_price"] = df[['sales_price']].iloc[100:120]

def plot_bubble(m2, standard, price_estimated, sales_price):             # bubble plot
    red = min(1, price_estimated / 20_000)
    color = (1 - red,1-red,1-red)
    color_back = (red, 0.5 - red*0.5, 0)                          # RGB
    ax.scatter(m2, standard, color=color_back, s=1500)            # bubble
    ax.text(m2, standard,
            s=f"{price_estimated/1000:.1f}\n{sales_price/1000:.1f}",                            # only estimated
            color="yellow",fontweight="bold", fontsize=11, ha='center', va='center')  # text
    plt.draw()                                                    # update

for _, r in dfTest.iterrows():                                    # clean loop
    plot_bubble(r.m2, r.standard, r.Estimated, r.sales_price)            # plot bubble

plt.show()                                                        # show plot
feature_names = poly.get_feature_names_out(X.columns)

formula = f"y = {model.intercept_:.2f}"
for coef, feature in zip(model.coef_, feature_names):
    if feature != "1":  # skip constant term
        formula += f" + ({coef:.4f})*{feature}"

print(formula)