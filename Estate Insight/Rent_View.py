from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import io
import tkintermapview


class rentview:
    def __init__(self,root):
        self.root = root
        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 15, "bold")

        one = Label(root,
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
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)

        # setting up the toolbar for the app
        toolbar = Frame(root, bg="white", relief=GROOVE, bd=2, pady=2)

        printButt = Button(toolbar,
                           text="Home",
                           bg="white",
                           border=0,
                           activebackground='#B67352', command=self.home)
        printButt.pack(side=LEFT, padx=20, pady=2)
        insertButt = Button(toolbar,
                            text="Buy",
                            bg="white",
                            border=0,
                            command=self.buy)
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Sell",
                           bg="white",

                           border=0,
                           activebackground='#B67352', command=self.sell)

        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Rent",
                           bg="#B31312",
                           relief=RAISED,
                           border=1,
                           fg='white',
                           command=self.rent)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Wishlist",
                           bg="white",
                           border=0)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Help",
                           bg="white",
                           border=0)
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

        # Frame 1 where image is to be viewed
        frame1 = Frame(root, width=400, height=900, bg="White", relief=GROOVE, bd=1)
        frame1.pack(side=LEFT, padx=40, pady=50)

        self.img = ImageTk.PhotoImage(Image.open('Images/maindoor.jpeg'))
        Label2 = Label(frame1, image=self.img, width=300, height=300, padx='10', pady='10')
        Label2.pack(side=TOP)

        def open_mumbaimap_window():
            # # Create a new window for Mumbai map
            # mumbai_window = tk.Toplevel(window)
            # mumbai_window.title("Mumbai Map")

            mapwidget = tkintermapview.TkinterMapView(tk.Toplevel(self.root), width=420, height=400, corner_radius=0)
            mapwidget.pack()

            # Create a map widget for Mumbai
            marker_1 = mapwidget.set_address("AP Shah Institute of Technology,kasarvadavli,thane,india", marker=True)
            marker_1.set_text("AP Shah Institute of Technology,kasarvadavli,thane,india")

        def imagechange():
            self.image1 = ImageTk.PhotoImage(Image.open('Images/Livingroom.jpeg'), Image.open('Images/Bedroom.jpeg'))
            Label2.configure(image=self.image1)
            Label2.image = self.image1

        top_label = Label(frame1, text="Korus apt", font=("Arial", 12, "bold"), bg='White')
        top_label.place(relx=0.5, rely=0.00, anchor='n')

        button = Button(frame1, text=">>", padx='10', pady='10', command=imagechange)
        button.pack(side=TOP, pady='10')

        # Frame 2 where information is to be displayed
        frame2 = Frame(root, width=600, height=700, bg='White')
        frame2.pack(side=RIGHT, padx=10, pady=10)

        text = "Carpet Area\n1104 sqft\n₹31,703/sqft"
        label1 = Label(frame2, text=text, anchor=NW, justify=LEFT, bd=1, relief=GROOVE)
        label1.place(x=10, y=10)

        text2 = "Floor\n2 (Out of 13 Floors)"
        label2 = Label(frame2, text=text2, anchor=NW, justify=LEFT, bd=1, relief=GROOVE)
        label2.place(x=150, y=10)

        text3 = "Trasaction type\nResale"
        label3 = Label(frame2, text=text3, anchor=NW, justify=LEFT, bd=1, relief=GROOVE)
        label3.place(x=320, y=10)

        text4 = "Status\n Ready To Move"
        label4 = Label(frame2, text=text4, anchor=NW, justify=LEFT, bd=1, relief=GROOVE)
        label4.place(x=450, y=10)

        labels_to_bold = [label1, label2, label3, label4]

        for label in labels_to_bold:
            label.config(font=("Arial", 8, "bold"), pady=10)

        vertical_spacing = 80

        y_coordinate_label5 = label1.winfo_y() + label1.winfo_height() + vertical_spacing

        text5 = (
            "More Details\n\nPrice Breakup : ₹3.5 Cr | ₹17,50,000 Approx. Registration Charges | ₹8,500 Monthly\n\n"
            "Booking Amount : ₹100000\n\n"
            "Address : Jai Arati plot no 2930 Swastik Park Near Kali Bari Temple Chembur East Mumbai \nMaharashtra 400071,"
            " Chembur, Mumbai - Harbour Line, Maharashtra\n\nLandmarks : kali bari Temple\n\nFurnishing : Unfurnished\n\n"
            "Flooring : Vitrified\n\nType of Ownership : Co-operative Society\n\n"
            "Overlooking : Garden/Park, Main Road\n\n"
            "Age of Construction : 5 to 10 years\n\n"
            "Water Availability : 24 Hours Available\n\n"
            "Status of Electricity : No/Rare Powercut")
        label5 = Label(frame2, text=text5, font=("Arial", 10), anchor=NW, justify=LEFT, bd=1, relief=GROOVE)
        label5.place(x=10, y=y_coordinate_label5)

        button = Button(frame2, text="Contact Owner", padx='10', pady='10', bg='#B31312', fg='White')
        button.place(x=200, y=490)

        that_button = Button(frame2,
                             text="View Location",
                             foreground='#f7f7f7',
                             background='#B31312',
                             activeforeground='#E43A19',
                             activebackground='RED',
                             command=open_mumbaimap_window,
                             font=('Microsoft', 12))
        that_button.place(relx=0.65, rely=0.86)

        # setting up the back page button

        back_button = Button(root, bg='#B31312', fg='white', text='<<Back',command=self.back)
        back_button.place(relx=0.05, rely=0.15)

    def next(self):
        self.root.destroy()
        import Homepage2

    def home(self):
        self.root.destroy()
        import Homepage1

    def rent(self):
        self.root.destroy()
        import Rent1

    def sell(self):
        self.root.destroy()
        import Sell_1
    def buy(self):
        self.root.destroy()
        import buy1
    def back(self):
        self.root.destroy()
        import Rent1



root = Tk()
obj = rentview(root)
root.mainloop()


