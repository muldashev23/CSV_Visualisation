import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

# --------------------------Data Exploration---------------------#

print(f'The shape of the csv file: {df_tesla.shape}')
print(f'Columns  are {df_tesla.columns}')
print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')
print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')

# -----------------------Converting Strings to DateTime Objects-----------#
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)

# -----------------------Data Visualisation----------------------------#

years = mdates.YearLocator()
month = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)
ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#e6232e", linewidth=3)

ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
ax1.set_ylabel('TSLA Stock Price', color='#e6232e', fontsize=14)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(month)
plt.show()
