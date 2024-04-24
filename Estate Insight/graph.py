from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
import tkinter.font as tkFont
from io import BytesIO
import matplotlib.pyplot as plt  # Importing matplotlib's pyplot module
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class maininterface2:
    def __init__(self, root):
        self.root = root
        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 19, "bold")
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#22107031#',
            database='estateinsight'
        )
        # Create a cursor to execute SQL queries
        self.cursor = self.conn.cursor()
        one = Label(root,
                    text="EstateInsight",
                    bg="#B31312",
                    fg="white",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=1,
                    height=5)
        one.pack(fill=X, side=TOP)
        insertButt = Button(one,
                            text="Login",
                            bg="#B31312",
                            fg="white",
                            border=0,
                            activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=3, pady=2)
        insertButt = Button(one,
                            text="Sign Up",
                            bg="#B31312",
                            fg="white",
                            border=0,
                            activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=3, pady=2)

        # app color
        self.root.configure(bg='white')

        # setting up geometry for app
        window_width = 1000
        window_height = 660

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # setting up icon for window title
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)

        toolbar_font = ("Arial", 11)
        # setting up the toolbar for the app
        toolbar = Frame(root, bg="white", relief=GROOVE, bd=2, pady=4)

        printButt = Button(toolbar,
                           text="Home",
                           bg="#B31312",
                           border=1,
                           font=toolbar_font,
                           relief=RAISED,
                           fg="white",
                           command=self.home)
        printButt.pack(side=LEFT, padx=20, pady=2)
        insertButt = Button(toolbar,
                            text="Buy",
                            bg="white",
                            font=toolbar_font,
                            border=0,
                            command=self.buy)
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Sell",
                           bg="white",
                           font=toolbar_font,
                           border=0,
                           activebackground='#B67352', command=self.sell)

        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Rent",
                           bg="white",
                           font=toolbar_font,
                           border=0, activebackground='#B67352', command=self.rent)

        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Rent Upload",
                           bg="white",
                           font=toolbar_font,
                           border=0, command=self.rentup)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Land/Value Graph",
                           bg="white",
                           font=toolbar_font,
                           border=0)
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

        printButt = Button(toolbar,
                           text="Calculate EMI",
                           bg="white",
                           border=0,
                           font=toolbar_font,
                           command=self.emi)
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

       # left_frame = Frame(root, width=900, height=90, bg="white", bd=2, relief=GROOVE)
       # left_frame.place(relx=0.1, rely=0.1)
        mumbai = Button(root, text='Mumbai', bg="#B31312", fg="white", font=("Arial", 12), relief="raised",)
                       # command=self.display_graph)
        mumbai.place(relx=0.10, rely=0.29)

        delhi = Button(root, text='  Delhi  ', bg="#B31312", fg="white", font=("Arial", 12), relief="raised",)
                       #command=self.display_graph2)
        delhi.place(relx=0.25, rely=0.29)

        bengaluru = Button(root, text='Bengaluru', bg="#B31312", fg="white", font=("Arial", 12), relief="raised",)
                        #   command=self.display_graph3)
        bengaluru.place(relx=0.4, rely=0.29)

        Chennai = Button(root, text=' Chennai ', bg="#B31312", fg="white", font=("Arial", 12), relief="raised",)
                        # command=self.display_graph4)
        Chennai.place(relx=0.55, rely=0.29)

        Kolkata = Button(root, text=' Kolkata ', bg="#B31312", fg="white", font=("Arial", 12), relief="raised",)
                         #command=self.display_graph5)
        Kolkata.place(relx=0.7, rely=0.29)

        Pune = Button(root, text='   Pune   ', bg="#B31312", fg="white", font=("Arial", 12), relief="raised",)
                      #command=self.display_graph6)
        Pune.place(relx=0.85, rely=0.29)

        land = Label(root, text='Land Value Analysis', bg="white", fg="Black", font=("Arial", 19))#, relief="raised",

        land.place(relx=0.39, rely=0.15)

    def buy(self):
        self.root.destroy()
        import buy1

    def agent(self):
        self.root.destroy()
        import Agent1

    def profile(self):
        self.root.destroy()
        import Profile

    def rent(self):
        self.root.destroy()
        import Rent1

    def sell(self):
        self.root.destroy()
        import Sell_1

    def rentup(self):
        self.root.destroy()
        import Rent2

    def emi(self):
        import emi

    def home(self):
        import Homepage1



root=Tk()
obj = maininterface2(root)
root.mainloop()