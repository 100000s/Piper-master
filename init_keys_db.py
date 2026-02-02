import sqlite3

# This script will create the 'keys' table in keys.db3 if it does not exist.

db_path = 'keys.db3'
con = sqlite3.connect(db_path)
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS keys (
    serialnum TEXT PRIMARY KEY,
    public TEXT,
    private TEXT,
    btcaddr TEXT,
    coinType TEXT,
    password TEXT,
    encrypted INTEGER
);
''')

con.commit()
con.close()
print("Created 'keys' table in keys.db3 (if it did not exist).")
