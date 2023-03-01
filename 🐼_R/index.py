import pandas as pd
import re


new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modfied.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    #print('CHUNK DF')
    #print(df)

    x = new_df = pd.concat([new_df, results])

print(x)