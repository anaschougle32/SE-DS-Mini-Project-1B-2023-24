import tkinter as tk
from tkinter import messagebox
from subprocess import call
from tkinter import filedialog
from PIL import ImageTk, Image

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
        self.username_label = tk.Label(
            self.background_label, text="Username:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.username_entry = tk.Entry(self.background_label, font=("Arial", 16))
        self.password_entry = tk.Entry(self.background_label, show="*", font=("Arial", 16))
        self.password_label = tk.Label(
            self.background_label, text="Password:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.login_button = tk.Button(
            self.background_label, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.admin_login)
        self.back_button = tk.Button(
            self.background_label, text="back", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.go_back)
        

        # Placing widgets on the screen
        self.login_label.pack(pady=40)
        self.username_label.pack()
        self.username_entry.pack(pady=20)
        self.password_label.pack()
        self.password_entry.pack(pady=20)
        self.back_button.pack(side=tk.LEFT, padx=(180,0), pady=30)
        self.login_button.pack(side=tk.RIGHT, padx=(0,180), pady=30)
        

    def admin_login(self):
        email = "johnsmith"
        password = "12345"
        if self.username_entry.get() == email and self.password_entry.get() == password:
            messagebox.showinfo(
                title="Login Success", message="You successfully logged in.")
            self.open_dashboard()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    def open_dashboard(self):
        self.master.withdraw()  # Hide the login window
        call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/admindashboard.py'])  # Call the Dashboard script with the correct path

    def go_back(self):
        self.master.withdraw()  # Hide the login window
        call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/MainDashboard.py'])
        
        
       

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
