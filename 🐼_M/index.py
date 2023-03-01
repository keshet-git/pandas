import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

df.loc[df['Total'] > 500, ['Generation','Legendary']] = 'Flamer'

df.to_csv('modified.txt', index=False, sep='\t')
#print(df)