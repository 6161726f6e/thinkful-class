import sqlite3 as lite
import pandas as pd

# connect to DB
conn = lite.connect('cities_weather.db')
cur = conn.cursor()

# create city table and populate data
cur.execute("drop table if exists cities")
cur.execute("create table cities(name text, state text)")

cities = (('New York City', 'NY'),
          ('Boston', 'MA'),
          ('Chicago', 'IL'),
          ('Miami', 'FL'),
          ('Dallas', 'TX'),
          ('Seattle', 'WA'),
          ('Portland', 'OR'),
          ('San Francisco', 'CA'),
          ('Los Angeles', 'CA'))

with conn:
    cur = conn.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)

# create weather table and populate data
cur.execute("drop table if exists weather")
cur.execute("create table weather(city text, year INTEGER, warm_month text, cold_month text, average_high INTEGER)")

weather = (('New York City', 2013, 'July', 'January', 62),
           ('Boston', 2013, 'July', 'January', 59),
           ('Chicago', 2013, 'July', 'January', 59),
           ('Miami', 2013, 'August', 'January', 84),
           ('Dallas', 2013, 'July', 'January', 77),
           ('Seattle', 2013, 'July', 'January', 61),
           ('Portland', 2013, 'July', 'December', 63),
           ('San Francisco', 2013, 'September', 'December', 64),
           ('Los Angeles', 2013, 'September', 'December', 75))

with conn:
    cur = conn.cursor()
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

# join data and insert into df
cur.execute("select name, state, year, warm_month, cold_month, average_high from cities inner join weather on name = city")
rows = cur.fetchall()
cols = [desc[0] for desc in cur.description]
df = pd.DataFrame(rows, columns=cols)

# print(df.head())
warm_july = df[df['warm_month'] == 'July']
print('\nThe cities that are warmest in July are:\n')
print(warm_july)

