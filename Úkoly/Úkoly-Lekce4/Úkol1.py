import pandas
import numpy
import psycopg2
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect
pandas.set_option('display.max_columns', None)
HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "miriamatyralova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "p=?yLFrmJVLsHxkw"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)
dreviny = pandas.read_sql("dreviny", con=engine)


smrk = pandas.read_sql("SELECT * from dreviny WHERE \"dd_txt\" = 'Smrk, jedle, douglaska'", con=engine)
smrk.sort_values(by="rok").plot.bar(y="hodnota", x="rok", title="vývoj objemu těžby")
plt.show()

nahodila_tezba = pandas.read_sql("SELECT * from dreviny WHERE \"druhtez_txt\" = 'Nahodilá těžba dřeva'", con=engine)
nahodila_tezba_pivot = pandas.pivot_table(nahodila_tezba, index="rok", columns="prictez_txt", values="hodnota", aggfunc=numpy.sum)
nahodila_tezba_pivot.plot()
plt.show()
