import time
import os

from resources.validation import Validation

menu_active = True

while menu_active == True:
    os.system("cls") 
    choice = input("Register | Login\n ").lower() # this allows the user to either Login or Register (.lower() makes all the characters login)
    

    if choice == "login": # if the user inputed "login"
        os.system('cls')
        user = input("Username: ")
        password = input("Password: ")
    
        Validation.read_database() # this goes to the class "Validation()" and calls the function "read_database()"
    
        Validation.check_account(user, password) # after it read the csv file, it will check if the username provided matches a username in the csv file.
        Validation.display_login_true() # checks the end result of if the user has a correct user name or password
        
        if Validation.login_success == False:
            menu_active = True
        else:
            menu_active = False
        
    elif choice == "register": # if the user inputed "register"
        os.system('cls')
        first_name = input("Please type in your first name: ") # string varible to hold their first name
        surname = input("Please type in your surname: ") # string varible to hold their second name
    
        pass_match = False # this is to create a loop to confirm the passwords match
    
        while pass_match == False:
            new_password = input("Please type in your new password: ") # user creates their password
            new_password_r = input("Please confirm your new password: ") # user has to confirm the password previsouly mentioned
    
            if new_password == new_password_r: # checks if the password is correct or not
                pass_match = True # makes the boolean True to end the loop
                Validation.create_username(first_name, surname, new_password) # calls the function from Validation Class to create a new user with the information provided
    
            else:
                print("Passwords do not match, please try again. ") # displays error and asks to type their password in again
                pass_match = False # keeps the loop going.
    else:
        print("Error - Invalid")
        time.sleep(1)