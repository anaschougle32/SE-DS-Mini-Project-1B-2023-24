import tkinter as tk
from tkinter import messagebox
from subprocess import call
from tkinter import filedialog
from PIL import ImageTk, Image
import mysql.connector

class LoginForm:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Login form")
        self.master.geometry('600x440')
        self.master.configure(bg='#333333')

        # Create a label for the background image
        self.background_label = tk.Label(master, bg='#333333')
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Load and set the background image
        self.set_background_image("C:\\Users\\Arju salmani\\PycharmProjects\\taxidrivercomplientsystem\\userlogin.png")

        # Creating widgets
        self.login_label = tk.Label(
            self.background_label, text="Login", font=("Arial", 30))
        self.email_label = tk.Label(
            self.background_label, text="Email:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.email_entry = tk.Entry(self.background_label, font=("Arial", 16))
        self.password_entry = tk.Entry(self.background_label, show="*", font=("Arial", 16))
        self.password_label = tk.Label(
            self.background_label, text="Password:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.login_button = tk.Button(
            self.background_label, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.admin_login)
        self.back_button = tk.Button(
            self.background_label, text="back", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.go_back)
        self.registration_button = tk.Button(
            self.background_label, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),command=self.user_registers)

        # Placing widgets on the screen
        self.login_label.pack(pady=40)
        self.email_label.pack()
        self.email_entry.pack(pady=20)
        self.password_label.pack()
        self.password_entry.pack(pady=20)
        self.back_button.pack(side=tk.LEFT, padx=(90,0), pady=30)
        self.login_button.pack(side=tk.LEFT, padx=(90,0), pady=30)
        self.registration_button.pack(padx=10, pady=30)

    def admin_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Arju2003@",
            database="complaintsystem",
            auth_plugin="mysql_native_password",
        )
        cursor = conn.cursor()

        # Query the database to check if the email and password exist
        cursor.execute("SELECT * FROM userregister WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()  # Fetch one row

        if user:  # If user exists
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            self.open_dashboard(email)
        else:
            messagebox.showerror(title="Error", message="Invalid email or password.")

        # Close cursor and connection
        cursor.close()
        conn.close()

    def open_dashboard(self, email):
        self.master.withdraw()  # Hide the login window
        call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/dashboard.py', email])

    def go_back(self):
        self.master.withdraw()  # Hide the login window
        call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/MainDashboard.py'])
        
        
    def user_registers(self):
        self.master.withdraw()  # Hide the login window
        call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/userregister.py'])    

    def set_background_image(self, path):
        try:
            image = Image.open(path)
            image = image.resize((779, 550), Image.LANCZOS)  # Use Image.LANCZOS as resampling filter
            self.background_image = ImageTk.PhotoImage(image)
            self.background_label.config(image=self.background_image)
        except Exception as e:
            print("Error loading image:", e)

root = tk.Tk()
login_form = LoginForm(root)
root.mainloop()
