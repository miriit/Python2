import numpy
import pandas
import requests

desired_width = 1000
pandas.set_option('display.max_columns', None)
pandas.set_option("display.width", desired_width)
numpy.set_printoptions(linewidth=desired_width)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

zvirata = pandas.read_csv("lexikon-zvirat.csv", sep=";")
zvirata = zvirata.dropna(how="all", axis="rows")
zvirata = zvirata.dropna(how="all", axis="columns")
zvirata = zvirata.set_index("id")
print(zvirata)
"""
def check_url(radek):
    if isinstance(radek.image_src, str):
        if radek.image_src.startswith("https://zoopraha.cz/images/"):
            if radek.image_src.endswith(".jpg"):
                return radek.title

for radek in zvirata.itertuples():
    print(check_url(zvirata))"""
#radek.image_src.startswith("https://zoopraha.cz/images/")



#for zvire in zvirata.itertuples():
#    check_url()
