#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%
df = pd.read_csv('flights.csv')

print(df.head(10))
print(df.info())
print(df.isnull().sum())
print(df.describe().round(2))
print(df['Origin'].value_counts())
#%%
df['Year'] = df['Fly Date'].astype(str).str.slice(0,4)

print(df['Year'])
flights_in_2000 = df[df['Year'] == '2000']
print(flights_in_2000.head())
#%%
non_lax_flights = df[~df['Origin'].isin(['LAX'])] #tilde negates. so really saying 'is not in'
print(non_lax_flights.head())
print('LAX' in non_lax_flights['Origin'].unique())
#%%
passengers_and_distance = df[(df['Passengers'] > 100) & (df['Distance'] < 1000)]
print(passengers_and_distance[['Passengers', 'Distance']])
#%%
ny_la = df[(df['Origin City']).str.contains('New York|Los Angeles') | (df['Destination City'].str.contains('New York|Los Angeles'))]
print(ny_la[['Origin City', 'Destination City']])
print(ny_la.info())
#%%
large_origin = df[df['Origin Population'] > 1000000]
print(large_origin[['Origin Population', 'Origin City']])
#%%
underbooked = df.query('Seats > Passengers')
print(underbooked[['Seats', 'Passengers']])
#%%
busy_shorthaul = df.query('Distance < 500 & Flights > 10')
print(busy_shorthaul [['Distance', 'Flights']])
busy_shorthaul.to_csv('shorthaul.csv')