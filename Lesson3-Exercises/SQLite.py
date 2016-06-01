import sqlite3 as lite

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
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January')")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January')")

