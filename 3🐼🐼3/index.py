
import pandas as pd

df = pd.read_csv('new_df.csv', index_col='Year', parse_dates=['Year'])
#print(df.head())
#print(df.dtypes)
#print(df.index)
df.Monaco =pd.to_numeric(df.Monaco, errors='coerce')
#print(df.Monaco)
df.Germany = df.Germany.astype('int64')
print(df.Germany)