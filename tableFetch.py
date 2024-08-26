import pandas as pd
from datetime import datetime

current_datetime = datetime.now()

CURRENT_YEAR = current_datetime.year
# CURRENT_YEAR = 2021

def getCircuits(year: int):

    url = 'https://en.wikipedia.org/wiki/'+ str(year) +'_Formula_One_World_Championship'
    tables = pd.read_html(url)
    df = tables[2]
    circuits = []
    for x in range(len(df)-1):
        circuits.append(df.iat[x,2])
    return circuits