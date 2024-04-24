from tkinter import *
import tkinter as tk
from tkinter import NW, filedialog
from subprocess import call
from PIL import ImageTk, Image

def create_frame():
    return tk.Frame(bg='#333333')

window = tk.Tk()
window.title("Taxi driver forbidden complaint")
window.geometry('779x550')
window.configure(bg='#333333')

# Load and resize the background image
bg_image = Image.open("C:\\Users\\Arju salmani\\PycharmProjects\\taxidrivercomplientsystem\\bg_image.png")
bg_image = bg_image.resize((779, 550), Image.LANCZOS)  # Use Image.LANCZOS as resampling filter
bg_image = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
background_label = tk.Label(window, image=bg_image)
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
    window.destroy()
    call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/userlogin.py'])

def adminlogin():
    window.destroy()
    call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/adminlogin.py'])

frame = create_frame()

Dashboard_label = tk.Label(frame, text='Taxi driver forbidden complaints', bg='white', fg="blue", font=("Arial 28 underline"))
Dashboard_label.pack()

User = tk.Button(window, text="User", relief="raised", height=5, width=20, font=("Arial 16"), bg='white', anchor='center', command=userlogin)
User.place(anchor='center', x=380, y=170)

Admin = tk.Button(window, text="Admin", relief="solid", height=5, width=20, font=("Arial 16"), bg='blue', command=adminlogin)
Admin.place(anchor='center', x=380, y=370)

frame.pack()

window.mainloop()
