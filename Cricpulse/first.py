import tkinter as tk
import subprocess
import sys

def home():
    print("Home button clicked")
    window.destroy()
    subprocess.Popen(["python", "first.py"] + sys.argv[1:])
def player_comparison():
    print("Player Comparison button clicked")

def player_performance():
    print("Player Performance button clicked")
    window.destroy()
    subprocess.Popen(["python", "second.py"] + sys.argv[1:])

def field_determination():
    print("Field Determination button clicked")

def my_profile():
    print("My Profile button clicked")

def label1_click():
    print("Label 1 clicked")

def label3_click():
    print("Label 3 clicked")

# Create main window
window = tk.Tk()
window.title("Project Winow")
window.geometry("835x490")
window.configure(bg="white")
window.geometry("+100+100")  # Set the position of the window

# Create dashboard frame
dashboard_frame = tk.Frame(window, width=252, height=490, bg="blue")
dashboard_frame.pack(side="left", fill="y")

# Create buttons in dashboard
buttons = [
    ("Home", home),
    ("Player Comparison", player_comparison),
    ("Player Performance", player_performance),
    ("Field Determination", field_determination),
    ("My Profile", my_profile)
]

for i, (text, command) in enumerate(buttons):
    btn = tk.Button(dashboard_frame, text=text, width=20, command=command)
    btn.grid(row=i, column=0, pady=25)

# Create label with black border
label_frame = tk.Frame(window, width=463, height=146, bg="white", bd=2, relief="solid")
label_frame.pack(pady=10)
label = tk.Button(label_frame, text="Label 1", bg="white", fg="black", font=("Arial", 12), command=label1_click)
label.place(relx=0.5, rely=0.5, anchor="center")

# Create frame for additional labels
additional_labels_frame = tk.Frame(window, bg="white")
additional_labels_frame.pack(pady=10)

# Create three labels with black border horizontally
label_2 = tk.Frame(window, width=136, height=174, bg="white", bd=2, relief="solid")
label_2.pack(pady=20)
label_2.place(relx=0.4, rely=0.65, anchor="center")

# Load the image
image = tk.PhotoImage(file="t20f1.png")

# Create a label to display the image
image_label = tk.Label(label_2, image=image, bd=0)
image_label.image = image  # This line is crucial to prevent garbage collection
image_label.pack()

label_3 = tk.Frame(window, width=136, height=174, bg="white", bd=2, relief="solid")
label_3.pack(pady=10)
label_3.place(relx=0.61, rely=0.65, anchor="center")
image = tk.PhotoImage(file="t20f1.png")

# Load the image
image1 = tk.PhotoImage(file="download.png")

# Create a label to display the image
image_label1 = tk.Label(label_3, image=image1, bd=0)
image_label1.image = image1  # This line is crucial to prevent garbage collection
image_label1.pack()

label_4 = tk.Frame(window, width=136, height=174, bg="white", bd=2, relief="solid")
label_4.pack(pady=10)
label_4.place(relx=0.81, rely=0.65, anchor="center")

# Load the image
image2 = tk.PhotoImage(file="test.png")

# Create a label to display the image
image_label2 = tk.Label(label_4, image=image2, bd=0)
image_label2.image = image2 # This line is crucial to prevent garbage collection
image_label2.pack()

window.mainloop()
