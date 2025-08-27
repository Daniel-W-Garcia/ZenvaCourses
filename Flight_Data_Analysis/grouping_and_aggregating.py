import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
df = pd.read_csv('flights.csv')

#%%
busiest_routes = df.groupby(['Origin', 'Destination']).agg({'Passengers' : 'sum'})
busiest_routes = busiest_routes.sort_values(by='Passengers', ascending=False)
print(busiest_routes.head())

#%%
busiest_routes = df.groupby(['Origin', 'Destination']).agg({'Passengers' : 'sum', 'Flights' : 'sum'})
busiest_routes = busiest_routes.sort_values(by=['Passengers', 'Flights'], ascending=[False, False])
print(busiest_routes.head(10))

#%%
df['Month'] = pd.to_datetime(df['Fly Date'], format='%Y%m').dt.to_period('M')
monthly_trends = df.groupby('Month').agg({'Flights': 'sum'})
monthly_trends = monthly_trends.sort_values(by='Month')
print(monthly_trends)

#%%
distance_bins = pd.cut(df['Distance'], bins=[0, 500, 1000, 2000, 3000, 4000, df['Distance'].max()])
distance_group = df.groupby(distance_bins).agg({'Flights': 'sum', 'Passengers': 'sum'})
print(distance_group.sort_values(by='Distance', ascending=False))

#%%
busiest_airports = df.groupby('Origin').agg({'Flights': 'sum'}).nlargest(10, 'Flights')
busiest_airports.plot(kind='bar')
plt.title('Top 10 Busiest Airports by Outgoing Flights')
plt.xlabel('Airport')
plt.ylabel('Number of Flights')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()