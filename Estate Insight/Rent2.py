import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
import tkinter as tk

class Rent2:
    def __init__(self, root):
        self.root = root
        self.add_user_pic = Image.open('Images/estate.png')

        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 19, "bold")

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

        down_arrow = Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
        down_arrow.pack()
        down_arrow.menu = Menu(down_arrow)
        down_arrow["menu"] = down_arrow.menu
        down_arrow.menu.add_checkbutton(label="Profile")
        down_arrow.menu.add_checkbutton(label="Agents")
        down_arrow.menu.add_checkbutton(label="LogOut")
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

        # *********setting up the main page********

        # setting the strings of radio buttons
        self.registered_selection = tk.StringVar()
        self.transaction_selection = tk.StringVar()
        self.status_selection = tk.StringVar()
        self.ownership_selection = tk.StringVar()

        # pic upload
        self.pic_path = tk.StringVar()
        self.pic_path.set('')

        self.pic_path2 = tk.StringVar()  # Initialize pic_path2
        self.pic_path2.set('')

        self.pic_path3 = tk.StringVar()  # Initialize pic_path3
        self.pic_path3.set('')

        def open_pic():
            path = askopenfilename()

            if path:
                self.img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                self.pic_path.set(path)  # Store path in pic_path

                add_pic_butt.config(image=self.img)
                add_pic_butt.image = self.img

        def open_pic2():
            path = askopenfilename()

            if path:
                self.img2 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                self.pic_path2.set(path)  # Store path in pic_path2

                add_pic2_butt.config(image=self.img2)
                add_pic2_butt.image = self.img2

        def open_pic3():
            path = askopenfilename()

            if path:
                self.img3 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                self.pic_path3.set(path)  # Store path in pic_path3

                add_pic3_butt.config(image=self.img3)
                add_pic3_butt.image = self.img3

        # adding top text
        top_text = tk.Label(root, text='Property Details',
                            bg='white',
                            fg='black',
                            font=('Bold', 20))
        top_text.place(relx=0.01, rely=0.06)

        # adding name entry box
        prop_name = tk.Label(root, text='>Property Name:', font=('Bold', 15), bg='white')
        prop_name.place(relx=0.3, rely=0.15)
        prop_name_ent = tk.Entry(root, font=('Bold', 15),
                                 highlightcolor='black', highlightbackground='gray',
                                 highlightthickness=2)  # name entry button
        prop_name_ent.place(relx=0.3, rely=0.2)

        username= tk.Label(root, text='>UserID:', font=('Bold', 15), bg='white')
        username.place(relx=0.01, rely=0.15)
        username_ent = tk.Entry(root, font=('Bold', 15),
                                highlightcolor='black', highlightbackground='gray',
                                highlightthickness=2)  # name entry button
        username_ent.place(relx=0.01, rely=0.2)

        # adding register selection
        register_select = tk.Label(root, text='>Register as:',
                                   font=('Bold', 15), bg='white')
        register_select.place(relx=0.01, rely=0.3)
        owner = tk.Radiobutton(root, text='Owner',
                               font=('Bold', 15), bg='white',
                               variable=self.registered_selection, value='owner')
        owner.place(relx=0.01, rely=0.35)
        builder = tk.Radiobutton(root, text='Builder',
                                 font=('Bold', 15), bg='white',
                                 variable=self.registered_selection, value='builder')
        builder.place(relx=0.1, rely=0.35)
        self.registered_selection.set('owner')

        # adding transaction selection
        transaction_select = tk.Label(root, text='>Transaction Type:',
                                      font=('Bold', 15), bg='white')
        transaction_select.place(relx=0.5, rely=0.3)
        new_property = tk.Radiobutton(root, text='New Property',
                                      font=('Bold', 15), bg='white',
                                      variable=self.transaction_selection, value='new_property')
        new_property.place(relx=0.5, rely=0.35)
        resale = tk.Radiobutton(root, text='Resale',
                                font=('Bold', 15), bg='white',
                                variable=self.transaction_selection, value='resale')
        resale.place(relx=0.66, rely=0.35)
        self.transaction_selection.set('new_property')

        # adding status selection
        status_select = tk.Label(root, text='>Status:',
                                 font=('Bold', 15), bg='white')
        status_select.place(relx=0.01, rely=0.45)
        Un_construct = tk.Radiobutton(root, text='Under Construction',
                                      font=('Bold', 15), bg='white',
                                      variable=self.status_selection, value='Un_construct')
        Un_construct.place(relx=0.01, rely=0.5)
        ready = tk.Radiobutton(root, text='Ready to Move',
                               font=('Bold', 15), bg='white',
                               variable=self.status_selection, value='ready')
        ready.place(relx=0.22, rely=0.5)
        self.status_selection.set('Un_construct')

        # adding ownership selection
        ownership_select = tk.Label(root, text='>Type of Ownership:',
                                    font=('Bold', 15), bg='white')
        ownership_select.place(relx=0.5, rely=0.45)
        house = tk.Radiobutton(root, text='House',
                               font=('Bold', 15), bg='white',
                               variable=self.ownership_selection, value='house')
        house.place(relx=0.5, rely=0.5)
        villa = tk.Radiobutton(root, text='Villa',
                               font=('Bold', 15), bg='white',
                               variable=self.ownership_selection, value='villa')
        villa.place(relx=0.6, rely=0.5)
        society = tk.Radiobutton(root, text='Co-Operative Society',
                                 font=('Bold', 15), bg='white',
                                 variable=self.ownership_selection, value='society')
        society.place(relx=0.69, rely=0.5)
        self.ownership_selection.set('house')

        # pic add

        # add images of property text
        top_text = tk.Label(root, text='Add Images of Property:',
                            bg='white',
                            fg='black',
                            font=('Bold', 17))
        top_text.place(relx=0.01, rely=0.63)

        # 1st image
        add_pic_frame = tk.Frame(root,
                                 highlightbackground='black',
                                 highlightthickness=2,
                                 bg='white')
        add_pic_butt = tk.Button(add_pic_frame, bd=0,
                                 command=open_pic)  # the pic upload button
        add_pic_butt.pack()
        add_pic_frame.place(relx=0.01, rely=0.73, width=105, height=105)

        # 2nd image
        add_pic2_frame = tk.Frame(root,
                                  highlightbackground='black',
                                  highlightthickness=2,
                                  bg='white')
        add_pic2_butt = tk.Button(add_pic2_frame, bd=0,
                                  command=open_pic2)  # the pic upload button
        add_pic2_butt.pack()
        add_pic2_frame.place(relx=0.16, rely=0.73, width=105, height=105)

        # 3rd image
        add_pic3_frame = tk.Frame(root,
                                  highlightbackground='black',
                                  highlightthickness=2,
                                  bg='white')
        add_pic3_butt = tk.Button(add_pic3_frame, bd=0,
                                  command=open_pic3)  # the pic upload button
        add_pic3_butt.pack()
        add_pic3_frame.place(relx=0.32, rely=0.73, width=105, height=105)

        # adding the next button
        next_butt = tk.Button(root, text="Next",
                              font=('Bold', 15), bg='#B31312',
                              fg='white', bd=1, command=self.next)
        next_butt.place(relx=0.6, rely=0.8)

        # setting up the back page button

        back_button = Button(root, bg='#B31312', fg='white', text='<<Back',command=self.back)
        back_button.place(relx=0.9, rely=0.1)

        self.username_ent = username_ent
        self.prop_name_ent = prop_name_ent
        self.registered_selection = self.registered_selection
        self.transaction_selection = self.transaction_selection
        self.status_selection = self.status_selection
        self.ownership_selection = self.ownership_selection
        self.pic_path = self.pic_path
        self.pic_path2 = self.pic_path2
        self.pic_path3 = self.pic_path3

    def next(self):
        username = self.username_ent.get()
        propertyname = self.prop_name_ent.get()
        registeras = self.registered_selection.get()
        transactiontype = self.transaction_selection.get()
        propstatus = self.status_selection.get()
        typeofownership = self.ownership_selection.get()
        image1_path = self.pic_path.get()
        image2_path = self.pic_path2.get()
        image3_path = self.pic_path3.get()

        try:
            if self.conn.is_connected():
                pst = self.conn.cursor()
                sql_query = (
                    "INSERT INTO rent (username, propertyname, registeras, transactionty,status,typeofos, photo1) VALUES (%s, %s, %s, %s, %s, %s, %s)")

                pst.execute(sql_query, (
                    username, propertyname, registeras, transactiontype, propstatus, typeofownership, image1_path))
                self.conn.commit()
                messagebox.showinfo("", "Successfully Saved")

                # No need to import Sell_2 here

                # Close the Sell_1 window
                self.root.destroy()

                # Import and display the Sell_2 window
                import Rent3
                Rent3.Rent3.username = username
                root2 = Tk()
                Rent3 = Rent3.Rent3(root2)
                root2.mainloop()



        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("", "Failed to register")

    def back(self):
        self.root.destroy()
        subprocess.run(['python','Homepage1.py'])
        import Homepage1



root = Tk()
obj = Rent2(root)
root.mainloop()