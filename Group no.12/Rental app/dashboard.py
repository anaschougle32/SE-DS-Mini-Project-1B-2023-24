
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from tkcalendar import Calendar
import mysql.connector
from tkinter import messagebox
import uuid
from datetime import datetime
from io import BytesIO
import io
import subprocess
import requests
from tkinter import simpledialog
import webbrowser
import time
import socket
from threading import Thread


class ModernTk(tk.Tk):
    def __init__(self):
        super().__init__()
        

    def run(self):
        self.mainloop()

class RentalApplication():
    def __init__(self, master, username):
        self.master = master
        self.master.geometry('950x600')
        self.master.title("Rental Application")
        self.master.config(bg="#121212")  # Set background color to dark gray
        self.create_widgets(username)
        self.username = username
        

    def run(self):
        self.master.mainloop()

    def create_widgets(self, username):
        self.options_frame = tk.Frame(self.master, bg='#232323', width=200, height=600)  # Adjusted size
        self.options_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.main_frame = tk.Frame(self.master, highlightbackground='black', highlightthickness=1, width=620, height=550, bg="#121212")  # Darker background
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add user logo
        user_logo = Image.open("user_logo.png")  # Provide the path to your user logo image
        user_logo = user_logo.resize((100, 100))  # Resize the logo
        user_logo = ImageTk.PhotoImage(user_logo)
        logo_label = tk.Label(self.options_frame, image=user_logo, bg="#232323")
        logo_label.image = user_logo
        logo_label.pack()

        # Add username text
        username_label = tk.Label(self.options_frame, text=username, font=('Arial', 14), fg='white', bg='#232323')
        username_label.pack(pady=(20, 5))  # Increase the gap between Username and Home button

        # Add buttons with icons
        self.pages = {
            " Home": {"icon": "home_icon.png", "command":lambda:self.home_page(username)},
            " Profile": {"icon": "profile_icon.png", "command": lambda:self.profile_page(username)},
            " Orders": {"icon": "order_icon.png", "command": self.order_page},
            " My Ads": {"icon": "ad_icon.png", "command": self.my_ads_page},
            " My Rentee": { "icon": "cart_icon.png", "command" :self.rentee_page},
            " About": {"icon": "about_icon.png", "command": self.about_page},
            
        }
        self.current_page = None
        self.buttons = {}
        for text, info in self.pages.items():
            icon = Image.open(info["icon"])
            icon = icon.resize((30, 30))  # Resize the icon
            icon = ImageTk.PhotoImage(icon)
            command=info["command"]
            button = tk.Button(self.options_frame, text=text, image=icon, compound=tk.LEFT,
                   font=('Arial', 14), fg='white', bg='#800080',  # Adjusted font size and button color
                   width=180,cursor="hand2" ,command=lambda cmd=command: self.change_page(cmd)) 
            button.image = icon
            button.pack(side=tk.TOP, fill=tk.X, pady=5)  # Adjust position for buttons
            self.buttons[text] = button

        

        # Add logout button at the bottom with an icon
        logout_icon = Image.open("logout_icon.png")  # Provide the path to your logout icon image
        logout_icon = logout_icon.resize((30, 30))  # Resize the icon
        logout_icon = ImageTk.PhotoImage(logout_icon)
        logout_button = tk.Button(self.options_frame, text="Logout", image=logout_icon, compound=tk.LEFT,
                                  font=('Arial', 14), fg='white', bg='#800080',cursor="hand2" ,width=180, command=self.logout)  # Adjusted font size and button width
        logout_button.image = logout_icon
        logout_button.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        # Add Terms & Conditions button at the bottom with custom styling
        terms_icon = Image.open("terms_icon.png")  # Provide the path to your Terms icon image
        terms_icon = terms_icon.resize((24, 24))  # Resize the icon
        terms_icon = ImageTk.PhotoImage(terms_icon)
        terms_button = tk.Button(self.options_frame, text=" Terms&Condition", image=terms_icon, compound=tk.LEFT,
                                font=('Arial', 14, 'underline'), fg='white', bg='#232323', width=180,
                                borderwidth=0, cursor="hand2",  # Added borderwidth and cursor properties
                                command=self.terms_conditions_page)  # Command for the Terms & Conditions page
        terms_button.image = terms_icon
        terms_button.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        self.change_page(lambda:self.home_page(username))  # Select home page by default
    
    
    def logout(self):
        # Prompt user for confirmation
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            # Destroy the current window
            self.master.destroy()
            # Start the start.py file using subprocess
            subprocess.run(["python", "start.py"])
        
        

    
    def change_page(self, page):
        # Delete existing pages
        self.delete_pages()

    # Check if the page is the profile page
        if page == self.profile_page:
            self.display_profile_data(self.username)

        

    # Create a new frame for the selected page
        if callable(page):
            page()

    # Set the current page attribute to the selected page
        self.current_page = page

    def return_to_home(self, frame):
        # Destroy the current page frame
        frame.destroy()
        # Navigate back to the home page
        self.home_page(self.username)


    def carrom_page(self,username):
        # Placeholder for carrom page content
        self.delete_pages()

        carrom_frame = tk.Frame(self.main_frame, bg="#121212")
        carrom_frame.pack(fill=tk.BOTH, expand=True)

        # Add back button
        back_button = tk.Button(carrom_frame, text="Back", command=lambda: self.return_to_home(carrom_frame), font=('Arial', 12), bg="#800080", fg="white", width=15, height=2)
        back_button.place(x=560, y=7)

        carrom_label = tk.Label(carrom_frame, text="Carrom Page Content:", font=('Arial', 20), fg="white", bg="#121212")
        carrom_label.place(x=10, y=10)

        # Create a canvas for scrolling
        canvas = tk.Canvas(carrom_frame, bg="#121212")
        canvas.place(x=10, y=60, relwidth=0.95, relheight=0.9)

        # Add a scrollbar for the canvas
        scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        carrom_content_frame = tk.Frame(canvas, bg="#121212")
        canvas.create_window((0, 0), window=carrom_content_frame, anchor=tk.NW) # Use grid instead of pack

        # Fetch data from the database where category is "Football"
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            sql = "SELECT title, price,description, image1,username,phoneno FROM ad_table WHERE category = 'Carrom'"
            cursor.execute(sql)
            carrom_ads = cursor.fetchall()

            # Create containers dynamically
            row_num = 1  # Start row from 2 as back button and label are in rows 0 and 1
            col_num = 0
            for ad in carrom_ads:
                container = tk.Frame(carrom_content_frame, bg="#212121", width=200, height=300)
                container.grid(row=row_num, column=col_num, padx=10, pady=10,sticky="nw")

                # Display image
                image_data = ad[3]
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((150, 150))  # Adjust the size as needed
                photo_image = ImageTk.PhotoImage(image)
                image_label = tk.Label(container, image=photo_image)
                image_label.image = photo_image  # Keep a reference
                image_label.grid(row=0, column=0, padx=10, pady=10)

                # Display title
                title_label = tk.Label(container, text=ad[0], font=('Arial', 14), fg="white", bg="#212121")
                title_label.grid(row=1, column=0, padx=10, pady=5)

                # Display price
                price_label = tk.Label(container, text="Price: ₹" + str(ad[1]), font=('Arial', 12), fg="white", bg="#212121")
                price_label.grid(row=2, column=0, padx=10, pady=5)

                # View button
                view_button = tk.Button(container, text="View", command=lambda ad=ad: self.view_ad(ad,username), font=('Arial', 12), bg="#800080", fg="white")
                view_button.grid(row=3, column=0, padx=10, pady=5)

                if ad[4] == self.username:
                    view_button.config(state=tk.DISABLED)

                col_num += 1
                if col_num == 3:
                    col_num = 0
                    row_num += 1

        except mysql.connector.Error as err:
            # Handle any errors
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

        carrom_content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        print("carrom Page")

    def product_page(self):
    #     # Placeholder for product page content
    #     self.delete_pages()

    #     def update_selected_dates():
    #         start_date = calendar.selection_get()
    #         end_date = start_date + datetime.timedelta(days=4)  # Assuming a 5-day rental period
    #         selected_dates_label.config(text=f"Selected dates: {start_date.strftime('%d %B')} - {end_date.strftime('%d %B')}")

    #         # Calculate total price based on the number of days selected
    #         num_days = (end_date - start_date).days + 1  # Include the end date
    #         total_price = num_days * 100  # Assuming $100 per day
    #         price_label.config(text=f"Price: ${total_price}")

    #         # Update the displayed price
    #         updated_price_label.config(text=f"Updated Price: ${total_price}")

    #     def rent_now():
    #         # Add your rent now functionality here
    #         pass

    #     product_frame = tk.Frame(self.main_frame, bg="#121212")
    #     product_frame.pack(fill=tk.BOTH, expand=True)

    #     # Add back button
    #     back_button = tk.Button(product_frame, text="Back", command=lambda: self.return_to_home(product_frame), font=('Arial', 12), bg="#800080", fg="white", width=15, height=2)
    #     back_button.place(x=600 ,y=18)
        
    #     product_label = tk.Label(product_frame, text="Product Page Content:", font=('Arial', 20), fg="white", bg="#121212")
    #     product_label.pack(padx=20, pady=20)

    #     # Create a canvas with a scrollbar
    #     canvas = tk.Canvas(product_frame, bg="#121212")
    #     scrollbar = tk.Scrollbar(product_frame, orient=tk.VERTICAL, command=canvas.yview)
    #     scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    #     canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    #     canvas.configure(yscrollcommand=scrollbar.set)

    #     # Create a frame inside the canvas to hold the content
    #     content_frame = tk.Frame(canvas, bg="#121212")
    #     content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    #     canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

    #     # Add empty image box in the top-left corner of the canvas
    #     empty_image_box = tk.Frame(content_frame, bg="white", width=200, height=200)
    #     empty_image_box.grid(row=0, column=0, padx=20, pady=20)

    #     # Add title text on the right side parallel to the empty box
    #     title_text = tk.Label(content_frame, text="Title:", font=('Arial', 12), fg="white", bg="#121212")
    #     title_text.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    #     # Add "published by" text below the title
    #     published_by_text = tk.Label(content_frame, text="Published By:", font=('Arial', 12), fg="white", bg="#121212")
    #     published_by_text.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    #     # Add description text below published by text
    #     description_text = tk.Label(content_frame, text="Description:", font=('Arial', 12), fg="white", bg="#121212")
    #     description_text.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    #     # Add a calendar widget below the description
    #     calendar = Calendar(content_frame, font=('Arial', 10), selectmode='day', date_pattern='yyyy-mm-dd', command=update_selected_dates)
    #     calendar.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    #     # Add a label to display selected dates
    #     selected_dates_label = tk.Label(content_frame, text="", font=('Arial', 12), fg="white", bg="#121212")
    #     selected_dates_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    #     # Add price label
    #     price_label = tk.Label(content_frame, text="Price: $0", font=('Arial', 12), fg="white", bg="#121212")
    #     price_label.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    #     # Add updated price label
    #     updated_price_label = tk.Label(content_frame, text="", font=('Arial', 12), fg="white", bg="#121212")
    #     updated_price_label.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    #     # Add "Rent Now" button
    #     rent_now_button = tk.Button(content_frame, text="Rent Now", font=('Arial', 12), bg="#800080", fg="white", width=20, height=2, command=rent_now)
    #     rent_now_button.grid(row=7, column=1, padx=20, pady=(0, 20), sticky="w")
        pass
            

         



    def football_page(self,username):
        # Placeholder for football page content
        self.delete_pages()

        football_frame = tk.Frame(self.main_frame, bg="#121212")
        football_frame.pack(fill=tk.BOTH, expand=True)

        # Add back button
        back_button = tk.Button(football_frame, text="Back", command=lambda: self.return_to_home(football_frame), font=('Arial', 12), bg="#800080", fg="white", width=15, height=2)
        back_button.place(x=560, y=7)

        football_label = tk.Label(football_frame, text="Football Page Content:", font=('Arial', 20), fg="white", bg="#121212")
        football_label.place(x=10, y=10)

        # Create a canvas for scrolling
        canvas = tk.Canvas(football_frame, bg="#121212")
        canvas.place(x=10, y=60, relwidth=0.95, relheight=0.9)

        # Add a scrollbar for the canvas
        scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        football_content_frame = tk.Frame(canvas, bg="#121212")
        canvas.create_window((0, 0), window=football_content_frame, anchor=tk.NW)

        # Fetch data from the database where category is "Football"
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            sql = "SELECT title, price, description, image1, username,phoneno FROM ad_table WHERE category = 'Football'"
            cursor.execute(sql)
            football_ads = cursor.fetchall()

            # Create containers dynamically
            row_num = 1
            col_num = 0
            for ad in football_ads:
                container = tk.Frame(football_content_frame, bg="#212121", width=200, height=300)
                container.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="w")

                # Display image
                image_data = ad[3]
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((150, 150))  # Adjust the size as needed
                photo_image = ImageTk.PhotoImage(image)
                image_label = tk.Label(container, image=photo_image)
                image_label.image = photo_image
                image_label.grid(row=0, column=0, padx=5, pady=10)

                # Display title
                title_label = tk.Label(container, text=ad[0], font=('Arial', 14), fg="white", bg="#212121")
                title_label.grid(row=1, column=0, padx=5, pady=5)

                # Display price
                price_label = tk.Label(container, text="Price: ₹" + str(ad[1]), font=('Arial', 12), fg="white", bg="#212121")
                price_label.grid(row=2, column=0, padx=5, pady=5)

                # View button
                view_button = tk.Button(container, text="View", command=lambda ad=ad: self.view_ad(ad,username), font=('Arial', 12), bg="#800080", fg="white", width=20)
                view_button.grid(row=3, column=0, padx=5, pady=5)
                if ad[4] == self.username:
                    view_button.config(state=tk.DISABLED)

                col_num += 1
                if col_num == 3:
                    col_num = 0
                    row_num += 1

        except mysql.connector.Error as err:
            # Handle any errors
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

        # Update the scroll region to encompass the entire frame
        football_content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))


    def cricket_page(self,username):
        # Placeholder for cricket page content
        self.delete_pages()

        cricket_frame = tk.Frame(self.main_frame, bg="#121212")
        cricket_frame.pack(fill=tk.BOTH, expand=True)

        # Add back button
        back_button = tk.Button(cricket_frame, text="Back", command=lambda: self.return_to_home(cricket_frame), font=('Arial', 12), bg="#800080", fg="white", width=15, height=2)
        back_button.place(x=560, y=7)

        cricket_label = tk.Label(cricket_frame, text="Cricket Page Content:", font=('Arial', 20), fg="white", bg="#121212")
        cricket_label.place(x=10, y=10)

        # Create a canvas for scrolling
        canvas = tk.Canvas(cricket_frame, bg="#121212")
        canvas.place(x=10, y=60, relwidth=0.95, relheight=0.9)

        # Add a scrollbar for the canvas
        scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        cricket_content_frame = tk.Frame(canvas, bg="#121212")
        canvas.create_window((0, 0), window=cricket_content_frame, anchor=tk.NW)  # Use grid instead of pack

        # Fetch data from the database where category is "cricket"
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            sql = "SELECT title, price,description, image1,username,phoneno FROM ad_table WHERE category = 'Cricket'"
            cursor.execute(sql)
            carrom_ads = cursor.fetchall()

            # Create containers dynamically
            row_num = 1  # Start row from 2 as back button and label are in rows 0 and 1
            col_num = 0
            for ad in carrom_ads:
                container = tk.Frame(cricket_content_frame, bg="#212121", width=200, height=300)
                container.grid(row=row_num, column=col_num, padx=10, pady=10,sticky="nw")

                # Display image
                image_data = ad[3]
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((150, 150))  # Adjust the size as needed
                photo_image = ImageTk.PhotoImage(image)
                image_label = tk.Label(container, image=photo_image)
                image_label.image = photo_image  # Keep a reference
                image_label.grid(row=0, column=0, padx=10, pady=10)

                # Display title
                title_label = tk.Label(container, text=ad[0], font=('Arial', 14), fg="white", bg="#212121")
                title_label.grid(row=1, column=0, padx=10, pady=5)

                # Display price
                price_label = tk.Label(container, text="Price: ₹" + str(ad[1]), font=('Arial', 12), fg="white", bg="#212121")
                price_label.grid(row=2, column=0, padx=10, pady=5)

                # View button
                view_button = tk.Button(container, text="View", command=lambda ad=ad: self.view_ad(ad,username), font=('Arial', 12), bg="#800080", fg="white")
                view_button.grid(row=3, column=0, padx=10, pady=5)
                if ad[4] == self.username:
                    view_button.config(state=tk.DISABLED)

                col_num += 1
                if col_num == 3:
                    col_num = 0
                    row_num += 1

        except mysql.connector.Error as err:
            # Handle any errors
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

       # Update the scroll region to encompass the entire frame
        cricket_content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        print("Cricket Page")

    def chess_page(self,username):
        # Placeholder for football page content
        self.delete_pages()

        chess_frame = tk.Frame(self.main_frame, bg="#121212")
        chess_frame.pack(fill=tk.BOTH, expand=True)

        # Add back button
        back_button = tk.Button(chess_frame, text="Back", command=lambda: self.return_to_home(chess_frame), font=('Arial', 12), bg="#800080", fg="white", width=15, height=2)
        back_button.place(x=560, y=7)  # Use grid instead of pack

        chess_label = tk.Label(chess_frame, text="Chess Page Content:", font=('Arial', 20), fg="white", bg="#121212")
        chess_label.place(x=10, y=10)  # Use grid instead of pack

        # Create a canvas for scrolling
        canvas = tk.Canvas(chess_frame, bg="#121212")
        canvas.place(x=10, y=60, relwidth=0.95, relheight=0.9)

        # Add a scrollbar for the canvas
        scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        chess_content_frame = tk.Frame(canvas, bg="#121212")
        canvas.create_window((0, 0), window=chess_content_frame, anchor=tk.NW)

        # Fetch data from the database where category is "Football"
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            sql = "SELECT title, price, description,image1,username,phoneno FROM ad_table WHERE category = 'Chess'"
            cursor.execute(sql)
            carrom_ads = cursor.fetchall()

            # Create containers dynamically
            row_num = 1  # Start row from 2 as back button and label are in rows 0 and 1
            col_num = 0
            for ad in carrom_ads:
                container = tk.Frame(chess_content_frame, bg="#212121", width=200, height=300)
                container.grid(row=row_num, column=col_num, padx=10, pady=10,sticky="nw")

                # Display image
                image_data = ad[3]
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((150, 150))  # Adjust the size as needed
                photo_image = ImageTk.PhotoImage(image)
                image_label = tk.Label(container, image=photo_image)
                image_label.image = photo_image  # Keep a reference
                image_label.grid(row=0, column=0, padx=10, pady=10)

                # Display title
                title_label = tk.Label(container, text=ad[0], font=('Arial', 14), fg="white", bg="#212121")
                title_label.grid(row=1, column=0, padx=10, pady=5)

                # Display price
                price_label = tk.Label(container, text="Price: ₹" + str(ad[1]), font=('Arial', 12), fg="white", bg="#212121")
                price_label.grid(row=2, column=0, padx=10, pady=5)

                # View button
                view_button = tk.Button(container, text="View", command=lambda ad=ad: self.view_ad(ad,username), font=('Arial', 12), bg="#800080", fg="white")
                view_button.grid(row=3, column=0, padx=10, pady=5)
                if ad[4] == self.username:
                    view_button.config(state=tk.DISABLED)

                col_num += 1
                if col_num == 3:
                    col_num = 0
                    row_num += 1

        except mysql.connector.Error as err:
            # Handle any errors
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

        # Update the scroll region to encompass the entire frame
        chess_content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        print("Chess Page")

    def badminton_page(self,username):
        # Placeholder for football page content
        self.delete_pages()

        badminton_frame = tk.Frame(self.main_frame, bg="#121212")
        badminton_frame.pack(fill=tk.BOTH, expand=True)

        # Add back button
        back_button = tk.Button(badminton_frame, text="Back", command=lambda: self.return_to_home(badminton_frame), font=('Arial', 12), bg="#800080", fg="white", width=15, height=2)
        back_button.place(x=560, y=7) # Use grid instead of pack

        badminton_label = tk.Label(badminton_frame, text="Badminton Page Content:", font=('Arial', 20), fg="white", bg="#121212")
        badminton_label.place(x=10, y=10)  # Use grid instead of pack

        # Create a canvas for scrolling
        canvas = tk.Canvas(badminton_frame, bg="#121212")
        canvas.place(x=10, y=60, relwidth=0.95, relheight=0.9)

        # Add a scrollbar for the canvas
        scrollbar = tk.Scrollbar(canvas, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        badminton_content_frame = tk.Frame(canvas, bg="#121212")
        canvas.create_window((0, 0), window=badminton_content_frame, anchor=tk.NW)

        # Fetch data from the database where category is "badminton"
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            sql = "SELECT title, price, description,image1,username,phoneno FROM ad_table WHERE category = 'Badminton'"
            cursor.execute(sql)
            carrom_ads = cursor.fetchall()

            # Create containers dynamically
            row_num = 1  # Start row from 2 as back button and label are in rows 0 and 1
            col_num = 0
            for ad in carrom_ads:
                container = tk.Frame(badminton_content_frame, bg="#212121", width=200, height=300)
                container.grid(row=row_num, column=col_num, padx=10, pady=10,sticky="nw")

                # Display image
                image_data = ad[3]
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((150, 150))  # Adjust the size as needed
                photo_image = ImageTk.PhotoImage(image)
                image_label = tk.Label(container, image=photo_image)
                image_label.image = photo_image  # Keep a reference
                image_label.grid(row=0, column=0, padx=10, pady=10)

                # Display title
                title_label = tk.Label(container, text=ad[0], font=('Arial', 14), fg="white", bg="#212121")
                title_label.grid(row=1, column=0, padx=10, pady=5)

                # Display price
                price_label = tk.Label(container, text="Price: ₹" + str(ad[1]), font=('Arial', 12), fg="white", bg="#212121")
                price_label.grid(row=2, column=0, padx=10, pady=5)

                # View button
                view_button = tk.Button(container, text="View", command=lambda ad=ad: self.view_ad(ad,username), font=('Arial', 12), bg="#800080", fg="white")
                view_button.grid(row=3, column=0, padx=10, pady=5)
                if ad[4] == self.username:
                    view_button.config(state=tk.DISABLED)

                col_num += 1
                if col_num == 3:
                    col_num = 0
                    row_num += 1

        except mysql.connector.Error as err:
            # Handle any errors
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

        # Update the scroll region to encompass the entire frame
        badminton_content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        print("Badminton Page")

    def home_page(self,username):
        # Placeholder for home page content
        home_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        home_frame.pack(fill=tk.BOTH, expand=True)

        canvas_height = 50
        canvas = tk.Canvas(home_frame, bg="#121212", highlightthickness=0, height=canvas_height)
        canvas.pack(fill=tk.X)

        canvas.create_rectangle(0, 0, self.master.winfo_screenwidth(), canvas_height, fill="#212121")  # Adjust width as per screen width

        # Add text 'Home' on the left side of the canvas
        canvas.create_text(10, canvas_height // 2, anchor=tk.W, text="Home", fill="white", font=('Arial', 16, 'bold'))

        # Add 'Categories:' text below the canvas
        categories_label = tk.Label(self.main_frame, text="Categories:", font=('Arial', 24), fg="white", bg="#121212")
        categories_label.place(x=10, y=canvas_height + 30)  # Adjust y position as needed

        plus_icon = Image.open("plus_icon.png")
        plus_icon = plus_icon.resize((20, 20))  # Resize the image if needed
        plus_icon = ImageTk.PhotoImage(plus_icon)

        # Add a button with text 'Publish Ad' and the plus icon
        publish_ad_button = tk.Button(home_frame, text="Upload Ad", image=plus_icon, compound=tk.LEFT, font=('Arial', 14), fg="white", bg="#800080",command=self.publish_ad_page)
        publish_ad_button.image = plus_icon  # Keep a reference to prevent image garbage collection
        publish_ad_button.place(x=600, y=canvas_height + 40)

        # Load the shoe icon image
        carrom_icon = Image.open("carrom_icon.png")
        carrom_icon = carrom_icon.resize((50, 50))
        carrom_icon = ImageTk.PhotoImage(carrom_icon)

        # Add a button with shoe icon on the left side of the text
        carrom_button = tk.Button(home_frame, text=" Carrom", image=carrom_icon, compound=tk.LEFT, font=('Arial', 15), fg='white', bg='#800080', width=185, height=150, command=lambda: self.carrom_page(username))
        carrom_button.image = carrom_icon
        carrom_button.place(x=15, y=canvas_height + 100)

        # Load the football icon image
        football_icon = Image.open("football_icon.png")
        football_icon = football_icon.resize((45, 45))
        football_icon = ImageTk.PhotoImage(football_icon)

        # Add a button with football icon on the left side of the text
        football_button = tk.Button(home_frame, text="Football", image=football_icon, compound=tk.LEFT, font=('Arial', 15), fg='white', bg='#800080', width=185, height=150,  command=lambda: self.football_page(username))
        football_button.image = football_icon
        football_button.place(x=225, y=canvas_height + 100)

        # Load the cricket icon image
        cricket_icon = Image.open("cricket_icon.png")
        cricket_icon = cricket_icon.resize((50, 50))
        cricket_icon = ImageTk.PhotoImage(cricket_icon)

        # Add a button with cricket icon on the left side of the text
        cricket_button = tk.Button(home_frame, text="Cricket", image=cricket_icon, compound=tk.LEFT, font=('Arial', 15), fg='white', bg='#800080', width=185, height=150, command=lambda: self.cricket_page(username))
        cricket_button.image = cricket_icon
        cricket_button.place(x=435, y=canvas_height + 100)

        # Load the jersey icon image
        chess_icon = Image.open("chess_icon.png")
        chess_icon = chess_icon.resize((50, 50))
        chess_icon = ImageTk.PhotoImage(chess_icon)

        # Add a button with jersey icon on the left side of the text
        chess_button = tk.Button(home_frame, text="Chess", image=chess_icon, compound=tk.LEFT, font=('Arial', 15), fg='white', bg='#800080', width=185, height=150, command=lambda: self.chess_page(username))
        chess_button.image = chess_icon
        chess_button.place(x=15, y=canvas_height + 280)

        # Load the badminton icon image
        badminton_icon = Image.open("badminton_icon.png")
        badminton_icon = badminton_icon.resize((50, 50))
        badminton_icon = ImageTk.PhotoImage(badminton_icon)

        # Add a button with badminton icon on the left side of the text
        badminton_button = tk.Button(home_frame, text=" Badminton", image=badminton_icon, compound=tk.LEFT, font=('Arial', 15), fg='white', bg='#800080', width=185, height=150,command=lambda: self.badminton_page(username))
        badminton_button.image = badminton_icon
        badminton_button.place(x=225, y=canvas_height + 280)

        
        home_frame.pack(pady=0)

    def publish_ad_page(self):
        global photo_image_1  # Make photo_image_1 and photo_image_2 global variables

        def upload_image1():
            global photo_image_1
            global filename1  # Use the nonlocal keyword to modify the photo_image_1 variable from the outer scope
            filename1 = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("Image Files", "*.jpg *.png *.jpeg"), ("All Files", "*.*")))
            if filename1:
                # Load the selected image into a PhotoImage object
                image = Image.open(filename1)
                image = image.resize((200, 200))  # Resize the image to fit the frame
                photo_image_1 = ImageTk.PhotoImage(image)

                # Display the image in the image frame
                image_label_1.config(image=photo_image_1)
                image_label_1.image = photo_image_1  # Keep a reference to prevent garbage collection


        self.delete_pages()

        publish_ad_frame = tk.Frame(self.main_frame, bg="#121212")
        publish_ad_frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas with a scrollbar
        canvas = tk.Canvas(publish_ad_frame, bg="#121212")
        scrollbar = tk.Scrollbar(publish_ad_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Bind mouse wheel event to canvas for scrolling
        canvas.bind("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        # Create a frame inside the canvas to hold the content
        content_frame = tk.Frame(canvas, bg="#121212")
        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

        heading_label = tk.Label(content_frame, text="Upload Your Ad:", font=('Arial', 16), fg="white", bg="#121212")
        heading_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # Image 1
        image_frame_1 = tk.Frame(content_frame, bg="#212121", width=200, height=200)
        image_frame_1.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        # Create a label to display the image
        image_label_1 = tk.Label(image_frame_1, bg="#212121")
        image_label_1.place(relx=0, rely=0)

        upload_button_1 = tk.Button(content_frame, text="Upload Image", command=upload_image1, font=('Arial', 12), bg="#800080", fg="white")
        upload_button_1.grid(row=1, column=1, padx=20, pady=10, sticky="w")


        # Title
        title_label = tk.Label(content_frame, text="Title:", font=('Arial', 14), fg="white", bg="#121212")
        title_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        title_entry = tk.Entry(content_frame, font=('Arial', 12), bg="#212121", fg="white", width=30)
        title_entry.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        # Description
        description_label = tk.Label(content_frame, text="Description:", font=('Arial', 14), fg="white", bg="#121212")
        description_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        description_entry = tk.Text(content_frame, font=('Arial', 12), bg="#212121", fg="white", height=4, width=50)
        description_entry.grid(row=5, column=0, padx=20, pady=5, sticky="w")

        # Categories
        categories_label = tk.Label(content_frame, text="Category:", font=('Arial', 14), fg="white", bg="#121212")
        categories_label.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        category_style = ttk.Style()
        if not category_style.theme_names():
            category_style.theme_create("combostyle_publish", parent="alt", settings={"TCombobox": {"configure": {"fieldbackground": "#212121", "foreground": "white"}}})
            category_style.theme_use("combostyle_publish")
        categories1 = ["Carrom", "Football", "Cricket", "Chess", "Badminton"]
        category_combobox1 = ttk.Combobox(content_frame, values=categories1, font=('Arial', 12), state="readonly", width=27)
        category_combobox1.grid(row=7, column=0, padx=20, pady=5, sticky="w")
        category_combobox1.bind("<FocusIn>", lambda e: category_combobox1.configure(foreground="black"))
        category_combobox1.bind("<FocusOut>", lambda e: category_combobox1.configure(foreground="white"))

        # Price for 1 days
        price_1days_label = tk.Label(content_frame, text="Price for 1 Days:", font=('Arial', 14), fg="white", bg="#121212")
        price_1days_label.grid(row=8, column=0, padx=20, pady=10, sticky="w")
        price_entry = tk.Entry(content_frame, font=('Arial', 12), bg="#212121", fg="white", width=30)
        price_entry.grid(row=9, column=0, padx=20, pady=5, sticky="w")

        def publish_ad(username, filename1):
            # Retrieve data from the entry fields
            title = title_entry.get()
            description = description_entry.get("1.0", tk.END)  # Get text from Tkinter Text widget
            category = category_combobox1.get()
            price = float(price_entry.get())

            # Convert the images to bytes
            with open(filename1, 'rb') as file1:
                image_data_1 = file1.read()
                

            # Insert data into the database
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Annsh@10",
                    database="student"
                )
                cursor = conn.cursor()

                # Fetch phone number of the user from student_login table
                phone_number_query = "SELECT phone_no FROM student_login WHERE username = %s"
                cursor.execute(phone_number_query, (username,))
                phone_number = cursor.fetchone()[0] 

                # Define the SQL query for inserting data
                sql = "INSERT INTO ad_table (username, title, description, category, price, image1,phoneno) VALUES (%s, %s, %s, %s, %s, %s,%s)"
                values = (username, title, description, category, price, image_data_1,phone_number)

                # Execute the SQL query
                cursor.execute(sql, values)

                # Commit the transaction
                conn.commit()

                # Close the cursor and connection
                cursor.close()
                conn.close()

                # Show a success message
                messagebox.showinfo("Success", "Ad Uploaded successfully!")

            except mysql.connector.Error as err:
                # Handle any errors
                messagebox.showerror("Error", f"Error: {err}")

        # Publish button
        publish_button = tk.Button(content_frame, text="Upload", font=('Arial', 12), bg="#800080", fg="white", width=20, height=2, command=lambda: publish_ad(self.username, filename1))
        publish_button.grid(row=13, column=0, padx=20, pady=10, sticky="w")


    def view_ad(self, ad,username):
        # Function to handle the Rent Now button click
        self.delete_pages()
        def generate_order_id():
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            unique_id = uuid.uuid4().hex[:6]  # Generate a random hex string of length 6
            order_id = f"ORDER-{timestamp}-{unique_id}"
            return order_id

        def rent_now(ad,username):
            # Convert string dates to date objects
            start_date_str = self.start_date_entry.get_date()
            end_date_str = self.end_date_entry.get_date()
           
            if start_date_str and end_date_str:
                start_date = datetime.strptime(start_date_str, "%m/%d/%y")
                end_date = datetime.strptime(end_date_str, "%m/%d/%y")

                if end_date >= start_date:
                    # Calculate the price based on the selected dates
                    price_per_day = ad[1]  # Example price per day
                    num_days = (end_date - start_date).days + 1
                    total_price = price_per_day * num_days

                    # Generate order ID
                    order_id = generate_order_id()

                    # Function to redirect to payment page and start Flask server
                    def redirect_to_payment(amount):
                        # Define the URL of your Flask payment page
                        payment_url = f"http://127.0.0.1:5000/?amount={amount}/"

                        # Open the payment URL in the default web browser
                        webbrowser.open(payment_url)

                        # Start the Flask server in a subprocess
                        flask_process = subprocess.Popen(['python', 'payment.py'])

                        # Wait for a short time to ensure the server starts up
                        time.sleep(2)

                    def get_amount():
                        # Prompt the user to enter the amount
                        redirect_to_payment(total_price)

                    # Create a new Tkinter frame to display rental details
                    global rental_window
                    rental_window = tk.Toplevel(self.master)
                    rental_window.title("Rental Details")
                    rental_window.geometry("600x400")
                    rental_window.configure(bg="#212121")

                    detail_label = tk.Label(rental_window, text=f"Title:{ad[0]}.", font=('Arial', 16), fg="white",bg="#212121")
                    detail_label.pack(anchor='w', padx=10, pady=5)

                    # Display rental details
                    detail_label = tk.Label(rental_window, text=f"Rent from {start_date} to {end_date}.", font=('Arial', 16), fg="white",bg="#212121")
                    detail_label.pack(anchor='w', padx=10, pady=5)

                    detail_label = tk.Label(rental_window, text=f"Total Price: ₹{total_price}.", font=('Arial', 16), fg="white",bg="#212121")
                    detail_label.pack(anchor='w', padx=10, pady=5)

                    detail_label = tk.Label(rental_window, text=f"Order ID: {order_id}", font=('Arial', 16), fg="white",bg="#212121")
                    detail_label.pack(anchor='w', padx=10, pady=5)

                    # Add button to proceed to payment
                    payment_button = tk.Button(rental_window, text="Pay with Razorpay", font=('Arial', 14), bg="#800080", fg="white", width=20, command=get_amount)
                    payment_button.pack(side='top', anchor='center', padx=10, pady=10)

                    def confirm_payment():
                        # Insert order details into the database
                        # Display success message or handle errors as needed
                        #Insert order details into the database
                                
                                try:
                                    conn = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        password="Annsh@10",
                                        database="student"
                                    )
                                    cursor = conn.cursor()

                                    # Define the SQL query for inserting data into the order_table
                                    sql = """INSERT INTO order_table (order_id, username, title, description, price, start_date, end_date, num_of_days,publisher_name,publisher_phone) 
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"""
                                    values = (order_id, username, ad[0], ad[2], total_price, start_date, end_date, num_days,ad[4],ad[5])
                                    cursor.execute(sql, values)

                                    # Commit the transaction
                                    conn.commit()

                                    # Close the cursor and connection
                                    cursor.close()
                                    conn.close()

                                    # Show a message indicating that details have been successfully added to the database
                                    messagebox.showinfo("Success", "Order has been successfully placed.")

                                except mysql.connector.Error as err:
                                    # Handle any errors that occur during the database operation
                                    messagebox.showerror("Error", f"Database error: {err}")
                                rental_window.destroy()
                    

                    def listen_for_payment_notification():
                        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        server_socket.bind(('127.0.0.1', 5555))  # Same IP address and port as Flask server
                        server_socket.listen(1)
                        while True:
                            client_socket, address = server_socket.accept()
                            data = client_socket.recv(1024)
                            if data == b'payment_success':
                                confirm_payment()
                            client_socket.close()

                    # Start a thread to listen for payment notifications
                    notification_thread = Thread(target=listen_for_payment_notification)
                    notification_thread.start()
                                        
                else:
                    messagebox.showerror("Error", "End date cannot be before the start date.")
            else:
                messagebox.showerror("Error", "Please select both start and end dates.")

        # Create a new frame for viewing the ad
        view_ad_frame = tk.Frame(self.main_frame, bg="#121212")
        view_ad_frame.pack(fill=tk.BOTH, expand=True)

        # Add a canvas for scrolling
        canvas = tk.Canvas(view_ad_frame, bg="#121212")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar for the canvas
        scrollbar = tk.Scrollbar(view_ad_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the content
        content_frame = tk.Frame(canvas, bg="#121212")
        canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

        # Function to update canvas scroll region
        def on_content_configure(event):
            canvas.configure(scrollregion=canvas.bbox(tk.ALL))

        content_frame.bind("<Configure>", on_content_configure)

        # Add back button
        back_button = tk.Button(content_frame, text="Back", command=lambda: self.return_to_home(view_ad_frame), font=('Arial', 12), bg="#800080", fg="white", width=15, height=2)
        back_button.grid(row=0, column=2, padx=5, pady=5)
        view_ad_label = tk.Label(content_frame, text="Product Page Content:", font=('Arial', 20), fg="white", bg="#121212")
        view_ad_label.grid(row=0, column=0, padx=5, pady=5)

        # Display the image
        image_data = ad[3]  # Assuming ad[2] contains the image data
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((200, 200))  # Adjust size as needed
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(content_frame, image=photo_image, bg="#121212")
        image_label.image = photo_image
        image_label.grid(row=1, column=0, padx=5, pady=10, sticky="w")

        # Display the title of the ad
        title_label = tk.Label(content_frame, text=f"Title: {ad[0]}", font=('Arial', 16), bg="#121212", fg="white")
        title_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Display the description of the ad if available
        if len(ad) > 2:
            description_label = tk.Label(content_frame, text=f"Description: {ad[2]}", font=('Arial', 16), bg="#121212", fg="white")
            description_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        # Debugging print
        else:
            print("No description available")

        # Display the username of the publisher
        if len(ad) > 4:
            published_by_label = tk.Label(content_frame, text=f"Published By: {ad[4]}", font=('Arial', 16), bg="#121212", fg="white")
            published_by_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")


        # Add labels and entries for start and end dates
        start_date_label = tk.Label(content_frame, text="Start Date:", font=('Arial', 12), bg="#121212", fg="white")
        start_date_label.grid(row=5, column=0, padx=5, pady=10, sticky="w")
        self.start_date_entry = Calendar(content_frame)
        self.start_date_entry.grid(row=5, column=1, padx=5, pady=10, sticky="w")

        end_date_label = tk.Label(content_frame, text="End Date:", font=('Arial', 12), bg="#121212", fg="white")
        end_date_label.grid(row=6, column=0, padx=5, pady=10, sticky="w")
        self.end_date_entry = Calendar(content_frame)
        self.end_date_entry.grid(row=6, column=1, padx=5, pady=10, sticky="w")

        # Display the original price
        original_price_label = tk.Label(content_frame, text=f"Original Price: ₹{ad[1]}", font=('Arial', 16), bg="#121212", fg="white")
        original_price_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        # Rent Now button
        rent_now_button = tk.Button(content_frame, text="Rent Now", font=('Arial', 12), bg="#800080", fg="white", width=15, height=2,command=lambda:rent_now(ad, username))
        rent_now_button.grid(row=8, column=0, padx=5, pady=5, sticky="w")




    def perform_search(self):
        # Placeholder for search functionality
        print("Performing search...")

    def display_profile_data(self, username):
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )

            # Create a cursor
            cursor = conn.cursor()

            # Prepare the SQL query to fetch profile data
            sql = "SELECT * FROM student_login WHERE username = %s"
            cursor.execute(sql, (username,))

            # Fetch the data
            profile_data = cursor.fetchone()

            # Check if data is retrieved
            if profile_data:
                # Populate the text boxes/fields with the retrieved data
                self.username_entry.delete(0, tk.END)
                self.username_entry.insert(0, profile_data[0])  # Assuming username is the first column

                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, profile_data[1])  # Assuming password is the second column

                self.phone_entry.delete(0, tk.END)
                self.phone_entry.insert(0, profile_data[2])  # Assuming phone_no is the third column

                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, profile_data[3])  # Assuming email_id is the fourth column

                
                # Fetch years and branches from the database
                cursor.execute("SELECT DISTINCT year FROM student_login WHERE year IS NOT NULL ORDER BY year")
                years_result = cursor.fetchall()
                years = [data[0] for data in years_result]  # Fetch all unique years

                cursor.execute("SELECT DISTINCT branch FROM student_login WHERE branch IS NOT NULL ORDER BY branch")
                branches_result = cursor.fetchall()
                branches = [data[0] for data in branches_result]  # Fetch all unique branches

                # Set the values of the year and branch comboboxes
                default_years = ["FE", "SE", "TE", "Final year"]
                default_branches = ["Comps", "IT", "AIML", "Mech", "DS", "CIVIL"]

                year_values = default_years + [year for year in years if year not in default_years]
                branch_values = default_branches + [branch for branch in branches if branch not in default_branches]

                if year_values:
                    self.year_combobox['values'] = year_values
                    year_value = profile_data[6]  # Assuming year is at index 6
                    if year_value in year_values:
                        self.year_combobox.set(year_value)

                if branch_values:
                    self.branch_combobox['values'] = branch_values
                    branch_value = profile_data[5]  # Assuming branch is at index 5
                    if branch_value in branch_values:
                        self.branch_combobox.set(branch_value)

            # Close the cursor and connection
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            # Handle any errors that occur during the database operation
            print("Error:", err)

    def profile_page(self,username):
        # Delete existing pages
        self.delete_pages()

        # Create a new frame for the profile page
        profile_frame = tk.Frame(self.main_frame, bg="#121212")
        profile_frame.pack(fill=tk.BOTH, expand=True)

        # Add label "Your Profile"
        profile_label = tk.Label(profile_frame, text="Your Profile:", font=('Helvetica', 24), fg="white", bg="#121212")
        profile_label.place(x=20, y=20)

        # Create a canvas for the circular image box
        self.canvas = tk.Canvas(profile_frame, bg="#212121", width=100, height=100, highlightthickness=0)
        self.canvas.place(x=20, y=60)
        
        
        # profile_label1 = tk.Label(profile_frame, bg="blue",width=20,height=5)
        # profile_label1.place(x=20, y=400)
        #Draw a circular box on the canvas
        self.image = Image.open("user_logo.png").resize((100, 100), Image.LANCZOS)  # Create a blank image
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(50, 50, image=self.photo_image)

        # # Add upload button
        # upload_button = tk.Button(profile_frame, text="Upload", font=('Arial', 12), bg="#800080", fg="white", width=10, height=1, command=self.upload_prof_image)
        # upload_button.place(x=200, y=90)

        # Add username label and entry
        username_label = tk.Label(profile_frame, text="Username:", font=('Arial', 14), fg="white", bg="#121212")
        username_label.place(x=20, y=180)
        self.username_entry = tk.Entry(profile_frame, font=('Arial', 12), bg="#212121", fg="white")
        self.username_entry.place(x=20, y=210)

        # Add password label and entry
        password_label = tk.Label(profile_frame, text="Password:", font=('Arial', 14), fg="white", bg="#121212")
        password_label.place(x=400, y=180)
        self.password_entry = tk.Entry(profile_frame, show="*", font=('Arial', 12), bg="#212121", fg="white")
        self.password_entry.place(x=400, y=210)

        phone_label = tk.Label(profile_frame, text="Phone No.:", font=('Arial', 14), fg="white", bg="#121212")
        phone_label.place(x=20, y=260)
        self.phone_entry = tk.Entry(profile_frame, font=('Arial', 12), bg="#212121", fg="white")
        self.phone_entry.place(x=20, y=290)

        # Add email label and entry
        email_label = tk.Label(profile_frame, text="Email:", font=('Arial', 14), fg="white", bg="#121212")
        email_label.place(x=400, y=260)
        self.email_entry = tk.Entry(profile_frame, font=('Arial', 12), bg="#212121", fg="white")
        self.email_entry.place(x=400, y=290)

        # Add year label and combobox
        year_label = tk.Label(profile_frame, text="Year:", font=('Arial', 14), fg="white", bg="#121212")
        year_label.place(x=20, y=330)
        self.year_combobox = ttk.Combobox(profile_frame, values=["FE", "SE", "TE", "Final year"], font=('Arial', 12), state="readonly")
        self.year_combobox.place(x=20, y=360)

        # Add branch label and combobox
        branch_label = tk.Label(profile_frame, text="Branch:", font=('Arial', 14), fg="white", bg="#121212")
        branch_label.place(x=400, y=330)
        self.branch_combobox = ttk.Combobox(profile_frame, values=["Comps", "IT", "AIML", "Mech", "DS", "CIVIL"], font=('Arial', 12), state="readonly")
        self.branch_combobox.place(x=400, y=360)

        update_button = tk.Button(profile_frame, text="Update", font=('Arial', 12), bg="#800080", fg="white",width=20,height=1,command=self.update_profile)
        update_button.place(x=200, y=480)

        self.display_profile_data(username)
        

    def update_profile(self):
        # Get the updated profile data from the entry fields and comboboxes
        updated_username = self.username_entry.get()
        updated_password = self.password_entry.get()
        updated_phone = self.phone_entry.get()
        updated_email = self.email_entry.get()
        updated_branch = self.branch_combobox.get()
        updated_year = self.year_combobox.get()
       

        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )

            # Create a cursor
            cursor = conn.cursor()

            # Prepare the SQL query to update the profile data
            sql = "UPDATE student_login SET password = %s, phone_no = %s, email_id = %s,branch = %s, year = %s WHERE username = %s"
            cursor.execute(sql, (updated_password, updated_phone, updated_email ,updated_branch, updated_year, updated_username))

            # Commit the changes
            conn.commit()

            # Display a success message
            messagebox.showinfo("Success", "Profile updated successfully")

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            # Handle any errors that occur during the database operation
            messagebox.showerror("Error", f"Failed to update profile: {err}")

    def upload_prof_image(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("Image Files", "*.jpg *.png *.jpeg"), ("All Files", "*.*")))
        if filename:
            # Load the selected image into a PhotoImage object
            image = Image.open(filename)
            image = image.resize((100, 100))  # Resize the image to fit the canvas
            self.photo_image = ImageTk.PhotoImage(image)

            # Display the image on the canvas
            self.canvas.create_image(50, 50, image=self.photo_image)



    def order_page(self):
        global total_amount
        order_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        lb = tk.Label(order_frame, text='Order Page', font=('Bold', 30), fg="white", bg="#121212")  # Darker text and background
        lb.pack()

        frame1 = tk.Frame(order_frame, bg="#8444FC", width=200, height=50)
        frame1.pack(side=tk.TOP,pady=10)
        # Create a Treeview widget to display orders
        tree = ttk.Treeview(order_frame)
        tree["columns"] = ("Title", "Description", "Publisher Name","Publisher Phoneno","Price", "Start Date", "End Date", "Remaining Days")

        # Define column headings
        tree.heading("#0", text="Order ID")
        # tree.heading("#1","Order ID", text="Order ID")
        tree.heading("Title", text="Title")
        tree.heading("Description", text="Description")
        tree.heading("Publisher Name", text="Publisher Name")
        tree.heading("Publisher Phoneno", text="Publisher Phoneno")
        tree.heading("Price", text="Price")
        tree.heading("Start Date", text="Start Date")
        tree.heading("End Date", text="End Date")
        tree.heading("Remaining Days", text="No of Days")

        tree.column("#0", width=200)  # Adjust the width of the first column (Order ID)
        tree.column("#1", width=150)  # Adjust the width of the "Title" column
        tree.column("#2", width=200)  # Adjust the width of the "Description" column
        tree.column("#3", width=100)  # Adjust the width of the "Publisher Name" column
        tree.column("#4", width=100)  # Adjust the width of the "Price" column
        tree.column("#5", width=100)  # Adjust the width of the "Start Date" column
        tree.column("#6", width=100)  # Adjust the width of the "End Date" column
        tree.column("#7", width=100)
        tree.column("#8", width=100)

        # Add a horizontal scrollbar
        scrollbar_x = tk.Scrollbar(order_frame, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the Treeview to use the horizontal scrollbar
        tree.configure(xscrollcommand=scrollbar_x.set)

        

        # Fetch orders from the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Fetch orders made by the logged-in user
            query = """SELECT order_id, title, description, publisher_name,publisher_phone, price, start_date, end_date, num_of_days 
                       FROM order_table 
                       WHERE username = %s"""
            cursor.execute(query, (self.username,))
            orders = cursor.fetchall()

            total_amount = sum(order[5] for order in orders)

            label1 = tk.Label(frame1, text=f"Total Amount: ₹{total_amount} ", fg="white", bg="#8444FC", font=('Arial', 18))
            label1.pack(padx=30,pady=35)

            # Check if there are no orders
            if not orders:
                # If there are no orders, display an empty table
                tree.insert("", "end", text="No data available")
            else:
                # Populate the Treeview with orders
                for order in orders:
                    tree.insert("", "end", text=order[0], values=(order[1], order[2], order[3], order[4], order[5], order[6], order[7],order[8]))

            # Commit and close
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    
        # Pack the Treeview
        tree.pack(expand=True, fill=tk.BOTH)

        order_frame.pack(pady=20)

    def my_ads_page(self):
        # # Placeholder for "Your Ad" label
        # your_ad_label = tk.Label(self.main_frame, text="Your Ad:", font=('Arial', 24), fg='white', bg='#121212')
        # your_ad_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)  # Sticky to the west (left), with padding

        # Create a canvas to contain the scrollable content
        canvas = tk.Canvas(self.main_frame, bg="#121212")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a frame inside the canvas to hold the content
        ads_frame = tk.Frame(canvas, bg="#121212")
        ads_frame.pack(fill=tk.BOTH, expand=True)

        # Add a vertical scrollbar
        scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Bind the canvas to the scrollbar
        canvas.create_window((0, 0), window=ads_frame, anchor=tk.NW)
        ads_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Add the "Your Ad" label inside the ads_frame
        your_ad_label = tk.Label(ads_frame, text="Your Ad:", font=('Arial', 24), fg='white', bg='#121212')
        your_ad_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Fetch ads published by the logged-in user from the database
            sql = "SELECT ad_id,title, price, image1 FROM ad_table WHERE username = %s"  # Assuming 'user_id' is the column for user identifier
            cursor.execute(sql, (self.username,))  # Assuming 'self.user_id' contains the user's identifier
            ads = cursor.fetchall()

            row_num = 1  # Start row from 0
            for ad in ads:
                ad_id = ad[0]
                # Create a rectangular frame for each ad
                rectangular_frame = tk.Frame(ads_frame, bg="#212121", width=700, height=150)
                rectangular_frame.grid(row=row_num, column=0, sticky="ew", padx=10, pady=10)

                # Display the image
                image_data = ad[3]
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((100, 100))  # Adjust size as needed
                photo_image = ImageTk.PhotoImage(image)
                image_label = tk.Label(rectangular_frame, image=photo_image, bg="#212121")
                image_label.image = photo_image
                image_label.grid(row=0, column=0, padx=10, pady=10)

                # Display the title
                title_label = tk.Label(rectangular_frame, text=ad[1], font=('Arial', 16), fg='white', bg='#212121')
                title_label.grid(row=0, column=1, padx=5, pady=10)

                # Display the price
                price_label = tk.Label(rectangular_frame, text=f"Price: {ad[2]}", font=('Arial', 16), fg='white', bg='#212121')
                price_label.grid(row=1, column=0, padx=5, pady=10)

                edit_button = tk.Button(rectangular_frame, text="Edit", font=('Arial', 14), width=10,fg='white', bg='#008080', command=lambda ad_id=ad_id: self.edit_ad(ad_id))
                edit_button.grid(row=1, column=5, padx=10, pady=10, sticky="se")

                # Add a delete button to delete the ad
                delete_button = tk.Button(rectangular_frame, text="Delete", font=('Arial', 14),width=10 ,fg='white', bg='#800080', command=lambda ad_id=ad_id: self.delete_ad(ad_id))
                delete_button.grid(row=1, column=4, padx=10, pady=10,sticky="se")

                # Increment row number after each ad
                row_num += 1

        except mysql.connector.Error as err:
            # Handle any errors
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

    
    def delete_ad(self, ad_id):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Delete the ad from the database based on its ID
            sql = "DELETE FROM ad_table WHERE ad_id = %s"
            cursor.execute(sql, (ad_id,))
            conn.commit()
            messagebox.showinfo("Success", "Ad deleted successfully.")

        except mysql.connector.Error as err:
            # Handle any errors
            messagebox.showerror("Error", f"Error: {err}")


        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()



    def edit_ad(self, ad_id):
        global photo_image_1, photo_image_2  # Make photo_image_1 and photo_image_2 global variables

        def upload_image1():
            global photo_image_1
            global filename1  # Use the nonlocal keyword to modify the photo_image_1 variable from the outer scope
            filename1 = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("Image Files", "*.jpg *.png *.jpeg"), ("All Files", "*.*")))
            if filename1:
                # Load the selected image into a PhotoImage object
                image = Image.open(filename1)
                image = image.resize((200, 200))  # Resize the image to fit the frame
                photo_image_1 = ImageTk.PhotoImage(image)

                # Display the image in the image frame
                image_label_1.config(image=photo_image_1)
                image_label_1.image = photo_image_1  # Keep a reference to prevent garbage collection

       

        self.delete_pages()

        publish_ad_frame = tk.Frame(self.main_frame, bg="#121212")
        publish_ad_frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas with a scrollbar
        canvas = tk.Canvas(publish_ad_frame, bg="#121212")
        scrollbar = tk.Scrollbar(publish_ad_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Bind mouse wheel event to canvas for scrolling
        canvas.bind("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        # Create a frame inside the canvas to hold the content
        content_frame = tk.Frame(canvas, bg="#121212")
        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

        heading_label = tk.Label(content_frame, text="Edit Your Ad:", font=('Arial', 16), fg="white", bg="#121212")
        heading_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # Image 1
        image_frame_1 = tk.Frame(content_frame, bg="#212121", width=200, height=200)
        image_frame_1.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        # Create a label to display the image
        image_label_1 = tk.Label(image_frame_1, bg="#212121")
        image_label_1.place(relx=0, rely=0)

        upload_button_1 = tk.Button(content_frame, text="Upload Image", command=upload_image1, font=('Arial', 12), bg="#800080", fg="white")
        upload_button_1.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Title
        title_label = tk.Label(content_frame, text="Title:", font=('Arial', 14), fg="white", bg="#121212")
        title_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        title_entry = tk.Entry(content_frame, font=('Arial', 12), bg="#212121", fg="white", width=30)
        title_entry.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        # Description
        description_label = tk.Label(content_frame, text="Description:", font=('Arial', 14), fg="white", bg="#121212")
        description_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        description_entry = tk.Text(content_frame, font=('Arial', 12), bg="#212121", fg="white", height=4, width=50)
        description_entry.grid(row=5, column=0, padx=20, pady=5, sticky="w")

        # Categories
        categories_label1 = tk.Label(content_frame, text="Category:", font=('Arial', 14), fg="white", bg="#121212")
        categories_label1.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        category_style = ttk.Style()
        if not category_style.theme_names():
            category_style.theme_create("combostyle_publish", parent="alt", settings={"TCombobox": {"configure": {"fieldbackground": "#212121", "foreground": "white"}}})
            category_style.theme_use("combostyle_publish")
        categories1 = ["Carrom", "Football", "Cricket", "Chess", "Badminton"]
        category_combobox = ttk.Combobox(content_frame, values=categories1, font=('Arial', 12), state="readonly", width=27)
        category_combobox.grid(row=7, column=0, padx=20, pady=5, sticky="w")
        category_combobox.bind("<FocusIn>", lambda e: category_combobox.configure(foreground="black"))
        category_combobox.bind("<FocusOut>", lambda e: category_combobox.configure(foreground="white"))

        # Price for 1 days
        price_1days_label = tk.Label(content_frame, text="Price for 1 Days:", font=('Arial', 14), fg="white", bg="#121212")
        price_1days_label.grid(row=8, column=0, padx=20, pady=10, sticky="w")
        price_entry = tk.Entry(content_frame, font=('Arial', 12), bg="#212121", fg="white", width=30)
        price_entry.grid(row=9, column=0, padx=20, pady=5, sticky="w")

        def update_ad(ad_id, filename1):
            # Retrieve data from the entry fields
            title = title_entry.get()
            description = description_entry.get("1.0", tk.END)  # Get text from Tkinter Text widget
            category = category_combobox.get()
            price = float(price_entry.get())

            # Convert the images to bytes
            with open(filename1, 'rb') as file1:
                image_data_1 = file1.read()
                

            # Update data in the database
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Annsh@10",
                    database="student"
                )
                cursor = conn.cursor()

                # Define the SQL query for updating data
                sql = "UPDATE ad_table SET title=%s, description=%s, category=%s, price=%s, image1=%s WHERE ad_id=%s"
                values = (title, description, category, price, image_data_1, ad_id)

                # Execute the SQL query
                cursor.execute(sql, values)

                # Commit the transaction
                conn.commit()

                # Close the cursor and connection
                cursor.close()
                conn.close()

                # Show a success message
                messagebox.showinfo("Success", "Ad updated successfully!")

            except mysql.connector.Error as err:
                # Handle any errors
                messagebox.showerror("Error", f"Error: {err}")

            
        update_button = tk.Button(content_frame, text="Update", font=('Arial', 12), bg="#800080", fg="white", width=20, height=2, command=lambda: update_ad(ad_id, filename1))
        update_button.grid(row=11, column=0, padx=20, pady=10, sticky="w")

    



    def about_page(self):
        about_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        # Create a Text widget
        about_text = """
        About Us:-

        Welcome to Rental Hub, the premier platform for renting sports items within our college campus!

        At Rental Hub, we understand the importance of staying active and engaged in sports activities. That's why we've created a convenient and hassle-free way for students to access a wide range of sports equipment right here on campus.

        Our Mission:

        Our mission is to promote a healthy and active lifestyle among college students by providing easy access to high-quality sports equipment. We believe that everyone should have the opportunity to participate in sports and physical activities, regardless of their budget or access to resources.

        How It Works:

        Using Rental Hub is simple. Students can browse through our extensive collection of sports items, including everything from basketballs and footballs to tennis rackets and yoga mats. Once they find the equipment they need, they can easily rent it for a specified period, whether it's for a day, a week, or longer.

        Why Choose Us

        Convenience: No need to purchase expensive sports gear or travel off-campus to rent equipment. Everything you need is right here at your fingertips.
        Affordability: We offer competitive rental rates that fit within a student's budget, making it easy to access the equipment you need without breaking the bank.
        Quality: All of our sports items are carefully inspected and maintained to ensure they meet the highest standards of quality and safety.
        Community: By using [Your App Name], you're supporting a vibrant community of sports enthusiasts right here on campus.
        """

        text_scroll = tk.Scrollbar(about_frame, orient=tk.VERTICAL)
        about_label = tk.Text(about_frame, wrap=tk.WORD, yscrollcommand=text_scroll.set, bg="#121212", fg="white", font=('Arial', 12))
        about_label.insert(tk.END, about_text)
        about_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        text_scroll.config(command=about_label.yview)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        about_frame.pack(pady=20)
        # lb = tk.Label(about_frame, text='About Page', font=('Bold', 30), fg="white", bg="#121212")  # Darker text and background
        # lb.pack()
        # about_frame.pack(pady=20)


      # Placeholder for logout action
    def rentee_page(self):
        rentee_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        lb = tk.Label(rentee_frame, text='Your Rentee Page', font=('Bold', 30), fg="white", bg="#121212")  # Darker text and background
        lb.pack()

        # Create a Treeview widget to display rental details
        tree = ttk.Treeview(rentee_frame)
        tree["columns"] = ("username", "Title", "Description", "Price", "Start Date", "End Date", "Num of Days")

        # Define column headings
        tree.heading("#0", text="Order ID")  # Assuming there's an order ID associated with rentals
        tree.heading("username", text="Rentee Username")
        tree.heading("Title", text="Title")
        tree.heading("Description", text="Description")
        tree.heading("Price", text="Price")
        tree.heading("Start Date", text="Start Date")
        tree.heading("End Date", text="End Date")
        tree.heading("Num of Days", text="Num of Days")

        # Add a horizontal scrollbar
        scrollbar_x = tk.Scrollbar(rentee_frame, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the Treeview to use the horizontal scrollbar
        tree.configure(xscrollcommand=scrollbar_x.set)

        # Fetch rental details from the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Fetch rental details associated with the logged-in user's account
            query = """SELECT order_id,username, title, description, price, start_date, end_date, num_of_days 
                    FROM order_table 
                    WHERE publisher_name = %s"""
            cursor.execute(query, (self.username,))
            rentals = cursor.fetchall()

            # Check if there are no rentals
            if not rentals:
                # If there are no rentals, display an empty message
                tree.insert("", "end", text="No rentals available")
            else:
                # Populate the Treeview with rental details
                for rental in rentals:
                    tree.insert("", "end", text=rental[0], values=(rental[1], rental[2], rental[3], rental[4], rental[5], rental[6], rental[7]))

            # Commit and close
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        # Set column widths to fit content more closely
        tree.column("#0", width=100)  # Adjust the width of the first column (Order ID)
        tree.column("#1", width=150)  # Adjust the width of the "Rentee Username" column
        tree.column("#2", width=150)  # Adjust the width of the "UPI ID" column
        tree.column("#3", width=200)  # Adjust the width of the "Title" column
        tree.column("#4", width=250)  # Adjust the width of the "Description" column
        tree.column("#5", width=100)  # Adjust the width of the "Price" column
        tree.column("#6", width=100)  # Adjust the width of the "Start Date" column
        tree.column("#7", width=100)  # Adjust the width of the "End Date" column  

        # Pack the Treeview
        tree.pack(expand=True, fill=tk.BOTH)

        rentee_frame.pack(pady=20)

    def delete_pages(self):
        for child in self.main_frame.winfo_children():
            child.destroy()

    def terms_conditions_page(self):
        # Create a new Toplevel window for the Terms & Conditions page
        terms_window = tk.Toplevel(self.master)
        terms_window.title("Terms & Conditions")
        terms_window.geometry("850x600")
        terms_window.config(bg="#121212")  # Set the window size

        hlabel= tk.Label(terms_window,text="Terms & Condition:",font=('Arial',20,'underline'),bg="#121212",fg="yellow")
        hlabel.pack(padx=5,pady=5)
        # Add text for Terms & Conditions
        terms_text = """
        1.)Users of the app must be currently enrolled students at a recognized educational institution.

        2.)Registration:
            Users are required to register using their valid student credentials to access the app'sfeatures.
            Users are responsible for returning rented equipment by the agreed-upon date and time to avoid late fees.

        3.)Late Returns:
            Late returns will result in additional charges, as outlined in the app's fee structure.
            Equipment Condition:

        4.)Users must return rented equipment in the same condition as received, with normal wear and tear 	expected.

        5.)Damages beyond normal wear and tear will result in paying for the damages.

        6.)The app and its operators are not liable for any accidents, injuries, or damages incurred during the use of rented equipment.
        """
        text_scroll = tk.Scrollbar(terms_window, orient=tk.VERTICAL)
        terms_label = tk.Text(terms_window, wrap=tk.WORD, yscrollcommand=text_scroll.set, bg="#121212", fg="white", font=('Arial', 16))
        terms_label.insert(tk.END, terms_text)
        terms_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        text_scroll.config(command=terms_label.yview)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)    

if __name__ == "__main__":
    root = ModernTk()
    app = RentalApplication(root)
    root.run()
