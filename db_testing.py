import sqlite3


connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
c = connection.cursor()

c.execute("UPDATE accounts SET quiz_1 = '2' WHERE name = 'Lee'")
connection.commit()
