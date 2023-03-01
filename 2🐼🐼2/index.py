import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('x.csv', index_col='Year')

print(df.head())
#print(df.tail())
print(df['Australia']) #.plot()
#plt.show()

#print(df.describe())

#print(df.loc[1990])

#print(df.iloc[2])

#print(df.Australia)
df.to_csv('new_df.csv')
