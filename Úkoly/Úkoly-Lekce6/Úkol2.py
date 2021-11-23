import requests
import pandas
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

air_polution = pandas.read_csv("air_polution_ukol.csv")
air_polution["date"] = pandas.to_datetime(air_polution["date"], format="%Y/%m/%d")
air_polution["year"] = air_polution["date"].dt.year
air_polution["month"] = air_polution["date"].dt.month

x = air_polution[(air_polution["year"] == 2019) & (air_polution["month"] == 1)]["pm25"]
y = air_polution[(air_polution["year"] == 2020) & (air_polution["month"] == 1)]["pm25"]

print(mannwhitneyu(x, y))