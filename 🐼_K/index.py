import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

df.to_csv('modified.txt', index=False, sep='\t')

r = df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
print(r)