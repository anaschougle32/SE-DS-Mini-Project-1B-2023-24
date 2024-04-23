from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
#import tkinter as Tk
from tkinter import messagebox
from tkinter import Tk,Label



class Sell_3:
    username = None

    def __init__(self, root):
        self.root = root
        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 15, "bold")

        one = Label(root,
                    text="EstateInsight",
                    bg="#B31312",
                    fg="white",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=1,
                    height=1)
        one.pack(fill=X, side=TOP)
        name_label = Label(one,
                           text=f"{Sell_3.username}",
                           bg='#B31312',
                           fg='white',
                           bd=0)
        name_label.place(relx=0.85, rely=0.1)  # name
        down_arrow = Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
        down_arrow.pack()
        down_arrow.menu = Menu(down_arrow)
        down_arrow["menu"] = down_arrow.menu
        down_arrow.menu.add_checkbutton(label="Profile")
        down_arrow.menu.add_checkbutton(label="Agents")
        down_arrow.place(relx=0.92)  # drop down arrow

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
        self.icon = PhotoImage(file='Images/estate.png')  # Load the image here
        self.root.iconphoto(True, self.icon)  # Use the loaded image as iconphoto


        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='#22107031#',
                database='estateinsight'
            )
            print("Connected to MySQL")
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Database Error", "Failed to connect to database")
            return





        # ***************************setting the main part******************************

        # top text
        top_text = tk.Label(root, text='Additional Property Details',
                            bg='white',
                            fg='black',
                            font=('Bold', 20))
        top_text.place(relx=0.01, rely=0.08)

        # furnishing status
        furnishing = tk.Label(root, text='>Furnishing Status:', font=('Bold', 17), bg='white')
        furnishing.place(relx=0.01, rely=0.21)
        furnishing_ent = tk.Entry(root, font=('Bold', 17),
                                  highlightcolor='black', highlightbackground='gray',
                                  highlightthickness=2)
        furnishing_ent.place(relx=0.01, rely=0.26)

        # Flooring
        flooring = tk.Label(root, text='>Flooring:', font=('Bold', 17), bg='white')
        flooring.place(relx=0.5, rely=0.21)
        flooring_ent = tk.Entry(root, font=('Bold', 17),
                                highlightcolor='black', highlightbackground='gray',
                                highlightthickness=2)
        flooring_ent.place(relx=0.5, rely=0.26)

        # overlooking
        overlooking = tk.Label(root, text='>Overlooking:', font=('Bold', 17), bg='white')
        overlooking.place(relx=0.01, rely=0.41)
        overlooking_ent = tk.Entry(root, font=('Bold', 17),
                                   highlightcolor='black', highlightbackground='gray',
                                   highlightthickness=2)
        overlooking_ent.place(relx=0.01, rely=0.46)

        # age of construction
        construction = tk.Label(root, text='>Age of Construction:', font=('Bold', 17), bg='white')
        construction.place(relx=0.5, rely=0.41)
        construction_ent = tk.Entry(root, font=('Bold', 17),
                                  highlightcolor='black', highlightbackground='gray',
                                  highlightthickness=2)
        construction_ent.place(relx=0.5, rely=0.46)

        # water availaibility
        water = tk.Label(root, text='>Water Availability:', font=('Bold', 17), bg='white')
        water.place(relx=0.01, rely=0.61)
        water_ent = tk.Entry(root, font=('Bold', 17),
                             highlightcolor='black', highlightbackground='gray',
                             highlightthickness=2)
        water_ent.place(relx=0.01, rely=0.66)

        # electricity status
        electric = tk.Label(root, text='>Electricity Status:', font=('Bold', 17), bg='white')
        electric.place(relx=0.5, rely=0.61)
        electric_ent = tk.Entry(root, font=('Bold', 17),
                                highlightcolor='black', highlightbackground='gray',
                                highlightthickness=2)
        electric_ent.place(relx=0.5, rely=0.66)

        # 1st image


        # adding the submit button
        submit_butt = tk.Button(root, text="Submit",
                                font=('Bold', 15), bg='#B31312',
                                fg='white', bd=1,command= self.next)
        submit_butt.place(relx=0.5, rely=0.85, anchor=CENTER)#, command=self.homepage)

        self.furnishing_ent = furnishing_ent
        self.flooring_ent = flooring_ent
        self.overlooking_ent = overlooking_ent
        self.construction_ent = construction_ent
        self.water_ent = water_ent
        self.electric_ent = electric_ent

    def next(self):
        # Retrieve username (assuming you have a way to get the username)
        #userID = "sell_1"  # Change this with your username retrieval logic

        # Retrieve values from entry widgets
        furnishing_ent = self.furnishing_ent.get()
        flooring_ent = self.flooring_ent.get()
        overlooking_ent = self.overlooking_ent.get()
        construction_ent = self.construction_ent.get()
        water_ent = self.water_ent.get()
        electric_ent = self.electric_ent.get()

        try:
            if self.conn.is_connected():
                pst = self.conn.cursor()

                # Update row with the userID
                sql_update = (
                    "UPDATE sell SET furnishing = %s, flooring = %s, overlook = %s, age = %s, wateravail = %s, elecstatus = %s WHERE username = %s")

                pst.execute(sql_update, (
                    furnishing_ent,flooring_ent,overlooking_ent,construction_ent,water_ent,electric_ent, Sell_3.username))
                self.conn.commit()
                messagebox.showinfo("", "Successfully Saved")
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("", "Failed to register")

    def homepage(self):
        self.root.destroy()
        import Homepage1


root=Tk()
obj = Sell_3(root)
root.mainloop()