import sys
import tkinter as tk
import io
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import sys
bs = sys.argv[1]
root = tk.Tk()
root.title("Project Window")
root.geometry("835x590")
root.configure(bg="white")
# Function to fetch data from the database

def display_field_data(bs):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor = conn.cursor()
    # Query to fetch data from the database based on the name
    query = "SELECT * FROM field WHERE bowling_style = %s"
    cursor.execute(query, (bs,))
    result = cursor.fetchall()

    # Check if any data is found
    if result:
        # Since there may be multiple rows, we'll only display the data from the first row
        row_data = result[0]

        # Populate the text fields with the fetched data
        bowlingtypeEntryi.delete(0, tk.END)
        bowlingtypeEntryi.insert(tk.END, row_data[0])  # Bowling Style

        bowlingtypeEntryT.delete(0, tk.END)
        bowlingtypeEntryT.insert(tk.END, row_data[1])  # Bowling Type

        field_info.delete(1.0, tk.END)
        field_info.insert(tk.END, row_data[2])  # Field Information

        image_data = row_data[3]  # Image
        if image_data:
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((200, 325))  # Adjust the size as needed
            photo = ImageTk.PhotoImage(image)

            # Clear any existing widgets inside the frame
            for widget in label2_frame.winfo_children():
                widget.destroy()

            # Create a label and display the image
            image_label = tk.Label(label2_frame, image=photo)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.pack()

    else:
        # If no data is found, show a message
        messagebox.showinfo("Error", "No data found for the entered name")

    # Clear the main frame
    # Create a frame for player performance content

Field_label = tk.Label(root, text="Field Determination", font="times 20 bold", foreground="blue",relief="raised",padx=10, pady=10)
Field_label.pack()
label2_frame = tk.Frame(root, width=200, height=325, bd=2, relief="solid", bg="white")
label2_frame.place(relx=0.84, rely=0.45, anchor="center")

bowlingstyleEntry = tk.Label(root, text="Bowling Style", font="times 15 bold")
bowlingstyleEntry.place(x=40, y=110)
bowlingstyleEntryt = tk.Label(root, text="Bowling Style", font="times 15 bold")
bowlingstyleEntryt.place(x=40, y=170)

bowlingtypeEntryi = tk.Entry(root, font="times 15 bold", width=20, bg="white")
bowlingtypeEntryi.place(x=270, y=110)
bowlingtypeEntryT = tk.Entry(root, font="times 15 bold", width=20, bg="white")
bowlingtypeEntryT.place(x=270, y=170)
fieldinfo_label = tk.Label(root, text="Field Information", font="times 15 bold")
fieldinfo_label.place(x=40, y=200)
field_info = tk.Text(root, wrap="word", height=20, width=55, bd=2)
field_info.place(x=45,y = 250)

display_field_data(bs)
root.mainloop()