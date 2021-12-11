import pandas

zvirata = pandas.read_csv("lexikon-zvirat.csv", sep=";")
zvirata = zvirata.dropna(how="all", axis="rows")
zvirata = zvirata.dropna(how="all", axis="columns")
zvirata = zvirata.set_index("id")

def popisek(radek):
   nazev = str(radek.title)
   strava = str(radek.food)
   popis_stravy = str(radek.food_note)
   popis_zvirete = str(radek.description)
   return f"{nazev} preferuje následující typ stravy:{strava}. Konkrétně ocení když mu do misky přistanou {popis_stravy} Jak toto zvíře poznáme:{popis_zvirete}."

zvirata["popisek"] = zvirata.apply(popisek, axis=1)
print(zvirata["popisek"])
