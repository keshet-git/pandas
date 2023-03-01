import pandas as pd

df = pd.read_csv('pokemon_data.csv')

for index, row in df.iterrows(): #read ech rw
    print(index, row['Name'])