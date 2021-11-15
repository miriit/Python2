import pandas
import requests
import seaborn
import matplotlib.pyplot as plt
import numpy
desired_width = 1000
pandas.set_option('display.max_columns', None)
pandas.set_option("display.width", desired_width)
numpy.set_printoptions(linewidth=desired_width)
#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
#open("crypto_prices.csv", "wb").write(r.content)

crypto_prices = pandas.read_csv("crypto_prices.csv")
crypto_prices["x"] = crypto_prices.groupby("Name")["Close"].pct_change()
#print(crypto_prices)

crypto_prices_pivot = pandas.pivot_table(crypto_prices, index="Date", columns="Symbol", values="x")
print(crypto_prices_pivot.corr())

seaborn.jointplot("WBTC", "LTC", crypto_prices_pivot, kind='scatter')
plt.show()

seaborn.jointplot("UNI", "DOGE", crypto_prices_pivot, kind='scatter')
plt.show()