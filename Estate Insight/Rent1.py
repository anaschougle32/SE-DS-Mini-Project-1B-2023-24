import subprocess
import tkinter as tk
from tkinter import Button, Frame, Label, Entry, PhotoImage, Canvas, Scrollbar
import mysql.connector
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import *


class buy1:
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
                    anchor=tk.W,
                    relief=tk.SUNKEN,
                    bd=1,
                    pady=3)
        one.pack(fill=tk.X, side=tk.TOP)
        name_label = Label(one,
                           text='Insert Name',
                           bg='#B31312',
                           fg='white',
                           bd=0)
        name_label.place(relx=0.85, rely=0.1)  # name
        down_arrow = tk.Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
        down_arrow.pack()
        down_arrow.menu = tk.Menu(down_arrow)
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
        icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, icon)

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

        # Create a frame for the search bar
        search_frame = Frame(root, bg="white", bd=0, relief=tk.GROOVE)
        search_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Add a label for the search bar
        search_label = Label(search_frame, text="Search:", bg="white")
        search_label.pack(side=tk.LEFT, padx=(10, 5), pady=5)

        # Add an entry widget for the search query
        self.search_entry = Entry(search_frame, bg="white", bd=1, relief=tk.SOLID)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5), pady=5)

        # Add a button for the search action
        search_button = Button(search_frame, text="Search", bg="#B31312", fg="white", command=self.perform_search)
        search_button.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        self.canvas = Canvas(root, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(root, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.data_frame = Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.data_frame, anchor=tk.NW)

        # Connect to the database
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#22107031#',
            database='estateinsight'
        )

        # Fetch data from the database
        self.fetch_data()

        # Bind the canvas to the scrollbar
        self.data_frame.bind("<Configure>", self.on_frame_configure)
    def main_view1(self,propertyname):
        bs = propertyname
        subprocess.call(["python", "main_view.py", bs])
    def fetch_data(self):
        global property_name_text
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()

                # Execute your query to fetch data from the database
                cursor.execute("SELECT propertyname, username, price, address, photo1 FROM rent")

                # Fetch all rows
                rows = cursor.fetchall()

                # Process the fetched rows and create frames
                for i, row in enumerate(rows):
                    frame = Frame(self.data_frame, bg="white", bd=1, relief=tk.GROOVE,
                                  highlightbackground='black', highlightthickness=1, width=600,
                                  height=200)  # Increased width and height here
                    frame.grid(row=i, column=0, padx=10, pady=10, sticky=tk.W)

                    propertyname, username, price, address, photo1 = row

                    property_name_text = f"Name: {propertyname}"
                    label1 = Label(frame, text=property_name_text, font=("Arial", 15), bg="white")
                    label1.grid(row=0, column=1, sticky=tk.W)

                    label = Label(frame, text=f"Owner name: {username}", font=("Arial", 12), bg="white")
                    label.grid(row=1, column=1, sticky=tk.W)

                    label = Label(frame, text=f"Price: {price}", font=("Arial", 15), bg="white")
                    label.grid(row=2, column=0, sticky=tk.W)

                    label = Label(frame, text=f"Address: {address}", font=("Arial", 12), bg="white")
                    label.grid(row=3, column=0, sticky=tk.W)

                    # Fetch and display image
                    self.display_image(frame, photo1)

                    # Add "View" button
                    view_button = Button(frame, text="View", bg="#B31312", fg="white", command=lambda prop=propertyname: self.main_view1(prop))
                    view_button.grid(row=4, column=0, pady=5, sticky=tk.W)

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)

    def display_image(self, frame, image_path):
        try:
            # Open image using PIL
            image = Image.open(image_path)

            # Resize image
            image.thumbnail((200, 200))

            # Convert Image object to PhotoImage object
            photo_image = ImageTk.PhotoImage(image)

            # Display image in label
            label = Label(frame, image=photo_image, bg="white")
            label.image = photo_image  # Keep a reference to the image
            label.grid(row=1, column=0, sticky=tk.W)

        except Exception as e:
            print("Error displaying image:", e)

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def perform_search(self):
        # Get the search query from the entry widget
        search_query = self.search_entry.get()

        # Process the search query (e.g., filter data based on the query)
        # You can add your search logic here

        # For demonstration, let's print the search query
        print("Search Query:", search_query)

    def home(self):
        self.root.destroy()
        subprocess.run(['python','Homepage1.py'])
        import Homepage1

    def buy(self):
        self.root.destroy()
        import buy1

    def sell(self):
        self.root.destroy()
        import Sell_1

    def rent(self):
        self.root.destroy()
        import Rent1

    def view_property(self):
        # Define the functionality for viewing a property
        pass

    def rentup(self):
        self.root.destroy()
        import Rent2

    def emi(self):
        import emi


root = tk.Tk()
obj = buy1(root)
root.mainloop()
