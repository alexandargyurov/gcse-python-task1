import os
import time
import csv
import random
import sqlite3

from resources.login import Validation

class Quiz:
    def __init__(self, quiz, current_user):
        self.data = []
        self.total_score = 5
        self.score = 0
        self.percentage = 0
        self.grade = ""
        self.attempts = 0 # get the amount of times they have done it
        self.quiz = quiz
        self.current_user = current_user
        self.quiz_start = False
        
    def get_database(self):
        connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
        cur = connection.cursor()
        
        quiz_attempts = self.quiz.lower() + "_quiz_attempts"
        cur.execute("SELECT " + quiz_attempts + " FROM accounts WHERE username = (?)", (self.current_user,))
        attempts = cur.fetchone()
        if attempts == type(None):
            self.attempts = 0
        else:
            self.attempts = attempts[0]
            
        cur.close()
        
    def get_questions(self):

        quiz_to_get = self.quiz.lower() + "_q.csv"

        with open("resources/quizzes/data/" + quiz_to_get, "r") as f: # opens the csv file called "database.csv" and writes to it
            reader = csv.reader(f)
            self.data = list(reader) # reads the data from csv file

    def quiz_format(self):
        import sys
        print("----------" + self.quiz + " Quiz----------\n") # make it so it is public and not static

        print("You are now entering the " + self.quiz  + " Quiz.\nThe test is out of 5 questions.")
        print("You have attempted this Quiz " + str(self.attempts) + " times.")
        print("\nYou will be required to input a letter which represents the answer. \n\nPlease choose carefully as this will be your final answer.")

        enter = input("\nDo you wish to continue? [Y/N]   ").lower()
        os.system('cls')
        
        if enter == "y":
            self.quiz_start = True
            difficulty = input("\nPlease choose your difficulty:\n [EASY/MEDIUM/HARD] \nDefualt: Easy\n\nDiffuculty: ").lower()
            os.system('cls')
            for noQ in range(0, len(self.data)):

                if difficulty == "easy":
                    noQuestions = 4

                    choices_availblilty = [1,2,3,4]
                    letter_availblilty = ['A','B','C','D']

                elif difficulty == "medium":
                    noQuestions = 5

                    choices_availblilty = [1,2,3,4,5]
                    letter_availblilty = ['A','B','C','D','E']

                elif difficulty == "hard":
                    noQuestions = 6

                    choices_availblilty = [1,2,3,4,5,6]
                    letter_availblilty = ['A','B','C','D','E','F']
                else:
                    noQuestions = 4

                    choices_availblilty = [1,2,3,4]
                    letter_availblilty = ['A','B','C','D']
                    

                print("Question " + str(noQ) + ":\n" + str(self.data[noQ][0]))

                for x in range(0, noQuestions):
                    y = random.choice(choices_availblilty)
                    choices_availblilty.remove(y)
                    if self.data[noQ][y] == self.data[noQ][1]:
                        correct_answer = letter_availblilty[x]

                    print("[" + letter_availblilty[x] + "]. " + self.data[noQ][y])

                    x = x + 1

                answer = input("Please choose the correct answer: ")

                if answer == correct_answer:
                    print("Correct!\n")
                    self.score = self.score + 1
                else:
                    print("Incorrect!\n")
        elif enter == "n":
            self.quiz_start = False
            print("Returning to Main Menu..")               
            time.sleep(1)

    def finalise_score(self):
        self.percentage = (self.score / self.total_score) * 100
            
        if self.percentage <= 20:
            self.grade = "F"
        elif 20 < self.percentage <= 30:
            self.grade = "D"
        elif 30 < self.percentage <= 40:
            self.grade = "C"
        elif 40 < self.percentage <= 75:
            self.grade = "B"
        elif 75 < self.percentage <= 90:
            self.grade = "A"
        elif 90 < self.percentage <= 100:
            self.grade = "A*"

        print("Congratulations! You have now completed the " + self.quiz + " Quiz!\nTotal Score: " + str(self.score) + "\nPercentage: " + str(self.percentage) + "\nGrade: " + str(self.grade))
        input()
        os.system('cls')
        
    def update_database(self):        
        connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
        cur = connection.cursor()
        
        quiz_db_name = self.quiz+"_quiz_stats"
        
        quiz_score = self.quiz+"_quiz_score"
        quiz_percentage = self.quiz+"_quiz_percentage"
        quiz_grade = self.quiz+"_quiz_grade"
        quiz_attempts = self.quiz+"_quiz_attempts"
        
        attempts = self.attempts + 1
        
        cur.execute("UPDATE accounts SET "+quiz_score+" = (?) WHERE name = (?)", (self.score, self.current_user))
        cur.execute("UPDATE accounts SET "+quiz_percentage+" = (?) WHERE name = (?)", (self.percentage, self.current_user))
        cur.execute("UPDATE accounts SET "+quiz_grade+" = (?) WHERE name = (?)", (self.grade, self.current_user))
        cur.execute("UPDATE accounts SET "+quiz_attempts+" = (?) WHERE name = (?)", (attempts, self.current_user))
        connection.commit()
        
        cur.execute("SELECT AVG("+quiz_score+") FROM accounts")
        average_quiz_score = cur.fetchone()
        average_quiz_score = round(average_quiz_score[0],1) # rounds the value to 1 decimal place
        connection.commit()
        
        cur.execute("SELECT AVG("+quiz_percentage+") FROM accounts")
        average_quiz_percentage = cur.fetchone()
        average_quiz_percentage = round(average_quiz_percentage[0],1) # rounds the value to 1 decimal place
        connection.commit()
        
        cur.execute("SELECT AVG("+quiz_percentage+") FROM accounts")
        average_quiz_percentage = cur.fetchone()
        average_quiz_percentage = round(average_quiz_percentage[0],1)
        connection.commit()
        
        cur.execute("SELECT AVG("+quiz_grade+") FROM accounts")
        average_quiz_grade = cur.fetchone()
        average_quiz_grade = round(average_quiz_grade[0],1)
        connection.commit()
        
        cur.execute("SELECT TOTAL("+quiz_attempts+") FROM accounts")
        quiz_attempts = cur.fetchone()
        quiz_attempts = int(quiz_attempts[0])
        connection.commit()
        
        cur.execute("UPDATE "+quiz_db_name+" SET average_score = (?)", (average_quiz_score,))
        cur.execute("UPDATE "+quiz_db_name+" SET average_percentage = (?)", (average_quiz_percentage,))
        cur.execute("UPDATE "+quiz_db_name+" SET attempted_times = (?)", (quiz_attempts,))
        
        connection.commit()
        cur.close()
