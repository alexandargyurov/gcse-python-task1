import csv
import time
import sys
import os
import sqlite3

connection = sqlite3.connect("data\database.db")
c = connection.cursor()

class Validation: # new class called Validation
    def __init__(self):

        self.new_user = ""
        self.new_pass = ""

        self.current_user = ""                      # ## ## ## CHANGES ## ## ## #

        self.data = []
        self.admin_account = False                  # ## ## ## CHANGES ## ## ## #

        self.username_match = False
        self.password_match = False
        self.login_success = False

    def read_database(self): # this reads the file with the usernames and passwords
        c.execute("SELECT * FROM accounts")
        self.data = c.fetchall()

    def create_username(self, name, surname, password): # this function creates a new user with the information provided
        self.new_user = surname[0] + name[0] + name[1] + name[2] + time.strftime("%y")

        print("New Acount Created \nYour new username is: " + str(self.new_user)) # displayes their new generated username

        c.execute("INSERT INTO accounts (name, surname, username, password) VALUES (?,?,?,?)",
        (name, surname, self.new_user, password))
        connection.commit()
        c.close()

    def check_account(self, username, password): # this checks the username and sees if it matches a username from the database we read

        for x in range(0, len(self.data)): # loop to go through the whole sqlite3 database list and check the username
            if self.data[x][2].lower() == username.lower(): # makes the username lower to make sure it is not case sensitive

                if self.data[x][3] == password:
                    self.username_match = True # makes the varible true
                    self.password_match = True
                    self.current_user = self.data[x][0]

                    if self.data[x][7] == 1:
                        self.admin_account = True # sets value to True so later I can use it to show more options for the admin
                                                                                                               # ## ## ## CHANGES ## ## ##
            else: # if the first row didn't match the username given, go to the next one
                x = x + 1



    def display_login_true(self): # if everything checks out, return a True value and proceed with the rest of the program
        if self.username_match and self.password_match == True: # if both varibles are equal to true then make login_success True
            self.login_success = True
        else:
            print("Invalid Username or Password") # displays an error if something does not match.

    def create_admim(self, name, surname, user, password): # this function creates a new user with the information provided
        admin_status = 1

        with open('data\database.csv', 'a') as f: # writes the new user to the csv file database                                               # ## ## ## CHANGES ## ## ##
            f.write(name + "," + surname + "," + user + ',' + password + ',' + str(admin_status) + "," + test_1_score + ',' + test_2_score + ',' + test_3_score + '\n')                                                 # ## ## ## CHANGES ## ## ##

        print("New Acount Created \nYour new username is: " + str(self.new_user)) # displayes their new generated username
        input()


choice = input("Register | Login\n ").lower() # this allows the user to either Login or Register (.lower() makes all the characters login)
Validation = Validation() # this defines that the "Validation" is using the "Validation()" class

if choice == "login": # if the user inputed "login"
    os.system('cls')
    user = input("What is your username: ")
    password = input("What is your password: ")


    Validation.read_database() # this goes to the class "Validation()" and calls the function "read_database()"

    Validation.check_account(user, password) # after it read the csv file, it will check if the username provided matches a username in the csv file.
    Validation.display_login_true() # checks the end result of if the user has a correct user name or password

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