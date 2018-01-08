import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

X = pd.Series([80.0, 150.0, 76.0, 40.0])
y = pd.Series([1000.0, 1700.0, 960.0, 600.0])

plt.plot(X, y, "ro")
plt.plot(X, y, "r")
plt.axis([0, 300, 0, 3000])
plt.xlabel("Metros²")
plt.ylabel("Aluguel + Condomínio")
plt.show()
