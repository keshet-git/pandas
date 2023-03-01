import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] +df['Sp. Def'] + df['Speed']
#df.loc[df['Total'] > 500, ['Generatipn', 'Legndary']] = 'TEST VALU'
df.loc[df['Total'] > 500, ['Generatipn', 'Legndary']] = ['Test 1', 'Test 2']
print(df)
