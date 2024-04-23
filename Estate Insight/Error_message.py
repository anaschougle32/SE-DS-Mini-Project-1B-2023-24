from tkinter import *
from tkinter import ttk
import tkinter as tk


class Error_message:
    def __init__(self, root):
        self.root=root
# setting up the app
        root.title("Ouestion")
        root.resizable(False, False)

        font_info = ("Arial", 15, "bold")

        # app color
        root.configure(bg='white')

        # setting up geometry for app
        window_width = 300
        window_height = 200

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # setting up icon for window title
        icon = PhotoImage(file='Images/warning.png')
        root.iconphoto(True, icon)

        #top heading
        head = Label(root, text="To enjoy the features!!", font=('Bold',17), bg='white')
        head.place(relx=0.11, rely=0.11)

        #signin
        sign_in = Label(root, text="SignIn first", font=('Bold',14), bg='white')
        sign_in.place(relx=0.24, rely=0.4)
        sign_butt = Button(text='SignIn', bg='#B31312', fg='white', font=('Bold',10),command=self.signup)
        sign_butt.place(relx=0.56, rely=0.4)

        #Login
        log_in = Label(root, text="Already have an account?", font=('Microsoft YaHei UI Light',12), bg='white')
        log_in.place(relx=0.17, rely=0.6)
        log_butt = Button(root, text='LogIn', bg='#B31312', fg='white', font=('Bold',10),command=self.login)
        log_butt.place(relx=0.42, rely=0.75)

    def signup(self):
        self.root.destroy()
        import signup

    def login(self):
        self.root.destroy()
        import login
root = Tk()
obj=Error_message(root)
root.mainloop()
