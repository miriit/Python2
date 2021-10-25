import datetime
import pandas
import requests
import numpy
import datetime

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

air_polution = pandas.read_csv("air_polution_ukol.csv")
air_polution["date"] = pandas.to_datetime(air_polution["date"], format="%Y/%m/%d")
air_polution["year"] = air_polution["date"].dt.year
air_polution["month"] = air_polution["date"].dt.month
air_polution_pivot = pandas.pivot_table(air_polution, index="month", columns="year", values="pm25", aggfunc=numpy.mean)

print(air_polution_pivot)