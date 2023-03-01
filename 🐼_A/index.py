import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#df = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df)
#print(df.head(3))
print(df.columns)
#print(df[['Name', 'Type 1', 'HP']])