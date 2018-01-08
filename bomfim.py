import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score
import numpy as np

df = pd.read_csv("bomfim.csv")
X = df[["quartos", "metros", "vagas"]]
y = df["aluguel"] + df["condominio"]

# Visualization

plt.scatter(X["metros"], y,
            s=[quartos ** 2 * 200 for quartos in X["quartos"]],
            c=["green" if vagas > 0 else "red" for vagas in X["vagas"]])
plt.xlabel("Metros")
plt.ylabel("Aluguel + Condomínio")
plt.show()


# Prediction

model = LinearRegression()
model.fit(X, y)
print("Score", cross_val_score(model, X, y).mean())

unpriced = pd.read_csv("unpriced.csv")
unpriced["predicted price"] = model.predict(unpriced)
print(unpriced)
