import sqlite3
import time
import os

class Validation: # new class called Validation
    def __init__(self):

        self.new_user = ""
        self.new_pass = ""

        self.current_user = ""                      
        self.current_username = ""
        
        self.data = []
        self.admin_account = False

        self.username_match = False
        self.password_match = False
        self.login_success = False

    def read_database(self): # this reads the file with the usernames and passwords
        
        connection = sqlite3.connect("data\database.db")
        cur = connection.cursor()
        cur.execute("SELECT * FROM accounts")
        self.data = cur.fetchall()      
        cur.close()
        
    def create_username(self, name, surname, password): # this function creates a new user with the information provided
        self.new_user = surname[0] + name[0] + name[1] + name[2] + time.strftime("%y") 
        
        connection = sqlite3.connect("data\database.db")
        cur = connection.cursor()
        cur.execute("INSERT INTO accounts (name, surname, username, password) VALUES (?,?,?,?)",
        (name, surname, self.new_user.lower(), password))
        connection.commit()
        cur.close()
        
        print("New Account Created \nYour new username is: " + str(self.new_user)) # displayes their new generated username
        input("Press Enter to Return back to the Main Menu.")
        os.system('cls')

    def check_account(self, username, password): # this checks the username and sees if it matches a username from the database we read

        for x in range(0, len(self.data)): # loop to go through the whole sqlite3 database list and check the username
            if self.data[x][2].lower() == username.lower(): # makes the username lower to make sure it is not case sensitive

                if self.data[x][3] == password:
                    self.username_match = True # makes the varible true
                    self.password_match = True
                    
                    self.current_username = self.data[x][2]
                    self.current_user = self.data[x][0]
                    

                    if self.data[x][4] == 1:
                        self.admin_account = True # sets value to True so later I can use it to show more options for the admin
                                                                                                               # ## ## ## CHANGES ## ## ##
            else: # if the first row didn't match the username given, go to the next one
                x = x + 1



    def display_login_true(self): # if everything checks out, return a True value and proceed with the rest of the program
        if self.username_match and self.password_match == True: # if both varibles are equal to true then make login_success True
            active = False
            self.login_success = True
        else:
            print("Invalid Username or Password") # displays an error if something does not match.
            time.sleep(1)

Validation = Validation() # this defines that the "Validation" is using the "Validation()" class
