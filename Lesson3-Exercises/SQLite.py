import sqlite3 as lite
import pandas as pd

conn = lite.connect('getting_started.db')

with conn:
    # From the connection, you get a cursor object, which goes over the records from queries
    cur = conn.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    # You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
    data = cur.fetchone()
    # Read to print result
    print("SQLite version: %s" % data)

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 45)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 54)")

cities = (('Las Vegas', 'NV'),
          ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 59),
           ('Atlanta', 2013, 'July', 'January', 45))

conn = lite.connect('getting_started.db')

# insert rows by passing tuples
with conn:
    cur = conn.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    for row in rows:
        print(row)

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    print(df.head())
