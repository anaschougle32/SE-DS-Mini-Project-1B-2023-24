import subprocess
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




class Homepage1:
    def  __init__(self, root, username):
        self.root = root
        self.username = username
        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)
        self.username = username  # this is used to store the username
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)
        font_info = ("Arial", 19, "bold")

        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#22107031#',
            database='estateinsight'
        )

        # Create a cursor to execute SQL queries
        self.cursor = self.conn.cursor()
        #self.fetch_data_from_database()
        # Execute SELECT query to fetch name from the database table
        self.cursor.execute('SELECT username FROM signin WHERE username = %s', (self.username,))
        row = self.cursor.fetchone()
        if row:
            name = row[0]
        else:
            name = ""

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
                           text=self.username,
                           bg='#B31312',
                           fg='white',
                           bd=0, font=('Bold', 17))
        name_label.place(relx=0.78, rely=0.1, )  # name
        down_arrow = Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
        down_arrow.pack()
        down_arrow.menu = Menu(down_arrow)
        down_arrow["menu"] = down_arrow.menu
        down_arrow.menu.add_checkbutton(label="Profile", command=self.profile)
        down_arrow.menu.add_checkbutton(label="Agents", command=self.agent)
        down_arrow.menu.add_checkbutton(label="LogOut", command=self.login)

        down_arrow.place(relx=0.92)  # drop down arrow

        # app color
        self.root.configure(bg='white')

        # Add a button to open chat if there's a notification
        self.chat_button = Button(root, text="Chat", command=self.accept_chat_request)
        self.chat_button.place(relx=0.75, rely=0.2)
        # Add a Text widget to display notifications
        self.notification_text = Text(root, width=20, height=2, wrap=WORD, font=("Arial", 12))
        self.notification_text.place(relx=0.75, rely=0.15)

        # Fetch and display notifications from the database
        #self.check_notifications()
        self.fetch_notifications()
        # setting up geometry for app
        window_width = 1000
        window_height = 680

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
                           border=0,command=self.rentup)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Land/Value Graph",
                           bg="white",
                           font=toolbar_font,
                           border=0)
        printButt.pack(side=LEFT, padx=20, pady=2)

        printButt = Button(toolbar,
                           text="Calculate EMI",
                           bg="white",
                           border=0,
                           font=toolbar_font,
                           command=self.emi)
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

        # setting up the search bar
        custom_font = tkFont.Font(family="Bold", size=15, underline=True)
        top_text = tk.Label(root, text='Popular Properties',
                            bg='white',
                            fg='black',
                            font=custom_font)
        top_text.place(relx=0.03, rely=0.18)



        frame1 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       relief=GROOVE,
                       bd=1
                       )

        frame1.place(relx=0.03, rely=0.25)

        property_name = self.fetch_property_name_from_database(1)  # Assuming property ID 1
        image_label = Label(frame1, text=property_name, bg="white", font=("Arial", 12, "bold"))
        image_label.pack(pady=5)
        # Fetch image from database and display
        self.display_image_from_database(frame1, 1)  # Assuming image ID 1

        view_butt = Button(root, bg='white', bd=1, text='View',  command=lambda prop=property_name: self.main_view1(prop))
        view_butt.place(relx=0.15, rely=0.58)

        frame2 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame2.place(relx=0.35, rely=0.25)

        property_name = self.fetch_property_name_from_database(2)  # Assuming property ID 1
        image_label = Label(frame2, text=property_name, bg="white", font=("Arial", 12, "bold"))
        image_label.pack(pady=5)
        # Fetch image from database and display
        self.display_image_from_database(frame2, 2)  # Assuming image ID 2

        view_butt = Button(root, bg='white', bd=1, text='View', command=lambda prop=property_name: self.main_view1(prop))
        view_butt.place(relx=0.48, rely=0.58)

        frame3 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame3.place(relx=0.67, rely=0.25)

        property_name = self.fetch_property_name_from_database(3)  # Assuming property ID 1
        image_label = Label(frame3, text=property_name, bg="white", font=("Arial", 12, "bold"))
        image_label.pack(pady=5)
        # Fetch image from database and display
        self.display_image_from_database(frame3, 3)  # Assuming image ID 3

        view_butt = Button(root, bg='white', bd=1, text='View', command=lambda prop=property_name: self.main_view1(prop))
        view_butt.place(relx=0.8, rely=0.58)

        frame4 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE
                       )
        frame4.place(relx=0.03, rely=0.63)

        property_name = self.fetch_property_name_from_database(4)  # Assuming property ID 1
        image_label = Label(frame4, text=property_name, bg="white", font=("Arial", 12, "bold"))
        image_label.pack(pady=5)
        # Fetch image from database and display
        self.display_image_from_database(frame4, 4)  # Assuming image ID 4

        view_butt = Button(root, bg='white', bd=1, text='View', command=lambda prop=property_name: self.main_view1(prop))
        view_butt.place(relx=0.2, rely=0.93)

        frame5 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame5.place(relx=0.35, rely=0.63)

        property_name = self.fetch_property_name_from_database(5)  # Assuming property ID 1
        image_label = Label(frame5, text=property_name, bg="white", font=("Arial", 12, "bold"))
        image_label.pack(pady=5)
        # Fetch image from database and display
        self.display_image_from_database(frame5, 5)  # Assuming image ID 5

        view_butt = Button(root, bg='white', bd=1, text='View', command=lambda prop=property_name: self.main_view1(prop))
        view_butt.place(relx=0.5, rely=0.93)

        frame6 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame6.place(relx=0.67, rely=0.63)

        property_name = self.fetch_property_name_from_database(6)  # Assuming property ID 1
        image_label = Label(frame6, text=property_name, bg="white", font=("Arial", 12, "bold"))
        image_label.pack(pady=5)

        # Fetch image from database and display
        self.display_image_from_database(frame6, 6)  # Assuming image ID 6

        view_butt = Button(root, bg='white', bd=1, text='View', command=lambda prop=property_name: self.main_view1(prop))
        view_butt.place(relx=0.8, rely=0.93)
        # Method to fetch notifications from the database

    def fetch_notifications(self):
        try:
            # Execute SELECT query to fetch notifications from the database
            self.cursor.execute('SELECT notification FROM sell WHERE username = %s', (self.username,))
            notifications = self.cursor.fetchall()

            # Clear existing notifications in the Text widget
            self.notification_text.delete('1.0', END)

            # Display notifications in the Text widget
            for notification in notifications:
                self.notification_text.insert(END, f"{notification[0]}\n")

            self.notification_text.config(state='disabled')

        except Exception as e:
            print("Error fetching notifications:", e)

        # Method to open chat
    def accept_chat_request(self):
        import chat
        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='ARYA#305#varun',
                database='estateinsight'
            )

            # Create a cursor to execute SQL queries
            cursor = conn.cursor()

            # Execute DELETE query to remove the notification from the agent table
            cursor.execute("UPDATE sell SET notification = NULL WHERE username = %s", (self.username,))
            conn.commit()  # Commit the transaction

            print("Notification deleted successfully")

        except mysql.connector.Error as e:
            print("Error deleting notification:", e)
    def buy(self):
        self.root.destroy()
        import buy1

    def agent(self):
        self.root.destroy()
        import Agent1

    def profile(self):
        self.root.destroy()
        import Profile

    def home(self):
        self.root.destroy()
        import Homepage1

    def rent(self):
        self.root.destroy()
        import Rent1

    def sell(self):
        self.root.destroy()
        import Sell_1

    def rentup(self):
        self.root.destroy()
        import Rent2
    def login(self):
        self.root.destroy()
        import login

    def emi(self):
        import emi
    def display_image_from_database(self, frame, image_id):
        try:
            cursor = self.conn.cursor()
            # Fetch image data from the database
            cursor.execute("SELECT photo1 FROM sell WHERE ID = %s", (image_id,))
            image_data = cursor.fetchone()
            if image_data:
                image_data = image_data[0]  # Extract image data from the tuple

                # Convert binary image data to Image object
                image = Image.open(image_data)

                # Resize image
                image.thumbnail((200, 200))

                # Convert Image object to PhotoImage object
                photo_image = ImageTk.PhotoImage(image)

                # Display image in label
                label = Label(frame, image=photo_image, bg="white")
                label.image = photo_image  # Keep a reference to the image
                label.pack(padx=45, pady=45)
            else:
                print("No image data found for image ID:", image_id)

        except Exception as e:
            print("Error displaying image:", e)

    def fetch_property_name_from_database(self, property_id):
        try:
            # Assuming you have a table named 'properties' with columns 'property_id' and 'property_name'
            sql = "SELECT propertyname FROM sell WHERE id = %s"
            self.cursor.execute(sql, (property_id,))
            result = self.cursor.fetchone()
            if result:
                return result[0]  # Assuming property_name is the first column in the result
            else:
                return "Property not found"
        except mysql.connector.Error as e:
            print("Error fetching property name from database:", e)
            return "Error fetching property name"
    def main_view1(self, propertyname):
        bs = propertyname
        subprocess.call(["python", "main_view1.py", bs])

root = Tk()
obj = Homepage1(root, "")
root.mainloop()