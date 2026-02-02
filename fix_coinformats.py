import sqlite3
import os

db_path = os.path.abspath('settings.db3')
con = sqlite3.connect(db_path)
cur = con.cursor()

# Insert default Bitcoin entry into CoinFormats if missing
cur.execute("SELECT name FROM CoinFormats WHERE name=?;", ('Bitcoin',))
row = cur.fetchone()
if row is None:
    # Typical Bitcoin values: versionNum=0, prefix='1', bgfile='blank'
    cur.execute("INSERT INTO CoinFormats (versionNum, prefix, bgfile, name) VALUES (?, ?, ?, ?);", (0, '1', 'blank', 'Bitcoin'))
    print("Inserted default CoinFormats entry for Bitcoin.")
else:
    print("Bitcoin already exists in CoinFormats.")

con.commit()
con.close()
