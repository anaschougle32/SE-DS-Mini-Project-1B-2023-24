import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import sys
from subprocess import call

class Dashboard:
    def __init__(self, email):
        self.email = email 
        self.window = tk.Tk()
        self.window.title("Dashboard")
        self.window.geometry('600x440')
        self.window.configure(bg='#333333')

        def create_frame():
            return tk.Frame(bg='#333333')

        frame = create_frame()

        # Load and resize the background image
        bg_image = Image.open("C:\\Users\\Arju salmani\\PycharmProjects\\taxidrivercomplientsystem\\bg_image.png")
        bg_image = bg_image.resize((779, 550), Image.LANCZOS)  # Use Image.LANCZOS as resampling filter
        self.bg_image = ImageTk.PhotoImage(bg_image)

        # Create a label with the background image
        self.background_label = tk.Label(self.window, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Label to display email
        self.email_label = tk.Label(self.window, text="Email: " + email, bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.email_label.pack(side=tk.TOP, padx=10, pady=10)

        Dashboard_label = tk.Label(frame, text='User Dashboard', bg='white', fg="pink", font=("Arial 28 underline"))
        Dashboard_label.pack()

        button1 = tk.Button(self.window, text="Raise Complaints", font=("Arial",14),relief="raised" ,height=3, width=15, bg='pink',command=self.complaints)
        button1.place(x=200,y=100)

        # Create the second button with the name "Complaints Status"
        button2 = tk.Button(self.window, text="Complaints Status",font=("Arial",14), relief="solid",height=3, width=15, bg='pink',command=self.user_complaint_status)
        button2.place(x=200,y=240)

        button3 = tk.Button(self.window, text="Back", relief="solid",height=2, width=10,fg="white", bg='#FF3399',command=self.user_login)
        button3.place(x=50,y=370)

        frame.pack()

    def complaints(self):
        self.window.destroy()
        call(['python','C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/raisedcomplaints.py',self.email])
        
    def user_login(self):
        self.window.destroy()
        call(['python','C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/userlogin.py'])

    def user_complaint_status(self):
        self.window.destroy()
        call(['python','C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/usercomplaintstatus.py',self.email])

    def set_background_image(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                image = Image.open(file_path)
                image = image.resize((779, 550), Image.LANCZOS)  # Use Image.LANCZOS as resampling filter
                image = ImageTk.PhotoImage(image)
                self.background_label.config(image=image)
                self.background_label.image = image  # Keep a reference to avoid garbage collection
        except Exception as e:
            print("Error loading image:", e)

# Usage
if __name__ == "__main__":
    email = sys.argv[1]  # Get the email from command line argument
    dashboard = Dashboard(email)
    dashboard.window.mainloop()
