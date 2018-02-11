import sys
import os
import time

from resources.quizzes.quiz_format import Quiz
from resources.login import Validation
from fileinput import close

def start_quiz(quiz):
    os.system('cls')
    Quizz = Quiz(quiz, Validation.current_username) #this defines that the "Quiz" is using the "Quiz()" class from quiz_format.py file
    Quizz.get_database()
    
    Quizz.get_questions()
    Quizz.quiz_format()
    
    if Quizz.quiz_start == True:
        Quizz.finalise_score()
        Quizz.update_database()
        
 
quiz1 = "Geography"
quiz2 = "Mathematics"
quiz3 = "History"

quiz_select_menu_active = True

while quiz_select_menu_active == True:      
    print("Please see below which quizzes have been assigned below. \n")
    
    print("[1] " + quiz1 + "\n" + "[2] " + quiz2 + "\n" + "[3] " + quiz3 + "\n\n[4] Logout")
    
    choice = input("\nPlease input which Quiz you would like to do.\n\nOption: ")
    
    if choice.lower() == "1":
        start_quiz(quiz1)
        
    elif choice.lower() == "2":
        start_quiz(quiz2)
        
    elif choice.lower() == "3":
        os.system('cls')
        print("Function Disabled") # task only requires to test 2 subjects.
        time.sleep(1)
        os.system('cls')
        #start_quiz(quiz3)
    
    elif choice.lower() == "4":
        os.system('cls')
        
        Validation.login_success = False # This does not work for some reason.
        quiz_select_menu_active = False # Temp Solution: sys.exit(0)
        main_menu_active = False 
        
        print("You have successfully logged off.")
        time.sleep(1)
        
        sys.exit(0)
        
    else:
        os.system('cls')
        print("Invalid Input")
        time.sleep(1)
        os.system('cls')
        
