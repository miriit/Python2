import pandas
import requests
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

df_rental = pandas.read_csv("london_merged.csv")
#print(df_rental)
df_rental["timestamp"] = pandas.to_datetime(df_rental["timestamp"])
df_rental["year"] = df_rental["timestamp"].dt.year
#print(df_rental.head())
df_rental = pandas.pivot_table(df_rental, index= "year", columns="weather_code", values="cnt", aggfunc=numpy.sum)
print(df_rental)
