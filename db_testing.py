import sqlite3
quiz_score = "geography_quiz_score"
quiz_percentage = "geography_quiz_percentage"
quiz_grade = "geography_quiz_grade"
quiz_attempts = "geography_quiz_attempts"

score = 5
percentage = 70
grade = "B"
user_name = "test"
attempts = 5

connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
cur = connection.cursor()
print(quiz_score)
cur.execute("UPDATE accounts SET "+quiz_score+" = (?) WHERE name = (?)", (score, user_name))
cur.execute("UPDATE accounts SET "+quiz_percentage+" = (?) WHERE name = (?)", (percentage, user_name))
cur.execute("UPDATE accounts SET "+quiz_grade+" = (?) WHERE name = (?)", (grade, user_name))
cur.execute("UPDATE accounts SET "+quiz_attempts+" = (?) WHERE name = (?)", (attempts, user_name))


connection.commit()
connection.close()