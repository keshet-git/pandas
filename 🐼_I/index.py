import pandas as pd

df = pd.read_csv('pokemon_data.csv')

df.to_csv('modified.txt', index=False, sep='\t')

r = df.loc[~df['Name'].str.contains('Mega')]
print(r)