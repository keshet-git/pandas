import pandas as pn


df = pn.read_csv('gapminder.tsv', sep='\t')

#print(df.head())
#print(df.columns)
#print(df.values)
#print(type(df))
#print(df.shape)
#print(df.info())
#print(df['country'])
country_df =df['country']
#print(country_df.head())
subset = df[['country', 'continent', 'year']]
#print(subset.head())
#print(pn.__version__)
#print(df.loc[2])
#print(df.loc[[2, 0]])
#print(df.iloc[2])
subst2 =df.loc[:, ['year', 'pop']]
#print(subst2.head())
x = df.loc[df['year'] == 1967, ['year', 'pop']]
s = df.loc[(df['year'] == 1967) & (df['pop'] > 1_000_000), ['year', 'pop']]
print(x)