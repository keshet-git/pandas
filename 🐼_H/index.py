import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.to_csv('modfied.csv', index=False, sep='\t'))
#print(df.to_excel('modfied.csv', index=False))