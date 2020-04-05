import camelot
import pandas as pd
from matplotlib.pyplot import *
import os

path = os.getcwd()
'''
leggo il file pdf selezionando le pagine di mio interesse e indico l'area del foglio tramite table_areas 
dove ['x_leftup, yleftup, xrightdown, yrightdown'] (le coordinate vanno messe in termini di pixel e le 
righe 16 e 17 vi aiutano a farlo). L'attributo flavor non ho ben capito a cosa serve ma ho visto che 
i csv escono meglio. 
'''
df = camelot.read_pdf(path + "/ENAC_Traffic_data_2017_en.pdf", pages='45,46,47', flavor='stream', table_areas=['30,690,552,16'])

# in questo modo è possibile vedere le aree che il pacchetto riesce a individuare
camelot.plot(df[0], kind='text')
show()

df.export(path + '/Risultati/' + 'boh.csv', f='csv')

path = "D:/OneDrive/OneDrive - Universita' degli Studi di Roma Tor Vergata/Python/Scraping/Risultati/"

'''
Siccome camelot crea un file csv per ogni tabella che individua, creato questo piccolo script che legge 
ciascun csv e li unisce in un dataframe. l'attributo names permette di assegnare un nome ad ogni colonna. 
thousands permette alla libreria pandas di leggere numeri in un formato dove i seperatori delle migliaia 
sono punti  
'''
df_from_each_file = (pd.read_csv(path + f, names=['partenza', 'arrivo', 'paese', 'passeggeri'], thousands=r'.') for f in os.listdir(path))
df = pd.concat(df_from_each_file, ignore_index = True)
df.to_csv('passeggeri_voli_non_europei_2017.csv', index=False)