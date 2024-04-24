from operator import call
import tkinter as tk
from tkinter import RIGHT, LEFT, BOTTOM
import tkinter
from subprocess import call
from tkinter import NW, filedialog
from PIL import ImageTk, Image

def create_frame():
    return tk.Frame(bg='#333333')

window = tk.Tk()
window.title("Dashboard")
window.geometry('600x440')
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

def adminlogin():
    window.destroy()
    call(['python','C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/adminlogin.py'])
    
def admincomplaintstatus():
    window.destroy()
    call(['python','C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/admincomplaintstatus.py'])
    
def admincomplaints():
    window.destroy()
    call(['python','C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/admincomplaints.py'])

frame = create_frame()

Dashboard_label = tk.Label(frame, text='Admin Dashboard', bg='white', fg="blue", font=("Arial 28 underline"))
Dashboard_label.pack()

button1 = tk.Button(window, text="Complaints listed", font=("Arial",14),relief="raised" ,height=3, width=15, bg='pink',command=admincomplaints)
button1.place(x=200,y=100)

# Create the second button with the name "Compliments Status"
button2 = tk.Button(window, text="Complaints Status",font=("Arial",14), relief="solid",height=3, width=15, bg='pink',command=admincomplaintstatus)
button2.place(x=200,y=240)

button3 = tk.Button(window, text="Back", relief="solid",height=2, width=10, bg='#FF3399',fg="white",command=adminlogin)
button3.place(x=50,y=370)

frame.pack()

# Start the Tkinter event loop
window.mainloop()