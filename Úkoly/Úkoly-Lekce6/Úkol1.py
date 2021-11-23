import requests
import pandas
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)

psenice = pandas.read_csv("psenice.csv")
print(psenice)

x = psenice["Rosa"]
y = psenice["Canadian"]
print(mannwhitneyu(x, y))