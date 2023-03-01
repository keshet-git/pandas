import pandas as pd
import re
df = pd.read_csv('pokemon_data.csv')

#df.to_csv('modified.txt', index=False, sep='\t')

r = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(r)