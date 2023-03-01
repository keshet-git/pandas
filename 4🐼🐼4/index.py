import pandas as pd
import matplotlib.pyplot as plt
#%config InlineBackend.figure_format = 'svg'

df = pd.read_csv('new_df.csv', index_col='Year', parse_dates=['Year'])

df.Monaco =pd.to_numeric(df.Monaco, errors='coerce')

##df_totals = df.sum(axis=0).sort_values()[-5:]
df_totals = df.sum(axis=0).sort_values()[:5]
ax = df_totals.plot(kind='bar', figsize=(8, 3), title='co$_2$ Emmision $_{(1990 - 2014)})$')
ax.set_ylabel('co$_25 (ktonnts)')
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.show()