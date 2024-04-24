from subprocess import call
from tkinter import ttk, messagebox
import tkinter as tk
import mysql.connector

def submit_complaint():
    # Clear existing data in the Treeview
    for row in tree.get_children():
        tree.delete(row)
        
    # Fetch updated data from the database
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM complain")  # Assuming 'complain' is your table name
        data = cursor.fetchall()

        # Insert data into the Treeview table
        for entry in data:
            tree.insert('', 'end', values=entry)
        
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error fetching data: {error}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arju2003@",
        database="complaintsystem",
        auth_plugin="mysql_native_password",
    )

def on_select(event):
    # Clear previous details in the detail_frame
    for widget in detail_frame.winfo_children():
        widget.destroy()

    # Get the selected item from the Treeview
    selected_item = tree.selection()[0]
    item_details = tree.item(selected_item, 'values')
    
    # Display details in the detail_frame
    for idx, (title, value) in enumerate(zip(tree["columns"], item_details)):
        tk.Label(detail_frame, text=title + ":", fg="white", bg="#333333", font=("Arial", 12)).grid(row=idx, column=0, sticky="e")
        tk.Label(detail_frame, text=value, fg="white", bg="#333333", font=("Arial", 12)).grid(row=idx, column=1, sticky="w")

# Create the main window
root = tk.Tk()
root.title("admincomplaints")
root.geometry('1100x680')
root.configure(bg='#333333')

# Create a Treeview widget for the table
tree = ttk.Treeview(root, columns=('Name', 'Taxi Model', 'Taxi No', 'Date', 'Email', 'Phone No', 'Complaint Reason', 'Status', 'Feedback'),
                    show='headings', height=10)

# Define the headings
tree.heading('Name', text='Name')
tree.heading('Taxi Model', text='Taxi Model')
tree.heading('Taxi No', text='Taxi No')
tree.heading('Date', text='Date')
tree.heading('Email', text='Email')
tree.heading('Phone No', text='Phone No')
tree.heading('Complaint Reason', text='Complaint Reason')
tree.heading('Status', text='Status')
tree.heading('Feedback', text='Feedback')

# Set column widths
for column in tree['columns']:
    tree.column(column, width=120)

# Place the Treeview widget
tree.pack(padx=10, pady=10)

# Create the "View" button
submit_button = tk.Button(root, text="View", command=submit_complaint, width=10)
submit_button.pack(pady=10)


def admindashboard():
    root.destroy()
    call(['python','C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/admindashboard.py'])
    
back_button = tk.Button(root, text="Back", command=admindashboard, width=10)
back_button.pack(pady=10)

# Create the frame to display details
detail_frame = tk.Frame(root, bg='#333333')
detail_frame.pack(pady=10)

# Bind the treeview select event to the on_select method
tree.bind("<<TreeviewSelect>>", on_select)

# Run the application
root.mainloop()
