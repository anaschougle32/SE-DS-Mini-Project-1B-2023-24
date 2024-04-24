from tkinter import *
from subprocess import call
import tkinter as tk
from tkinter import Frame

root = Tk()
root.title("Field Determination")
root.geometry("735x490")
root.resizable(0, 0)
root.configure(background="white")

def User():
    print("select user")
    root.destroy()

    call(['python', 'login.py'])

def Admin():
    print("select admin")
    root.destroy()

    call(['python', 'loginad.py'])

userbtn = Button(root, text="User", width=15, height=2, bg="blue", fg="white", font="times 15 bold", command=User)
userbtn.place(x=290, y=150)

adminbtn = Button(root, text="Admin", width=15, height=2, bg="blue", fg="white", font="times 15 bold", command=Admin)
adminbtn.place(x=290, y=250)

root.mainloop()
