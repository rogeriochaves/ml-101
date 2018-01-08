import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score
import numpy as np

df = pd.read_csv("apartments.clean.csv")
X = df[["bedrooms", "area"]]
y = df["price"]

# Visualization

plt.scatter(X["area"], y,
            s=[quartos ** 2 * 200 for quartos in X["bedrooms"]])
plt.xlabel("Metros")
plt.ylabel("Aluguel")
plt.show()


# Prediction

model = LinearRegression()
model.fit(X, y)
print("Score", cross_val_score(model, X, y).mean())

unpriced = pd.read_csv("unpriced.csv")
unpriced["predicted price"] = model.predict(unpriced)
print(unpriced)
