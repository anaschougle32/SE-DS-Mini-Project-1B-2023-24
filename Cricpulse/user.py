from tkinter import *
import tkinter as tk
from tkinter import messagebox
#import mysql.connector
from subprocess import call

# Creating a main window
root = tk.Tk()
root.geometry("765x492")

# Define username_value1 and password_value1 as global variables
username_value1 = StringVar()
password_value1 = StringVar()
Name_Value = StringVar()
# Gender_Value = StringVar()
# Branch_Value = StringVar(value="Select Branch")
Phone_Value = StringVar()
User_Value = StringVar()
Password_Value = StringVar()

def Back():
    call(['python','choosingwindow.py'])
    root.destroy()
#login_label = Label(root, text="Login", font="times 20 bold", foreground="blue")
#login_label.pack()
'''
def register():

    print("click me")
    try:
        con = mysql.connector
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
        # Use self.root instead of root

    except Exception as e:jsa
        messagebox.showinfo('Unsuccessful', f'Try Again: {e}')
'''
def login_clicked():
    try:
        username = "yash24"
        password = "123"

        entered_username = username_value1.get()
        entered_password = password_value1.get()

        if entered_username == username and entered_password == password:
            messagebox.showinfo("Success", "Login Successful")
            call(['python', 'p2.py'])  # Open new1.py upon successful login
            root.destroy()  # Close the login window
        else:
            messagebox.showerror("Error", "Invalid username or password")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

'''
    try:
        con = mysql.connector
        db = con.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse", auth_plugin='mysql_native_password')
        c = db.cursor()

        username = username_value1.get()
        password = password_value1.get()

        query = "SELECT * FROM loginad WHERE Username = %s AND Password = %s"
        values = (username, password)

        c.execute(query, values)
        result = c.fetchone()

        if result:
            messagebox.showinfo("Success", "Login Successful")
            call(['python', 'new1.py'])  # Open p1.py upon successful login
            root.destroy()  # Close the login window
        else:
            messagebox.showerror("Error", "Invalid username or password")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
'''

def clear_main_frame():
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

# Function to switch to the registration frame
def registration_page():
    # Clear the main frame
    clear_main_frame()


    # Create a frame for registration content
    registration_frame = tk.Frame(main_frame)
    registration_frame.pack(fill=tk.BOTH, expand=True)

    # Labels and entry fields for registration
    # Make sure to define StringVar() variables globally
    Name_label = Label(registration_frame, text="Name", font="times 15 bold")
    Name_label.place(x=40, y=150)

    Phone_label = Label(registration_frame, text="Phone No", font="times 15 bold")
    Phone_label.place(x=310, y=150)

    User_label = Label(registration_frame, text="Username", font="times 15 bold")
    User_label.place(x=30, y=200)

    Password_label = Label(registration_frame, text="Password", font="times 15 bold")
    Password_label.place(x=310, y=200)



    NameEntry = Entry(registration_frame, textvariable=Name_Value, width=15, font="times 15 bold")
    NameEntry.place(x=110, y=150)

    PhoneEntry = Entry(registration_frame, textvariable=Phone_Value, width=15, font="times 15 bold")
    PhoneEntry.place(x=400, y=150)

    UserNameEntry = Entry(registration_frame, textvariable=User_Value, width=15, font="times 15 bold")
    UserNameEntry.place(x=125, y=200)

    PasswordEntry = Entry(registration_frame, textvariable=Password_Value, width=15, font="times 15 bold", show="*")
    PasswordEntry.place(x=400, y=200)
    Regbtn = Button(registration_frame, text="Register", bg="blue", fg="white", font="times 15 bold")
    Regbtn.place(x=250, y=300)
    regis_label = Label(registration_frame, text="Registration", font="times 15 bold", foreground="blue")
    regis_label.pack()

def forgot_password():
    print("Forgot Password button clicked")

def login_page():
    # Clear the main frame
    clear_main_frame()


    # Create a frame for login content
    login_frame = tk.Frame(main_frame)
    login_frame.pack(fill=tk.BOTH, expand=True)

    # Labels and entry fields for login
    username_label = Label(login_frame, text="Username:", font="times 15 bold")
    username_label.place(x=150, y=150)

    username_entry = Entry(login_frame, textvariable=username_value1, font="times 15 bold")
    username_entry.place(x=250, y=150)

    password_label = Label(login_frame, text="Password:", font="times 15 bold")
    password_label.place(x=150, y=200)

    password_entry = Entry(login_frame, textvariable=password_value1, font="times 15 bold", show="*")
    password_entry.place(x=250, y=200)

    ForgotPasswordbtn = Button(login_frame, text="Forgot Password?", font="times 12 bold", fg="blue", borderwidth=0, command=forgot_password)
    ForgotPasswordbtn.place(x=370, y=300)

    login_button = Button(login_frame, text="Login", bg="blue", fg="white", font="times 15 bold", command=login_clicked)
    login_button.place(x=250, y=300)
    login_label = Label(login_frame, text="Login", font="times 15 bold", foreground="blue")
    login_label.pack()

options_frame = tk.Frame(root, width=292, height=492, bg="blue")
options_frame.pack(side="left", fill="y")

buttons = [
    ("Login Page", login_page),
    ("Registration Page", registration_page)
]

for i, (text, command) in enumerate(buttons):
    btn = tk.Button(options_frame, text=text, width=20, command=command)
    btn.grid(row=i, column=0, pady=25, padx=10)
back_button = Button(options_frame,text="Back",width=20,command=Back)
back_button.place(relx=0.07,rely=0.35)
# Main frame
main_frame = tk.Frame(root, bg='white', highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
main_frame.pack_propagate(False)
main_frame.configure(height=492, width=473)

login_page()  # Display the login page initially

# Running the Tkinter event loop
root.mainloop()