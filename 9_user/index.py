import pandas as pd

#df = pd.read_csv('users_office (2).csv')
#df = pd.read_csv('microsoft_workers (2).csv')
#df = pd.read_csv('department_location.csv')

first = pd.read_csv('microsoft_workers (2).csv')
second = pd.read_csv('users_office (1).csv')
third = pd.read_csv('department_location.csv')
'''
print(first.head())
print(second.head())
print(third.head())
'''
first.set_index('User Name', inplace=True)
second.set_index('User Name', inplace=True)

#print(first.head())
#print(second.head())
joined = first.join(second)

print(joined.head())
#df = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df)
#print(df.head(3))
#print(df.columns)
