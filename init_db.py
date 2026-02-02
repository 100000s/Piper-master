import sqlite3

db_path = 'settings.db3'
import sqlite3
con = sqlite3.connect(db_path)
cur = con.cursor()

# Create keys table
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

# Create Settings table
cur.execute('''
CREATE TABLE IF NOT EXISTS Settings (
    key TEXT PRIMARY KEY,
    value TEXT
);
''')

# Create CoinFormats table
cur.execute('''
CREATE TABLE IF NOT EXISTS CoinFormats (
    versionNum TEXT,
    prefix TEXT,
    bgfile TEXT,
    name TEXT
);
''')

con.commit()
con.close()
print("Database initialized with tables: keys, Settings, CoinFormats.")
