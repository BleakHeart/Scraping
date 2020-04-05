import os
import pandas as pd
import re

path = "D:/OneDrive\OneDrive - Universita' degli Studi di Roma Tor Vergata/Python/Scraping/"

df = pd.read_csv(path + 'rotte_navali.csv')

#df.query("partenza.str.contains('(  )')")

mask = r"\([^)]+\)"

df = df[df.partenza.str.contains(mask)].apply(bla bla)

df

print(df)