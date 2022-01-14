"""
users should be able to log in and log out,the system also checks if users are logged in
there are three parts
    -register users,-log in users,-main loop to run the program
"""
import csv
from getpass import getpass#hides the password
#from Ipython.display import clear_ouput

#HANDLING USER REGISTRATION
def register_user():
    with open("users.csv",mode="a",newline="") as user_registration:
        writer=csv.writer(user_registration,delimiter=",")
        print("to register,please enter your information")
        user_email=input("enter your email:")
        user_password=getpass("enter your password:")
        password_confirm=getpass("re-enter your password:")
        #clear_output()
        if user_password==password_confirm :#checking if email is valid-add code
            writer.writerow([user_email,user_password])
            print("you are now registered")
        else:
            print("password dont match or you entered an invalid email.try again:")
            register_user()
#register_user()

#HANDLING USER LOG IN
def login_user():
    print("to login please enter your details:")
    user_email=input("please enter your email:")
    user_password=getpass("please enter your password")
    #clear_ouput()
    with open("users.csv",mode="r")as log_user:
        reader=csv.reader(log_user,delimiter=",")
        for login_row in reader:
            if login_row==[user_email,user_password]:#it checks row by row till it finds a match
                print("you are now logged in")
                return True
            else:
                print("incorrect details,try again")
                #login_user()
                return False
#MAIN LOOP
ACtive_user=True
logged_in=False
while ACtive_user:
    if logged_in:
        print("1.log out\n2.quit")
    else:
        print("1.login\n2.register\n3.quit")
    user_choice=input("what would you like to do:").lower()
    #clear_ouput()
    if user_choice=="register" and logged_in==False:
        register_user()
    elif user_choice=="login" and logged_in==False:
        logged_in=login_user()
    elif user_choice=="quit":
        ACtive_user=False
        print("thank you for using our software")
    elif user_choice=="log out" and logged_in==True:
        logged_in=False
        print("you are now logged out")
    else:
        print("sorry try again")