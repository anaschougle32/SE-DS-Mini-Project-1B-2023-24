
from tkinter import *
from tkinter import ttk, messagebox
from subprocess import call
import mysql.connector as con

global username_value1,Name_Value,Phone_Value,User_Value,Password_Value
global password_value
# Creating a main window
root = Tk()
root.geometry("935x650")

def loginadmin():
    root.destroy()
    call(['python', 'loginad.py'])

def back_btn():
    root.destroy()
    call(['python', 'choosingwindow.py'])


def register():
    global Name_Value,Phone_Value,Password_Value,User_Value

    clear_main_frame()
    # Username label and entry
    regis_frame = Frame(main_frame)
    regis_frame.pack(fill=BOTH, expand=True)

    # Creating a label with text "Registration" and specified font
    registration_label = Label(regis_frame, text="Registration", font="times 20 bold", foreground="blue")
    registration_label.place(x=350, y=100)  # Packing the label to display it in the window

    # Label
    Name_label = Label(regis_frame, text="Name", font="times 15 bold")
    Name_label.place(x=50, y=180)

    # Gender_label = Label(root , text="Gender", font="times 15 bold")
    # Gender_label.place(x=500,y=100)

    # Branch_label = Label(root , text="Branch", font="times 15 bold")
    # Branch_label.place(x=50,y=180)

    Phone_label = Label(regis_frame, text="Phone No", font="times 15 bold")
    Phone_label.place(x=350, y=180)

    User_label = Label(regis_frame, text="Username", font="times 15 bold")
    User_label.place(x=50, y=260)

    Password_label = Label(regis_frame, text="Password", font="times 15 bold")
    Password_label.place(x=350, y=260)

    # Entry

    Name_Value = StringVar()
    # Gender_Value = StringVar()
    # Branch_Value = StringVar(value="Select Branch")
    Phone_Value = StringVar()
    User_Value = StringVar()
    Password_Value = StringVar()

    NameEntry = Entry(regis_frame, textvariable=Name_Value, font="times 15 bold")
    NameEntry.place(x=140, y=180)

    # GenderEntry1=Radiobutton(root,variable=Gender_Value,text='Male',value='male',font="times 12 bold")
    # GenderEntry1.place(x=590,y=100)

    # GenderEntry2=Radiobutton(root,variable=Gender_Value,text='Female',value='female',font="times 12 bold")
    # GenderEntry2.place(x=590,y=120)

    # branch=['Comps','IT','DS','AIML']
    # BranchEntry=ttk.Combobox(root,textvariable=Branch_Value,values=branch,font="times 12 bold",state="readonly")
    # BranchEntry.place(x=140,y=180)

    PhoneEntry = Entry(regis_frame, textvariable=Phone_Value, font="times 15 bold")
    PhoneEntry.place(x=450, y=180)

    UserNameEntry = Entry(regis_frame, textvariable=User_Value, font="times 15 bold")
    UserNameEntry.place(x=140, y=260)

    PasswordEntry = Entry(regis_frame, textvariable=Password_Value, font="times 15 bold", show="*")
    PasswordEntry.place(x=450, y=260)

    # Button

    Regbtn = Button(regis_frame, text="Register", bg="blue", fg="white", font="times 15 bold", command=register_clicked)
    Regbtn.place(x=350, y=400)


def register_clicked():
    print("click me")
    try:
        db = con.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse", auth_plugin='mysql_native_password')
        c = db.cursor()

        Name = Name_Value.get()
        # Gender = Gender_Value.get()
        # Branch = Branch_Value.get()
        Phone = Phone_Value.get()
        Username = User_Value.get()
        Password = Password_Value.get()

        query = "INSERT INTO loginad(Name, Username, Phone, Password) VALUES (%s,%s,%s,%s)"
        values = (Name, Username, Phone, Password)

        c.execute(query, values)
        db.commit()
        messagebox.showinfo('Success', 'Successfully Inserted')
        #call(['python', "register.py"])
        root.destroy()  # Use self.root instead of root

    except Exception as e:
        messagebox.showinfo('Unsuccessful', f'Try Again: {e}')



# Function to create login page
def login_page():
    global username_value1,password_value  # Declare username_value1 as global
    clear_main_frame()
    # Username label and entry
    login_frame = Frame(main_frame)
    login_frame.pack(fill=BOTH, expand=True)

    username_label = Label(login_frame, text="Username:", font="times 15 bold")
    username_label.place(x=50, y=200)
    username_value1 = StringVar()
    username_entry = Entry(login_frame, textvariable=username_value1, font="times 15 bold")
    username_entry.place(x=150, y=200)

    # Password label and entry
    password_label = Label(login_frame, text="Password:", font="times 15 bold")
    password_label.place(x=50, y=250)
    password_value = StringVar()
    password_entry = Entry(login_frame, textvariable=password_value, font="times 15 bold", show="*")
    password_entry.place(x=150, y=250)
    login_button = Button(login_frame, text="Login", bg="blue", fg="white", font="times 15 bold", command=login_clicked)
    login_button.place(x=350, y=300)
    registration_label = Label(login_frame, text="Login", font="times 20 bold", foreground="blue")
    registration_label.place(x=350, y=100)

# Function to handle login button click
def login_clicked():
    try:
        db = con.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse", auth_plugin='mysql_native_password')
        c = db.cursor()

        username = username_value1.get()
        password = password_value.get()

        query = "SELECT * FROM loginad WHERE Username = %s AND Password = %s"
        values = (username, password)

        c.execute(query, values)
        result = c.fetchone()

        if result:
            messagebox.showinfo("Success", "Login Successful")
            root.destroy()  # Close the login window
            call(['python', 'p1.py'])  # Open p1.py upon successful login
        else:
            messagebox.showerror("Error", "Invalid username or password")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Creating a label with text "Login" and specified font
login_label = Label(root, text="Login", font="times 20 bold", foreground="blue")
login_label.place(x=350, y=100)


def clear_main_frame():
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()



options_frame = Frame(root, width=252, height=650, bg="blue")
options_frame.pack(side="left", fill="y")

buttons = [
    ("Login Page", login_page),
    ("Registration Page ", register),
    ("Back",back_btn)
]

for i, (text, command) in enumerate(buttons):
    btn = Button(options_frame, text=text, width=20, command=command)
    btn.grid(row=i, column=0, pady=25, padx=10)
main_frame = Frame(root, bg='white',highlightbackground='black', highlightthickness=2)  # Set main frame size
main_frame.pack(side=LEFT, fill=BOTH, expand=True)
main_frame.pack_propagate(False)
main_frame.configure(height=490, width=583)
login_page()
root.mainloop()
