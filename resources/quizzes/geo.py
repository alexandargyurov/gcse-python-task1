import sys
import time
import csv
import random
import sqlite3

class Quiz:
    def __init__(self):
        self.data = []
        self.difficulty = ""
        self.total_score = 5
        self.score = 0
        self.percentage = 0
        self.grade = ""

    def get_questions(self):
        with open('data\geo_q.csv', 'r') as f: # opens the csv file called "database.csv" and writes to it
            reader = csv.reader(f)
            self.data = list(reader) # reads the data from csv file

    def quiz_format(self):
        print("----------QUIZ NAME----------\n") # make it so it is public and not static


        for noQ in range(0, len(self.data)):

            if self.difficulty == "easy":
                noQuestions = 4

                choices_availblilty = [1,2,3,4]
                letter_availblilty = ['A','B','C','D']

            elif self.difficulty == "medium":
                noQuestions = 5

                choices_availblilty = [1,2,3,4,5]
                letter_availblilty = ['A','B','C','D','E']

            elif self.difficulty == "hard":
                noQuestions = 6

                choices_availblilty = [1,2,3,4,5,6]
                letter_availblilty = ['A','B','C','D','E','F']

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



    def finalise_score(self):
        self.percentage = (self.score / self.total_score) * 100

        if self.percentage <= 10:
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

        print("You have now completed the" + " GEOGRAPHY QUIZ" + "\nTotal Score: " + str(self.score) + "\nPercentage: " + str(self.percentage) + "\nGrade: " + str(self.grade))

    def update_database(self):
        connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
        cur = connection.cursor()

        cur.execute("UPDATE accounts SET quiz_1 = (?) WHERE name = 'Lee'", (self.score,))
        connection.commit()
        connection.close()

    def geography(self):
        import sys
        print("You are now entering the Geography Test.\nThe test is out of 5 questions.")
        print("You will be required to input a letter which represents the answer. \nPlease choose carefully as this will be your final answer.")

        enter = input("Do you wish to continue? [Y/N]   ").lower()

        if enter == "y" or "yes":
            self.difficulty = input("Please choose your difficulty: [EASY/MEDIUM/HARD] \nDiffuculty: ").lower()

            self.quiz_format()


Quiz = Quiz() #this defines that the "Validation" is using the "Validation()" class
Quiz.get_questions()
Quiz.geography()
Quiz.finalise_score()
Quiz.update_database()