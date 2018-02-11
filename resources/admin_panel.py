import os
import sqlite3
import time
import sys

from resources.validation import Validation

admin_menu_active = True

quiz1 = "Geography"
quiz2 = "Mathematics"
quiz3 = "History"

while admin_menu_active == True:   
    print("You are currently viewing the Admin Panel.")
    
    print("Please select an option below via their number: ")
    
    print(" [1] View Student Profile") # student profile contains things such as amount of times tried a quiz, all their complete quizzes, a total score, score grade and percentage of a quiz, their difficulty
    print(" [2] View Quiz Statistics") # outputs quiz average grade, average score, average diffiuclty, people who have done the quiz, highest score
    print(" [3] Add or Remove Admin Account\n")
    
    print(" [4] Logout\n")
    
    choice = input("Please select how you would like to proceed: ")
    
    ###################
    if choice == "1":
        os.system('cls')
        view = input("Search for User: [1]\nView all Users: [2]\nPick: ")
        if view == "2":
                os.system('cls')
                print("----------ALL STUDENT ACCOUNTS----------\n")
                for x in range(0, len(Validation.data)):
                    if Validation.data[x][8] == 0: # Checks if the account is an ADMIN account or STUDENT.
                        print(Validation.data[x][2])
                        x+=1
                    else:
                        x+=1
                        
                input("\nPress any button to return back.")
                os.system('cls')
        elif view == "1":
            user_search = input("[SEARCH] Username: ")
            for x in range(0, len(Validation.data)): # loop to go through the whole csv data and check the username
                if Validation.data[x][2].lower() == user_search.lower(): # makes the username lower to make sure it is not case sensitive
                    os.system('cls')
                    print("----------ACCOUNT DETAILS----------\n")
                    found_account = True
                else: # if the first row didn't match the username given, go to the next one
                    found_account = False
                    x = x + 1
                if found_account == True:
                        print("Name:" + str(Validation.data[x][0]) + "\n" + "Surname:" + str(Validation.data[x][1]) + "\n" + "Username:" + str(Validation.data[x][2]) + "\n" + "Password: ********\n\n")
                        print("----------QUIZ STATISITCS----------\n\n" + quiz1 + ": \n" + " Score: " + str(Validation.data[x][5]) + "\n" + " Percentage: " + str(Validation.data[x][6]) + "%\n" + " Grade: " + str(Validation.data[x][7]) + "\n Attempts: " + str(str(Validation.data[x][8])) + "\n\n")
                        print(quiz2 + ": \n" + " Score: " + str(Validation.data[x][9]) + "\n" + " Percentage: " + str(Validation.data[x][10]) + "%\n" + " Grade: " + str(Validation.data[x][11]) + "\n Attempts: " + str(str(Validation.data[x][12])) + "\n\n")
                        #print(quiz2 + ": \n" + " Score: " + str(Validation.data[x][9]) + "\n" + " Percentage: " + str(Validation.data[x][10]) + "%\n" + " Grade: " + str(Validation.data[x][11]) + "\n Attempts: " + str(str(Validation.data[x][12])) + "\n\n")
                        
                        input("\nPress any button to return back.")
                        os.system('cls')
        else:
            os.system('cls')
            print("Invalid - Error")
    ###################
    
    
    
    
    
    ###################
    elif choice == "2":
        os.system('cls')
        
        view = input("Choose Quiz: \n\n[1] " + quiz1 + "\n[2] " + quiz2 + "\n[3] " + quiz3 + "\n\nOption: ")
        if view == "1":
            os.system('cls')
            print("----------"+quiz1+" Statistics----------\n")
            
            quiz_db_name = quiz1.lower()+"_quiz_stats"
            
            connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
            cur = connection.cursor()
            
            cur.execute("SELECT * FROM {0}".format(quiz_db_name))
            data = cur.fetchall()
            print("Average Score: " + str(data[0][0]) + "\nAverage Percentage: " + str(data[0][1]) + "%" + "\nAttemped Time: " + str(data[0][2]))
            input("\n\nPress Enter to Return back to the Main Menu.")
            os.system('cls')
            
        elif view == "2":
            os.system('cls')
            print("----------"+quiz2+" Statistics----------\n")
            
            quiz_db_name = quiz2.lower()+"_quiz_stats"
            
            connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
            cur = connection.cursor()
            
            cur.execute("SELECT * FROM {0}".format(quiz_db_name))
            data = cur.fetchall()
            print("Average Score: " + str(data[0][0]) + "\nAverage Percentage: " + str(data[0][1]) + "%" + "\nAttemped Time: " + str(data[0][2]))
            input("\n\nPress Enter to Return back to the Main Menu.")
            os.system('cls')
            
        elif view == "3":
            os.system('cls')
            print("----------"+quiz3+" Statistics----------\n")
            
            quiz_db_name = quiz3.lower()+"_quiz_stats"
            
            connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
            cur = connection.cursor()
            
            cur.execute("SELECT * FROM {0}".format(quiz_db_name))
            data = cur.fetchall()
            print("Average Score: " + str(data[0][0]) + "\nAverage Percentage: " + str(data[0][1]) + "%" + "\nAttemped Time: " + str(data[0][2]))
            input("\n\nPress Enter to Return back to the Main Menu.")
            os.system('cls')
        else:
            os.system('cls')
            print("Invalid - Error")      
    ###############    
    
    
    
    
    ###############
    elif choice == "3":
        os.system('cls')
        choice_admin = input("Please choose from the options below: \n\n   [1] New Admin Account\n   [2] Existing User\n   [3] Remove Admin\n\nChoice: ")
        if choice_admin == "1":
            os.system('cls')
            first_name = input("Please type in the Admins first name: ") # string varible to hold their first name
            surname = input("Please type in the Admins surname: ") # string varible to hold their second name
            user = input("Please type in the Admins Custom Username: ")
    
            pass_match = False # this is to create a loop to confirm the passwords match
    
            while pass_match == False:
                new_password = input("Please type their new password: ") # user creates their password
                new_password_r = input("Please confirm their new password: ") # user has to confirm the password previsouly mentioned
    
                if new_password == new_password_r: # checks if the password is correct or not
                    pass_match = True # makes the boolean True to end the loop
                    
                    connection = sqlite3.connect("data\database.db")
                    cur = connection.cursor()
                    cur.execute("INSERT INTO accounts (name, surname, username, password, admin) VALUES (?,?,?,?,1)",
                    (first_name, surname, user.lower(), new_password))
                    connection.commit()
                    cur.close()
        
                    print("New Admin Account Created \nUsername: " + user) # displayes their new generated username
                    time.sleep(1)
                    os.system('cls')
                else:
                    print("Passwords do not match, please try again. ") # displays error and asks to type their password in again
                    pass_match = False # keeps the loop going.
        elif choice_admin == '2':
            os.system('cls')
            user_search = input("[SEARCH] Username to Add: ")
            for x in range(0, len(Validation.data)): # loop to go through the whole csv data and check the username
                if Validation.data[x][2].lower() == user_search.lower(): # makes the username lower to make sure it is not case sensitive
                    os.system('cls')
                    print("----------ACCOUNT DETAILS----------\n")
                    found_account = True
                else:
                    found_account = False
                    x = x + 1   # if the first row didn't match the username given, go to the next one
                if found_account == True:
                        print("Name:" + str(Validation.data[x][0]) + "\n" + "Surname:" + str(Validation.data[x][1]) + "\n" + "Username:" + str(Validation.data[x][2]) + "\n" + "Password: ********\n")
                        add = input("\nDo you wish to add this user to the Administrator list? [Y/N] \n Note: THIS WILL GIVE THEM FULL ACCESS TO THE ADMIN PANEL! \n Choice: ")
                        if add == "Y":
    
                            connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
                            cur = connection.cursor()
                            cur.execute("UPDATE accounts SET admin = 1 WHERE username = (?)", (user_search.lower(),))
                            connection.commit()
                            cur.close()
    
                            print("User: " + Validation.data[x][2] + " has been added to the admin list.")
    
                        elif add == "N":
                            print("User has NOT been added to the Administrator list.\n Returning to the Main Menu.")
                            time.sleep(2)
                            os.system('cls')
        elif choice_admin == '3':
            os.system('cls')
            user_search = input("[SEARCH] Username to Remove: ")
            for x in range(0, len(Validation.data)): # loop to go through the whole csv data and check the username
                if Validation.data[x][2].lower() == user_search.lower(): # makes the username lower to make sure it is not case sensitive
                    os.system('cls')
                    print("----------ACCOUNT DETAILS----------\n")
                    found_account = True
                else:
                    found_account = False
                    x = x + 1   # if the first row didn't match the username given, go to the next one
                if found_account == True:
                        print("Name:" + str(Validation.data[x][0]) + "\n" + "Surname:" + str(Validation.data[x][1]) + "\n" + "Username:" + str(Validation.data[x][2]) + "\n" + "Password: ********" + "\n\n----------QUIZ STATISITCS----------\n\n" + quiz1 + ": " + str(Validation.data[x][4]) + "\n" + quiz2 + ": " + str(Validation.data[x][5]) + "\n" + quiz3 + ": " + str(Validation.data[x][6]))
                        add = input("\nDo you wish to REMOVE this user to the Administrator list? [Y/N] \n Note: THIS WILL REMOVE FULL ACCESS TO THE ADMIN PANEL AND MAKE THEM A STUDENT ACCOUNT! \n Choice: ")
                        if add == "Y":
    
                            connection = sqlite3.connect("D:\Computer Science\gcse-python-task\data\database.db")
                            cur = connection.cursor()
    
                            cur.execute("UPDATE accounts SET admin = 0 WHERE username = (?)", (user_search.lower(),))
                            connection.commit()
                            connection.close()
    
                            print("User: " + Validation.data[x][2] + " has been removed to the admin list.")
    
                        elif add == "N":
                            print("User has NOT been removed to the Administrator list.\n Returning to the Main Menu.")
                            time.sleep(2)
                        os.system('cls')
    #################
    
    
    
    
    #################
    elif choice == "4":
        os.system('cls')
        Validation.login_success = False # Doesn't actually work, still loops back. 
        menu_active = False # Solution: Temp use sys.exit(0)
        print("You have successfully logged off.")
        time.sleep(1)
        sys.exit(0)
    
    else:
        os.system('cls')
        print("Invalid - Please Input a Correct Value")
        time.sleep(1)
        os.system('cls')
    ##################
    