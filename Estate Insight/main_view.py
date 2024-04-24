from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
import mysql
from PIL import Image, ImageTk
import tkintermapview
import sys
bs = sys.argv[1]


class mainview:
    def __init__(self, root,propertyname):

        self.root = root
        self.propertyname = propertyname
        # setting up the app
        self.root = root
        # Connect to the MySQL database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#22107031#",
            database="estateinsight"
        )
        self.cursor = self.connection.cursor()

        font_info = ("Arial", 15, "bold")

        one = Label(self.root,
                    text="EstateInsight",
                    bg="#B31312",
                    fg="White",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=1,
                    pady=3)
        one.pack(fill=X, side=TOP)
        name_label = Label(one,
                           text='Insert Name',
                           bg='#B31312',
                           fg='white',
                           bd=0)
        name_label.place(relx=0.85, rely=0.1)  # name
        down_arrow = Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
        down_arrow.pack()
        down_arrow.menu = Menu(down_arrow)
        down_arrow["menu"] = down_arrow.menu
        down_arrow.menu.add_checkbutton(label="Profile")
        down_arrow.menu.add_checkbutton(label="Agent")
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
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)

        # setting up the toolbar for the app
        toolbar = Frame(root, bg="WHite", relief=GROOVE, bd=2, pady=2)
        printButt = Button(toolbar,
                           text="Home",
                           bg="white",
                           border=0,
                           activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)

        insertButt = Button(toolbar, text="Buy", bg="White", border=0, activebackground='#B67352')
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Sell", bg="White", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Rent", bg="White", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Wishlist", bg="White", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Help", bg="White", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)
        self.setup_info()

        # Fetch data from the database and populate entries
        self.fetch_data()

        # Frame 1 where image is to be viewed
        frame1 = Frame(root, width=300, height=300, bg="White", relief=GROOVE, bd=1)
        frame1.pack(side=LEFT, padx=40, pady=70)

        self.display_image_from_database(frame1)





    def open_mumbaimap_window(self):
        mapwidget = tkintermapview.TkinterMapView(tk)
        # Create a map widget for Mumbai
        marker_1 = mapwidget.set_address("kasarvadavli,thane,india", marker=True)
        marker_1.set_text("kasarvadavli,thane,india")

    def display_image_from_database(self, frame):
        try:
            cursor = self.connection.cursor()
            # Fetch image data from the database
            cursor.execute("SELECT photo1 FROM rent WHERE propertyname = %s", (self.propertyname,))
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
                print("No image data found for property ID:", self.propertyname)

        except Exception as e:
            print("Error displaying image:", e)

        # setting up all the info
    def setup_info(self):
        carp_fra = Frame(root, relief=GROOVE, bd=1, width=100, height=70)
        carp_fra.place(relx=0.4, rely=0.12)
        carp_lab = Label(carp_fra, bd=0, text="Carpet Area")
        carp_lab.place(relx=0.1, rely=0.1)
        self.carp_ent = Entry(carp_fra, bd=1, state=DISABLED, width=15)
        self.carp_ent.place(relx=0.01, rely=0.45)

        floor_fra = Frame(root, relief=GROOVE, bd=1, width=100, height=70)
        floor_fra.place(relx=0.55, rely=0.12)
        floor_lab = Label(floor_fra, bd=0, text="Floor")
        floor_lab.place(relx=0.1, rely=0.1)
        self.floor_ent = Entry(floor_fra, bd=1, state=DISABLED, width=15)
        self.floor_ent.place(relx=0.01, rely=0.45)

        trans_fra = Frame(root, relief=GROOVE, bd=1, width=100, height=70)
        trans_fra.place(relx=0.7, rely=0.12)
        trans_lab = Label(trans_fra, bd=0, text="Transaction Type")
        trans_lab.place(relx=0.03, rely=0.1)
        self.trans_ent = Entry(trans_fra, bd=1, state=DISABLED, width=15)
        self.trans_ent.place(relx=0.01, rely=0.45)

        stat_fra = Frame(root, relief=GROOVE, bd=1, width=100, height=70)
        stat_fra.place(relx=0.85, rely=0.12)
        stat_lab = Label(stat_fra, bd=0, text="Status")
        stat_lab.place(relx=0.1, rely=0.1)
        self.stat_ent = Entry(stat_fra, bd=1, state=DISABLED, width=15)
        self.stat_ent.place(relx=0.01, rely=0.45)

        # ***********************************************************************************

        info_fra = Frame(root, relief=GROOVE, bd=1, width=550, height=470)
        info_fra.place(relx=0.4, rely=0.24)

        more_lab = Label(info_fra, bd=0, text='More Details')
        more_lab.place(relx=0.01, rely=0.01)

        self.price_lab = Label(info_fra, bd=0, text='Price:')
        self.price_lab.place(relx=0.01, rely=0.08)
        self.price_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.price_ent.place(relx=0.08, rely=0.08)

        self.book_lab = Label(info_fra, bd=0, text='Booking Price:')
        self.book_lab.place(relx=0.01, rely=0.165)
        self.book_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.book_ent.place(relx=0.16, rely=0.165)

        self.add_lab = Label(info_fra, bd=0, text='Address:')
        self.add_lab.place(relx=0.01, rely=0.25)
        self.add_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.add_ent.place(relx=0.11, rely=0.25)

        self.land_lab = Label(info_fra, bd=0, text='Landmarks:')
        self.land_lab.place(relx=0.01, rely=0.37)
        self.land_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.land_ent.place(relx=0.13, rely=0.37)

        self.fur_lab = Label(info_fra, bd=0, text='Furnishing:')
        self.fur_lab.place(relx=0.01, rely=0.44)
        self.fur_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.fur_ent.place(relx=0.13, rely=0.44)

        self.floor_lab = Label(info_fra, bd=0, text='Flooring:')
        self.floor_lab.place(relx=0.01, rely=0.52)
        self.flooring_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.flooring_ent.place(relx=0.11, rely=0.52)

        self.type_lab = Label(info_fra, bd=0, text='Type of Ownership:')
        self.type_lab.place(relx=0.01, rely=0.59)
        self.type_ent = Entry(info_fra, bd=1, state=DISABLED, width=50)
        self.type_ent.place(relx=0.21, rely=0.59)

        self.over_lab = Label(info_fra, bd=0, text='Overlooking:')
        self.over_lab.place(relx=0.01, rely=0.67)
        self.over_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.over_ent.place(relx=0.15, rely=0.67)

        self.age_lab = Label(info_fra, bd=0, text='Age of Construction:')
        self.age_lab.place(relx=0.01, rely=0.75)
        self.age_ent = Entry(info_fra, bd=1, state=DISABLED, width=50)
        self.age_ent.place(relx=0.23, rely=0.75)

        self.water_lab = Label(info_fra, bd=0, text='Water Availaibility:')
        self.water_lab.place(relx=0.01, rely=0.83)
        self.water_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.water_ent.place(relx=0.2, rely=0.83)

        self.elec_lab = Label(info_fra, bd=0, text='Status of Electricity:')
        self.elec_lab.place(relx=0.01, rely=0.9)
        self.elec_ent = Entry(info_fra, bd=1, state=DISABLED, width=70)
        self.elec_ent.place(relx=0.22, rely=0.9)

        button = Button(root, text="Contact Owner", bg='#B31312', fg='White', pady=5)
        button.place(relx=0.08, rely=0.87)

        that_button = Button(root,
                             text="View Location",
                             foreground='#f7f7f7',
                             background='#B31312',
                             activeforeground='#E43A19',
                             activebackground='RED',

                             font=('Microsoft', 12))
        that_button.place(relx=0.21, rely=0.87)

        # setting up the back page button

        back_button = Button(root, bg='#B31312', fg='white', text='<<Back')
        back_button.place(relx=0.05, rely=0.15)

        pass

    def fetch_data(self):
        data = None  # Initialize data as None
        try:
            query = "SELECT * FROM rent WHERE propertyname = %s"
            self.cursor.execute(query, (self.propertyname,))
            data = self.cursor.fetchone()

        except mysql.connector.Error as e:
            print("Error fetching data from database:", e)

        # Populate entries with fetched data
        if data:
            self.setup_info()  # Call setup_info method instead of populate_entries

            # Populate entries with fetched data
            self.carp_ent.config(state=NORMAL)
            self.carp_ent.insert(0, data[1])
            self.carp_ent.config(state=DISABLED)
            self.floor_ent.config(state=NORMAL)
            self.floor_ent.insert(0, data[2])
            self.floor_ent.config(state=DISABLED)
            self.trans_ent.config(state=NORMAL)
            self.trans_ent.insert(0, data[3])
            self.trans_ent.config(state=DISABLED)
            self.stat_ent.config(state=NORMAL)
            self.stat_ent.insert(0, data[4])
            self.stat_ent.config(state=DISABLED)
            self.price_ent.config(state=NORMAL)
            self.price_ent.insert(0, data[5])
            self.price_ent.config(state=DISABLED)
            self.book_ent.config(state=NORMAL)
            self.book_ent.insert(0, data[6])
            self.book_ent.config(state=DISABLED)
            self.add_ent.config(state=NORMAL)
            self.add_ent.insert(0, data[7])
            self.add_ent.config(state=DISABLED)
            self.land_ent.config(state=NORMAL)
            self.land_ent.insert(0, data[8])
            self.land_ent.config(state=DISABLED)
            self.fur_ent.config(state=NORMAL)
            self.fur_ent.insert(0, data[9])
            self.fur_ent.config(state=DISABLED)
            self.flooring_ent.config(state=NORMAL)
            self.flooring_ent.insert(0, data[10])
            self.flooring_ent.config(state=DISABLED)
            self.type_ent.config(state=NORMAL)
            self.type_ent.insert(0, data[11])
            self.type_ent.config(state=DISABLED)
            self.over_ent.config(state=NORMAL)
            self.over_ent.insert(0, data[12])
            self.over_ent.config(state=DISABLED)
            self.age_ent.config(state=NORMAL)
            self.age_ent.insert(0, data[13])
            self.age_ent.config(state=DISABLED)
            self.water_ent.config(state=NORMAL)
            self.water_ent.insert(0, data[14])
            self.water_ent.config(state=DISABLED)
            self.elec_ent.config(state=NORMAL)
            self.elec_ent.insert(0, data[15])
            self.elec_ent.config(state=DISABLED)
        else:
            print("No data fetched from the database.")


root = Tk()
propertyname = sys.argv[1] if len(sys.argv) > 1 else "default_property_name"
obj = mainview(root,propertyname)
root.mainloop()