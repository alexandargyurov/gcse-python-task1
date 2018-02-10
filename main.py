import os
import time

print("Welcome to the General Knowledge Quiz")
from resources.login import Validation

tests = 0 # PLACEOLDER
quiz1 = "Geography"
quiz2 = "Mathmatics"
quiz3 = "History"

while Validation.login_success == True:
    os.system('cls')
    menu_active = True
    while menu_active == True:
        print("Welcome", Validation.current_user, "to the General Knowledge Quiz!")
        if Validation.admin_account == True:
            print("You are currently viewing the Admin Panel.")

            print("Please select an option below via their number: ")

            print(" [1] View Student Profile") # student profile contains things such as amount of times tried a quiz, all their complete quizzes, a total score, score grade and percentage of a quiz, their difficulty
            print(" [2] View Quiz Statistics") # outputs quiz average grade, average score, average diffiuclty, people who have done the quiz, highest score
            print(" [3] Add Admin Account\n")

            print(" [4] Logout\n")

            choice = input("Please select how you would like to proceed: ")


            if choice == "1":
                os.system('cls')
                view = input("Search for User: [1]\nView all Users: [2]\nPick: ")
                if view == "2":
                        os.system('cls')
                        print("----------ALL STUDENT ACCOUNTS----------\n")
                        for x in range(0, len(Validation.data)):
                            if Validation.data[x][4] == "0": # Checks if the account is an ADMIN account or STUDENT.
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
                                print("Name:" + Validation.data[x][0] + "\n" + "Surname:" + Validation.data[x][1] + "\n" + "Username:" + Validation.data[x][2] + "\n" + "Password: ********" + "\n\n----------QUIZ STATISITCS----------\n\n" + quiz1 + ": " + Validation.data[x][5] + "\n" + quiz2 + ": " + Validation.data[x][6] + "\n" + quiz3 + ": " + Validation.data[x][7])
                                input("\nPress any button to return back.")
                                os.system('cls')
                else:
                    os.system('cls')
                    print("Invalid - Error")



            elif choice == "2":
                os.system('cls')
                print("NOT YET ADDED GO AWAY") # PLACEHOLDER
            elif choice == "3":
                os.system('cls')
                choice_admin = input("Please choose from the options below: \n\n   [1] New Admin Account\n   [2] Existing User\n\nChoice: ")
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
                            Validation.create_admim(first_name, surname, user, new_password) # calls the function from Validation Class to create a new user with the information provided

                        else:
                            print("Passwords do not match, please try again. ") # displays error and asks to type their password in again
                            pass_match = False # keeps the loop going.
                elif choice_admin == '2':
                    user_search = input("[SEARCH] Username to Add: ")
                    for x in range(0, len(Validation.data)): # loop to go through the whole csv data and check the username
                        if Validation.data[x][2].lower() == user_search.lower(): # makes the username lower to make sure it is not case sensitive
                            os.system('cls')
                            print("----------ACCOUNT DETAILS----------\n")
                            found_account = True
                        else: # if the first row didn't match the username given, go to the next one
                            found_account = False
                            x = x + 1
                        if found_account == True:
                                print("Name:" + Validation.data[x][0] + "\n" + "Surname:" + Validation.data[x][1] + "\n" + "Username:" + Validation.data[x][2] + "\n" + "Password: ********" + "\n\n----------QUIZ STATISITCS----------\n\n" + quiz1 + ": " + Validation.data[x][5] + "\n" + quiz2 + ": " + Validation.data[x][6] + "\n" + quiz3 + ": " + Validation.data[x][7])
                                add = input("\nDo you wish to add this user to the Administrator list? [Y/N] \n Note: THIS WILL GIVE THEM FULL ACCESS TO THE ADMIN PANEL! \n Choice: ")
                                if add == "Y":
                                    admin_status = 1
                                    with open('data\database.csv', 'a') as f: # writes the new user to the csv file database
                                        test_1_score = "NOT ATTEMPTED"
                                        test_2_score = "NOT ATTEMPTED"
                                        test_3_score = "NOT ATTEMPTED"
                                        f.write( Validation.data[x][0] + "," +  Validation.data[x][1] + "," +  Validation.data[x][2] + ',' +  Validation.data[x][3] + ',' + str(admin_status) + "," + test_1_score + ',' + test_2_score + ',' + test_3_score + '\n')
                                    print("User: " + Validation.data[x][2] + " has been added to the admin list.")

                                elif add == "N":
                                    print("User has NOT been added to the Adminstrator list.\n Returning to the Main Menu.")
                                    time.sleep(2)
                                os.system('cls')

            elif choice == "4":
                os.system('cls')
                Validation.login_success = False
                menu_active = False
                print("You have sucesfully logged off.")
                time.sleep(2)

            else:
                os.system('cls')
                print("Invalid - Please Input a Correct Value")
                time.sleep(2)
                os.system('cls')
                Validation.login_success = False
        else:
            print("You have completed a total of:", tests, "quizzes.")
            print("Please see below which quizzes have been assigned below. \n")

            print(quiz1 + "\n" + quiz2 + "\n" + quiz3)

            choice = input("\nPlease input which Quiz you would like to do.\n(To view statistics, please type 'Stats' to view your previous quiz resualts. )\nChoose: ")

            if choice.lower() == "geograpghy":
                print("go to geo quiz") # PLACEHOLDER
                input()
            elif choice.lower() == "math" or "mathmatics" or "maths":
                print("go to math quiz") # PLACEHOLDER
                input()
            elif choice.lower() == "history":
                print("go to history quiz") # PLACEHOLDER
                input()
            else:
                print("Invalid Quiz Name")
                input()
                # loop back
