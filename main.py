import os
import time
import sqlite3

from resources.login import Validation

main_menu_active = True
    
while Validation.login_success == True:
    os.system('cls')

    while main_menu_active == True:
        print("Welcome", Validation.current_user, "to the General Knowledge Quiz!")
        if Validation.admin_account == True:
            import admin_panel
        else:
            import student_panel
            