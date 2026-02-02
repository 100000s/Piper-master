import sqlite3

con = sqlite3.connect('settings.db3')
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print('Tables in settings.db3:', tables)
if any('keys' in t for t in tables):
    print('The keys table exists.')
else:
    print('The keys table does NOT exist.')
con.close()
