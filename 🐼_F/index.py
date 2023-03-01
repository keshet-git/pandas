import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))
