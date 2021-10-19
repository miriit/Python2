import pandas
import requests
import numpy

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
#open("london_merged.csv", 'wb').write(r.content)

#r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
#open("titanic.csv", 'wb').write(r.content)

df_titanic = pandas.read_csv("titanic.csv")
df_titanic_pivot = pandas.pivot_table(df_titanic, index= ["Sex", "Survived"], columns="Pclass", values="Name", aggfunc=len, margins=True)
print(df_titanic_pivot)
