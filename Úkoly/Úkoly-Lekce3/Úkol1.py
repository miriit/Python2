import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

zvirata = pandas.read_csv("lexikon-zvirat.csv", sep=";")
zvirata = zvirata.dropna(how="all", axis="rows")
zvirata = zvirata.dropna(how="all", axis="columns")
zvirata = zvirata.set_index("id")
#print(zvirata)

def check_url(radek):
     if isinstance(radek.image_src, str):
         if radek.image_src.startswith("https://zoopraha.cz/images/"):
            if radek.image_src.endswith(".jpg"):
                print({radek.image_src})
            else:
                print(radek.title)

#for zvire in zvirata.itertuples():
#    check_url(zvire)

for idx, zvire in zvirata.iterrows():
    check_url(zvire)


