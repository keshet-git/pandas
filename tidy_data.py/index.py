import pandas as pd
# terning data to a long format

pew = pd.read_csv('pew.csv')

#print(pew.head())
#print(pew.columns)

pew_Long = pd.melt(pew, id_vars='religion')

#print(pew_Long.head())
pew_long2 = pd.melt(pew, id_vars='religion',
var_name='income',
value_name='count')

#print(pew_long2.head())
bill = pd.read_csv('billboard.csv')

# print(bill.head())

bill_melt = pd.melt(
    bill,
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
    var_name='week',
    value_name='rating')
'''
print(bill_melt.head())
print(bill.shape)
print(bill_melt.shape)
'''
ebola = pd.read_csv('country_timeseries.csv')

#print(ebola.head())

ebola_long = pd.melt(ebola,
id_vars=['Date', 'Day'])

#print(ebola_long.head())

#print('Cases_Guinea'.split('_'))
variable_split = ebola_long['variable'].str.split('_')
#print(variable_split[0][0])
#print(type(variable_split))
# print(type(variable_split[0][0]))

#print(variable_split.str[0])
#print(variable_split.str[1])

ebola_long['stats'] = variable_split.str.get(0)
ebola_long['country'] = variable_split.str.get(1)

#print(ebola_long.head())

ebola_long[['stats_e', 'country_e']] = (ebola_long['variable']
.str
.split('_', expand=True))
#print(ebola_long)

weather = pd.read_csv('weather.csv')

#
#print(weather)
'''can use pd.melt or weather.elt'''
weather_melt = pd.melt(
    weather,
    id_vars=['id','year','month', 'element'],
    var_name='day',
    value_name='temp'
)

#print(weather_melt.head())

weather_tidy = weather_melt.pivot_table(
    index=['id', 'year', 'month', 'day'],
    columns='element',
    values='temp'
)

#print(weather_tidy.reset_index())
#print(bill.head())
#print(bill_melt.head())

bm  = bill_melt.loc[bill_melt['track'] == 'Loser']
#print(bm)

bill_songs = bill_melt[['year', 'artist', 'track', 'time']]

#print(bill_songs)

#print(bill_songs.shape)

bill_songs = bill_songs.drop_duplicates()
#print(bill_songs.shape)
#print(bill_songs.drop_duplicates())

bill_songs['id'] = range(len(bill_songs))

#print(bill_songs.head())
bill_songs.to_csv('bill_song.csv',index=False)

bill_rating = bill_melt.merge(
    bill_songs, on=['year', 'artist', 'track', 'time']
)

#print(bill_rating.head())

bill_rating = bill_rating[['id', 'date.entered', 'week', 'rating']]

print(bill_rating.sample(30))

bill_rating.to_csv('bill_rating.csv', index=False)

print(bill_rating.info())