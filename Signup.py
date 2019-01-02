from tkinter import *
import os
from Dashboard import *

#def delete2():
#    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def homepage():
    global home_screen
    home_screen=Toplevel(screen)
    home_screen.title("Welcome To Test Page")
    home_screen.geometry("400x300")
    Label(home_screen,text="Welcome To Test Page").pack()
    Label(home_screen, text="\n").pack()
    Label(home_screen, text="Click on Start Test Button").pack()
    Button(home_screen,text="Start Test",command=run_test(questions)).pack()

def login_sucess():
    homepage()


   # global screen3
   # screen3=Toplevel(screen)
   # screen3.title("Successful Login")
   # screen3.geometry("150x100")
   # Label(screen3,text="Successful Login").pack()
   # Button(screen3,text="ok",command=delete2).pack()

def wrong_pass():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("Wrong Password")
    screen4.geometry("150x100")
    Label(screen4,text="Wrong Password Entered !\n").pack()
    Button(screen4,text="Ok",command=delete3).pack()


def invalid_user():
   global screen5
   screen5=Toplevel(screen)
   screen5.title("User Not Found")
   screen5.geometry("150x100")
   Label(screen5,text="No Such User Exist .").pack()
   Button(screen5,text="Ok",command=delete4).pack()



def sign_user():

    uname_info=uname.get()
    password_info=password.get()

    file= open(uname_info,"w")
    file.write(uname_info+"\n")
    file.write(password_info)
    file.close()

    uname_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text="Registration Successful .",fg="green",font=("calibri",12)).pack()


def login():


    global screen2,uname_verify, password_verify, uname_entry1,password_entry1
    screen2=Toplevel(screen)
    screen2.title("LOG_IN")
    screen2.geometry("300x250")

    Label(screen2,text="Please Enter Log In Credentials below .")
    Label(screen2,text="").pack()


    uname_verify=StringVar()
    password_verify=StringVar()


    Label(screen2,text="USER_NAME * ").pack()
    uname_entry1=Entry(screen2,textvariable=uname_verify)
    uname_entry1.pack()
    Label(screen2,text="").pack()



    Label(screen2,text="PASSWORD * :").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()

    Button(screen2,text="Log In",width=10,height=1,command=login_verify).pack()



def login_verify():

    uname1=uname_verify.get()
    password1=password_verify.get()

    uname_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files=os.listdir()

    if uname1 in list_of_files:
        file1=open(uname1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            wrong_pass()
    else:
        invalid_user()



def log_in():
    print("Log In Session Started")


def sign_up():

    global screen1
    screen1=Toplevel(screen)
    screen1.title("Sign Up")
    screen1.geometry("300x250")

    global uname,password, uname_entry,password_entry
    uname=StringVar()
    password=StringVar()

    Label(screen1,text="Please Enter Deatils Below :").pack()
    Label(text="").pack()

    Label(screen1,text="User Name *").pack()
    uname_entry=Entry(screen1,textvariable=uname)
    uname_entry.pack()

    Label(screen1,text="Password *").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()

    Label(text="").pack()

    Button(screen1,text="Register",width="10",height="1",command=sign_user).pack()






def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Project MCQ")
    Label(text="Welcome To Project MCQ",bg="Orange",width="300",height="2",font=("Calibri",14)).pack()
    Label(text="").pack()
    Button(text="Signup",width="30",height="2",command=sign_up).pack()
    Label(text="").pack()
    Button(text="Log in",width="30 ",height="2",command=login).pack()



    screen.mainloop()

main_screen()
