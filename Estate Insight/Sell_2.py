from tkinter import *
import tkinter as tk
from tkinter import messagebox
from mysql.connector import Error
import mysql.connector
from tkinter import Tk,Label


class Sell_2:
    username= None
    def __init__(self, root):
        self.root = root
        # self.userID = userID
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
        Sell_2.username
        name_label = Label(one,
                          # text=f"Welcome, {Sell_2.username}!",
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

        # *********setting the main part************

        # adding top text
        top_text = tk.Label(root, text='More Property Details',
                            bg='white',
                            fg='black',
                            font=('Bold', 20))
        top_text.place(relx=0.01, rely=0.06)

        # Area part

        area_text = tk.Label(root, text='Area Details:',
                             bg='white',
                             fg='black',
                             font=('Microsoft Sans', 17))
        area_text.place(relx=0.01, rely=0.15)

        # carpet area
        carpet_area = tk.Label(root, text='>Carpet Area', font=('Bold', 15), bg='white')
        carpet_area.place(relx=0.01, rely=0.21)
        carpet_area_ent = tk.Entry(root, font=('Bold', 15),
                                   highlightcolor='black', highlightbackground='gray',
                                   highlightthickness=2)
        carpet_area_ent.place(relx=0.01, rely=0.26)

        # carpet area/sq.ft
        carpet_price = tk.Label(root, text='>Price/Sq.Ft', font=('Bold', 15), bg='white')
        carpet_price.place(relx=0.26, rely=0.21)
        carpet_price_ent = tk.Entry(root, font=('Bold', 15),
                                    highlightcolor='black', highlightbackground='gray',
                                    highlightthickness=2)
        carpet_price_ent.place(relx=0.26, rely=0.26)

        # floors
        floor = tk.Label(root, text='>Floor', font=('Bold', 15), bg='white')
        floor.place(relx=0.51, rely=0.21)
        floor_ent = tk.Entry(root, font=('Bold', 15),
                             highlightcolor='black', highlightbackground='gray',
                             highlightthickness=2)
        floor_ent.place(relx=0.51, rely=0.26)

        # out of floors
        floor_out = tk.Label(root, text='>Number of Floors', font=('Bold', 15), bg='white')
        floor_out.place(relx=0.76, rely=0.21)
        floor_out_ent = tk.Entry(root, font=('Bold', 15),
                                 highlightcolor='black', highlightbackground='gray',
                                 highlightthickness=2)
        floor_out_ent.place(relx=0.76, rely=0.26)

        # location part

        location_text = tk.Label(root, text='Location Details:',
                                 bg='white',
                                 fg='black',
                                 font=('Microsoft Sans', 17))
        location_text.place(relx=0.01, rely=0.36)

        # adress
        address = tk.Label(root, text='>Address', font=('Bold', 15), bg='white')
        address.place(relx=0.01, rely=0.42)
        address_ent = tk.Entry(root, font=('Bold', 15),
                               highlightcolor='black', highlightbackground='gray',
                               highlightthickness=2)
        address_ent.place(relx=0.01, rely=0.47)

        # landmarks
        landmark = tk.Label(root, text='>Landmark', font=('Bold', 15), bg='white')
        landmark.place(relx=0.3, rely=0.42)
        landmark_ent = tk.Entry(root, font=('Bold', 15),
                                highlightcolor='black', highlightbackground='gray',
                                highlightthickness=2)
        landmark_ent.place(relx=0.3, rely=0.47)

        # pricing part

        pricing_text = tk.Label(root, text='Pricing Details:',
                                bg='white',
                                fg='black',
                                font=('Microsoft Sans', 17))
        pricing_text.place(relx=0.01, rely=0.57)

        # price
        price = tk.Label(root, text='>Price', font=('Bold', 15), bg='white')
        price.place(relx=0.01, rely=0.63)
        price_ent = tk.Entry(root, font=('Bold', 15),
                             highlightcolor='black', highlightbackground='gray',
                             highlightthickness=2)
        price_ent.place(relx=0.01, rely=0.68)

        # booking
        booking = tk.Label(root, text='>Booking', font=('Bold', 15), bg='white')
        booking.place(relx=0.3, rely=0.63)
        booking_ent = tk.Entry(root, font=('Bold', 15),
                               highlightcolor='black', highlightbackground='gray',
                               highlightthickness=2)
        booking_ent.place(relx=0.3, rely=0.68)

        # Define instance variables for entry widgets
        self.carpet_area_ent = carpet_area_ent
        self.carpet_area_price = carpet_price_ent
        self.floor_ent = floor_ent
        self.floor_out_ent = floor_out_ent
        self.address_ent = address_ent
        self.landmark_ent = landmark_ent
        self.price_ent = price_ent
        self.booking_ent = booking_ent

        # next button
        next_butt = tk.Button(root, text="Next",
                              font=('Bold', 15), bg='#B31312',
                              fg='white', bd=1, command=self.next)
        next_butt.place(relx=0.5, rely=0.87, anchor=CENTER)

    def next(self):
        # Retrieve username (assuming you have a way to get the username)
        #userID = "sell_1"  # Change this with your username retrieval logic

        # Retrieve values from entry widgets
        carpet_area_value = self.carpet_area_ent.get()
        carpet_price_value = self.carpet_area_price.get()
        floor_value = self.floor_ent.get()
        floor_out_value = self.floor_out_ent.get()
        address_value = self.address_ent.get()
        landmark_value = self.landmark_ent.get()
        price_value = self.price_ent.get()
        booking_value = self.booking_ent.get()

        try:
            if self.conn.is_connected():
                pst = self.conn.cursor()

                # Update row with the userID
                sql_update = (
                    "UPDATE sell SET carpetarea = %s, floor = %s, address = %s, landmarks = %s, price = %s, bookingprice = %s WHERE username = %s")

                pst.execute(sql_update, (
                    carpet_area_value, floor_value, address_value,
                    landmark_value, price_value, booking_value, self.username))
                self.conn.commit()
                messagebox.showinfo("", "Successfully Saved")
                # Close the Sell_1 window
                self.root.destroy()

                # Import and display the Sell_2 window
                import Sell_3
                Sell_3.Sell_3.username = Sell_2.username  # Set the username attribute
                #if self.root.winfo_exists():
                      # Close the Login window
                Sell_3 = Sell_3.Sell_3(Tk())  # Open the Homepage1 window
            else:
                print("Login window has been closed")

        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("", "Failed to register")



# Create the root window and instantiate the Sell_2 class
root = Tk()
obj = Sell_2(root)
root.mainloop()