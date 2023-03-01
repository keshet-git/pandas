import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
#new_df = new_df.reset_index(drop=True, inplace=True)
#print(new_df)
new_df = new_df.reset_index(drop=True)
print(new_df)
#new_df.to_csv('filtered.csv')