import datetime
import re
from validations import *
def menu():
     choose=int(input("welcome to our app please choose your input.....\n1-registration\n2-login\n--->"))
     if choose==1:
          register()
     elif choose==2:
          login()
     else:
          print("invalid,back to menu...")
          menu()

def project_menu():
     choose=int(input("1-create project\n2-view projects\n3-edit project\n4-delete project\n5- back to main menu--->"))
     if choose==1:
          create_project()
     elif choose==2:
          a_file = open("projects.txt")
          lines = a_file.readlines()
          for line in lines:
               print(line)
          project_menu()
     elif choose==3:
          edit_project()
     elif choose==4:
          delete_project()
     elif choose==5:
          menu()
     else:
          print("invalid data...")



def register():
     first_name = input("please enter your first name: ").strip().lower()
     last_name = input("please enter your last name: ").strip().lower()
     #check if email is valid using regix
     while True:
          regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
          email = input("plese enter you email: ").strip().lower()
          if(re.fullmatch(regex, email)):
               break
          else:
               print("invalid email please enter a valid email address..")     
     #check if password is confirms
     while True:
          password = input("please enter your password: ")
          password_confirm = input("please confirm your password: ")
          if password == password_confirm:
               print("password match fine")
               break
          else:
               print("password doesn't match enter a new password")
     #check if phone number is validated against Egyptian phone numbers 
     while True:
          mobile=(input("please enter your phone number:"))
          if mobile.startswith("01") and len(mobile)==11:
               print("phone number is valid")
               break
          else:
               print("worng phone number please enter an egyptian number")
     users_data=open("login_info.txt","a")
     users_data.write(f"{email}:{password}:{first_name}.{last_name}:{mobile}\n")        
     print("------------registration success -----------")
     users_data.close()
     menu()




def login():
     email_login=input("please enter your email to login: ")
     password_login = input("please enter your login password: ")
     stored_data = open("login_info.txt","r")
     user_info=stored_data.read()
     check_info=f"{email_login}:{password_login}"
     if check_info in user_info:
          print("=============================================")
          print("login successfully")

     else:
          print("email or password is wrong please try again...")
          login()
     project_menu()





def create_project():
     title=input("insert project title: ")
     details=input("write the details about this project: ")
     total_target=float(input("enter total targeted money for this project:"))
     start_project= date_check()[0]
     end_project=date_check()[1]
     project_data=open("projects.txt",'a')
     project_data.write(f"{title}:{details}:{total_target}:{start_project}:{end_project}\n") 
     project_data.close()
     print("project created successfully")
     project_menu()


def edit_project():
     x=input("please enter title of project you want to edit:")
     with open("projects.txt", "r") as f:
          lines = f.readlines()
     with open("projects.txt", "w") as f:
          for line in lines:
               if not line.startswith(x):
                    f.write(line)
     f.close()
     create_project()
     


def delete_project():
     x=input("please enter title of project you want to delete:")
     with open("projects.txt", "r") as f:
          lines = f.readlines()
     with open("projects.txt", "w") as f:
          for line in lines:
               if not line.startswith(x):
                    f.write(line)
               print("project deleted succesfully")
     f.close()
     project_menu()





menu()



