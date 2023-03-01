import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] +df['Sp. Def'] + df['Speed']

x = df.to_csv('modfied.csv', index=False, sep='\t')

x = df.drop(columns=['Total'])

x.loc[df['Total'] > 500, ['Generation','Legendary']] == 'TEST VALUE'

print(x)