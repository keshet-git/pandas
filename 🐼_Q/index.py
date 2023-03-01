import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

df['count'] = 1 

#x = df.groupby(['Type 1']).mean().sort_values('HP', ascending=False)
#y = df.groupby(['Type 1']).sum()
z = df.groupby(['Type 1', 'Type 2']).count()['count']

print(z)