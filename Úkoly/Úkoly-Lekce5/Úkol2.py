import pandas as pd
import requests
import matplotlib.pyplot as plt
import statistics
from scipy.stats import gmean

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
#open("crypto_prices.csv", "wb").write(r.content)

crypto_prices = pd.read_csv("crypto_prices.csv")
crypto_prices_link = crypto_prices[crypto_prices["Symbol"] == "LINK"]
print(crypto_prices_link)

crypto_prices_link["x"] = crypto_prices_link.groupby(["Symbol"])["Close"].pct_change() + 1
crypto_prices_link.dropna(inplace=True)
print(crypto_prices_link)

x = crypto_prices_link.groupby(["Symbol"])["x"].apply(gmean) - 1
print(x)
