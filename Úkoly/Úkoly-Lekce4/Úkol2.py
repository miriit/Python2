import pandas
import datetime
import psycopg2
from sqlalchemy import create_engine, inspect
pandas.set_option('display.max_columns', None)
HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "miriamatyralova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "p=?yLFrmJVLsHxkw"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)
crime = pandas.read_sql("crime", con=engine)
print(crime.columns)

kradez_aut = pandas.read_sql("SELECT * from crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT' AND \"SECONDARY_DESCRIPTION\" = 'AUTOMOBILE'", con=engine)
#print(kradez_aut)

kradez_aut["date"] = pandas.to_datetime(kradez_aut["DATE_OF_OCCURRENCE"])
kradez_aut["month"] = kradez_aut["date"].dt.month

kradez_aut_podle_mesice = kradez_aut.groupby(["month"]).size()
print(kradez_aut_podle_mesice)

