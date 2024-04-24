from io import BytesIO
from tkinter import *
import tkinter as tk
from tkinter import Frame, filedialog, messagebox
import mysql.connector
from PIL import Image, ImageTk


root = Tk()
root.title("Field Determination")
root.geometry("935x610")
root.configure(background="white")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parthavi@1204",
    database="cricpulse",
    auth_plugin="mysql_native_password"
)
cursor = db.cursor()
def update_data():
    try:
        bowlingstyle1 = style_value.get()
        fieldinfo = field_info.get("1.0", "end-1c")
        bowlingtype = type_value.get()

        # Read image file in binary mode
        with open(file_path, 'rb') as file:
            image_data = file.read()

        # Update data in the table
        query = "UPDATE field SET  bowling_type = %s, field_info = %s, image = %s WHERE bowling_style = %s"
        values = (fieldinfo, bowlingtype, image_data, bowlingstyle1)  # Note the order of parameters
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_data():
    # Get the name from the name text field
    style = style_value.get()

    # Query to fetch data from the database based on the name
    query = "SELECT * FROM field WHERE bowling_style = %s"
    cursor.execute(query, (style,))
    result = cursor.fetchall()

    # Check if any data is found
    if result:
        # Since there may be multiple rows, we'll only display the data from the first row
        row_data = result[0]

        # Populate the text fields with the fetched data
        bowlingstyleEntry.delete(0, tk.END)
        bowlingstyleEntry.insert(tk.END, row_data[0])  # Name
         # Age

        bowlingtypeEntry.delete(0, tk.END)
        bowlingtypeEntry.insert(tk.END, row_data[1])
        field_info.delete(1.0, tk.END)
        field_info.insert(tk.END, row_data[2])
        # Teams

        # Fetch and display the image
        image_data = row_data[3]  # Image
        if image_data:
            image = Image.open(BytesIO(image_data))
            image = image.resize((298, 423))  # Adjust the size as needed
            photo = ImageTk.PhotoImage(image)

            global label2_framei
            # Clear any existing widgets inside the frame
            for widget in label2_framei.winfo_children():
                widget.destroy()

            # Create a label and display the image
            image_label = tk.Label(label2_framei, image=photo)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.pack()
    else:
        # If no data is found, show a message
        messagebox.showinfo("Error", "No data found for the entered name")
def add_data_to_db():
    if file_path == "":
        messagebox.showerror("Error", "Please select an image.")
        return
     # Replace with actual image path
    field_info_data = field_info.get("1.0", "end-1c")  # Retrieve text from Text widget
    bowling_style_data = style_value.get()
    bowling_type_data = type_value.get()
    with open(file_path, 'rb') as file:
        image_data = file.read()

    # Insert data into MySQL
    sql = '''INSERT INTO field (bowling_style, bowling_type, field_info, image)
             VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (bowling_style_data,  bowling_type_data, field_info_data, image_data))
    db.commit()
    messagebox.showinfo("Success", "Data inserted successfully!")


def select_image():
    global file_path
    file_path = filedialog.askopenfilename()
    display_selected_image(file_path)
def delete_data():
    try:
        name = style_value.get()

        # Delete data from the table
        query = "DELETE FROM field WHERE bowling_style = %s"
        cursor.execute(query, (name,))
        db.commit()
        messagebox.showinfo("Success", "Data deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def display_selected_image(file_path):
    try:
        global label2_framei

        # Clear any existing widgets inside the frame
        for widget in label2_framei.winfo_children():
            widget.destroy()

        # Load the image
        image = Image.open(file_path)
        image = image.resize((298, 423))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)

        # Create a label and display the image
        image_label = tk.Label(label2_framei, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack()  # Use pack() to display the label inside the frame
    except Exception as e:
        messagebox.showerror("Error", f"Error displaying image: {e}")

Field_label = Label(root, text="Field Determination", font="times 20 bold", foreground="blue", relief="raised", padx=10, pady=10)
Field_label.pack()

bowlingstyle_label = Label(root, text="Bowlingstyle", font="times 15 bold")
bowlingstyle_label.place(x=50, y=100)

bowlingtype_label = Label(root, text="Bowlingtype", font="times 15 bold")
bowlingtype_label.place(x=50, y=150)
fieldinfo_label = Label(root, text="Field Information", font="times 15 bold")
fieldinfo_label.place(x=50, y=210)


# Create label 2 with black border
label2_frame = tk.Frame(root, width=300, height=425, bd=2, relief="solid", bg="white")
label2_frame.place(relx=0.79, rely=0.48, anchor="center")
label2_framei = tk.Label(label2_frame, width=285, height=410)
label2_framei.place(relx=0.50, rely=0.50, anchor="center")

style_value = StringVar()
type_value = StringVar()
fieldinfo = StringVar()

bowlingstyleEntry = Entry(root, textvariable=style_value, font="times 15 bold")
bowlingstyleEntry.place(x=200, y=100)

bowlingtypeEntry = Entry(root, textvariable=type_value, font="times 15 bold")
bowlingtypeEntry.place(x=200, y=150)

select_imagebtn = Button(root, text="Select image", bg="blue", fg="white", font="times 15 bold", command=select_image)
select_imagebtn.place(x=670, y=510)
add_imagebtn = Button(root, text="Add", bg="blue", fg="white", font="times 15 bold",command=add_data_to_db)
add_imagebtn.place(x=450, y=570)
update_imagebtn = Button(root, text="Update", bg="blue", fg="white", font="times 15 bold",command=update_data)
update_imagebtn.place(x=550, y=570)
submit_imagebtn = Button(root, text="Delete", bg="blue", fg="white", font="times 15 bold",command=delete_data)
submit_imagebtn.place(x=650, y=570)
submit_imagebtnf = Button(root, text="fetch", bg="blue", fg="white", font="times 15 bold",command=fetch_data)
submit_imagebtnf.place(x=750, y=570)
field_info = tk.Text(root, wrap="word", height=14, width=65, bd=2)
field_info.place(x=55,y=250)

root.mainloop()









