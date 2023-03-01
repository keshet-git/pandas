import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

print(df)