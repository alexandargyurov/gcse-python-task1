quiz_db_name = "geography_quiz_stats"

quiz_score = "geography_quiz_score"
quiz_percentage = "geography_quiz_percentage"
quiz_grade = "geography_quiz_grade"
quiz_attempts = "geography_quiz_attempts"

connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
cur = connection.cursor()

cur.execute("SELECT AVG("+quiz_score+") FROM accounts")
average_quiz_score = cur.fetchone()
average_quiz_score = round(average_quiz_score[0],1) # rounds the value to 1 decimal place

cur.execute("SELECT AVG("+quiz_percentage+") FROM accounts")
average_quiz_percentage = cur.fetchone()
average_quiz_percentage = round(average_quiz_percentage[0],1) # rounds the value to 1 decimal place

cur.execute("SELECT AVG("+quiz_percentage+") FROM accounts")
average_quiz_percentage = cur.fetchone()
average_quiz_percentage = round(average_quiz_percentage[0],1)

cur.execute("SELECT AVG("+quiz_grade+") FROM accounts")
average_quiz_grade = cur.fetchone()
average_quiz_grade = round(average_quiz_grade[0],1)

cur.execute("SELECT TOTAL("+quiz_attempts+") FROM accounts")
quiz_attempts = cur.fetchone()
quiz_attempts = int(quiz_attempts[0])

cur.execute("UPDATE "+quiz_db_name+" SET average_score = (?)", (average_quiz_score,))
cur.execute("UPDATE "+quiz_db_name+" SET average_percentage = (?)", (average_quiz_percentage,))
cur.execute("UPDATE "+quiz_db_name+" SET average_grade = (?)", (average_quiz_grade,))
cur.execute("UPDATE "+quiz_db_name+" SET attempted_times = (?)", (quiz_attempts,))

connection.commit()
connection.close()