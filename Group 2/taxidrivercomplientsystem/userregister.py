from sqlite3 import Cursor
from subprocess import call
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import mysql.connector

class RegistrationForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Registration Form")
        self.master.geometry("600x440")
        self.master.configure(bg='#333333')

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.repeatpassword_var = tk.StringVar()

        tk.Label(self.master, text="Registration Form", font=("Arial", 20), bg="#FF3399", fg="white").pack(pady=20)

        tk.Label(self.master, text="Your Name:", bg="#333333", fg="white").pack(pady=(20, 10))
        self.name_entry = tk.Entry(self.master, textvariable=self.name_var, bg="#DDD", bd=3)
        self.name_entry.pack()

        tk.Label(self.master, text="Your Email:", bg="#333333", fg="white").pack(pady=(10, 10))
        self.email_entry = tk.Entry(self.master, textvariable=self.email_var, bg="#DDD", bd=3)
        self.email_entry.pack()

        tk.Label(self.master, text="Password:", bg="#333333", fg="white").pack(pady=(10, 10))
        self.password_entry = tk.Entry(self.master, textvariable=self.password_var, bg="#DDD", bd=3, show="*")
        self.password_entry.pack()

        tk.Label(self.master, text="Repeat Password:", bg="#333333", fg="white").pack(pady=(10, 10))
        self.repeatpassword_entry = tk.Entry(self.master, textvariable=self.repeatpassword_var, bg="#DDD", bd=3, show="*")
        self.repeatpassword_entry.pack()

        self.register_button = tk.Button(
            self.master, text="Register", command=self.register, bg="green", fg="white", bd=0, font=("Arial", 10, "bold")
        )
        self.register_button.pack(pady=10)

        self.back_button = tk.Button(
            self.master, text="Back",bg="#FF3399", fg="white", bd=0, font=("Arial", 10, "bold"),command=self.user_login)
        
        self.back_button.pack(pady=10)

        # Connect to MySQL database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Arju2003@",
            database="complaintsystem",
            auth_plugin="mysql_native_password",
            
        )
        
        self.cursor = self.conn.cursor()

        # Create userregister table if not exists
       
    def register(self):
        name = self.name_var.get()
        email = self.email_var.get()
        password = self.password_var.get()
        repeatpassword = self.repeatpassword_var.get()

        # Check if fields are empty
        if not name or not email or not password or not repeatpassword:
            messagebox.showerror("Error", "All fields are required.")
            return

        # Check if passwords match
        if password != repeatpassword:
            messagebox.showerror("Error", "Passwords do not match.")
            return
    
        # Insert user into database
        self.cursor.execute("INSERT INTO userregister (name, email, password, repeatpassword) VALUES (%s, %s, %s, %s)",
                            (name, email, password, repeatpassword))
        self.conn.commit()

        messagebox.showinfo("Success", "Registration successful.")
        self.clear_fields()

    def clear_fields(self):
        self.name_var.set("")
        self.email_var.set("")
        self.password_var.set("")
        self.repeatpassword_var.set("")

    def __del__(self):
        # Close database connection when the object is destroyed
        self.conn.close()

    def user_login(self):
        self.master.withdraw()  # it will hide the form
        call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/userlogin.py'])
    

root = tk.Tk()

# Load and resize the background image
bg_image = Image.open("C:\\Users\\Arju salmani\\PycharmProjects\\taxidrivercomplientsystem\\bg_image.png")
bg_image = bg_image.resize((779, 550), Image.LANCZOS)  # Use Image.LANCZOS as resampling filter
bg_image = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def set_background_image():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((779, 550), Image.LANCZOS)  # Use Image.LANCZOS as resampling filter
            image = ImageTk.PhotoImage(image)
            background_label.config(image=image)
            background_label.image = image  # Keep a reference to avoid garbage collection
    except Exception as e:
        print("Error loading image:", e)


def userlogin():
    root.destroy()
    # call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/userlogin.py'])


my_gui = RegistrationForm(root)
root.mainloop()
