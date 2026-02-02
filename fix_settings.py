import sqlite3
import os

db_path = os.path.abspath('settings.db3')
con = sqlite3.connect(db_path)
cur = con.cursor()

# Insert default cointype if missing
cur.execute("SELECT value FROM Settings WHERE key='cointype';")
row = cur.fetchone()
if row is None:
    cur.execute("INSERT INTO Settings (key, value) VALUES (?, ?);", ('cointype', 'Bitcoin'))
    print("Inserted default cointype: Bitcoin")
else:
    print("cointype already set:", row[0])

con.commit()
con.close()