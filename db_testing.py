import sqlite3

conn = sqlite3.connect("data\database.db")
c = conn.cursor()

c.execute("SELECT username, password FROM accounts")
data = c.fetchall()

print(data[0][1])