import pandas
import requests
import numpy
desired_width = 1000
pandas.set_option('display.width', desired_width)
pandas.set_option('display.max_columns',100)

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

president_elections = pandas.read_csv("1976-2020-president.csv")
#print(president_elections)

president_elections["Rank"] = president_elections.groupby(["year", "state"])["candidatevotes"].rank(ascending=False)

president_elections = president_elections[president_elections["Rank"] == 1]

president_elections["xxx"] = president_elections["party_simplified"].shift(-1)

president_elections["porovnani"] = numpy.where(president_elections["xxx"] != president_elections["party_simplified"], 1,0)
president_elections = president_elections[["year", "state", "Rank", "party_simplified", "xxx","porovnani"]]
#print(president_elections)

president_elections = president_elections.groupby(["state"])["porovnani"].sum().sort_values()
print(president_elections)