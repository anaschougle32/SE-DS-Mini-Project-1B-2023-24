from inspect import FrameInfo
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
from tkinter import NW, filedialog
from subprocess import call
from PIL import ImageTk, Image
import mysql.connector

# Function to fetch data from MySQL and populate the table
def fetch_data():
    # Connect to MySQL database
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Arju2003@",
            database="complaintsystem",
            auth_plugin="mysql_native_password",
        )
        cursor = conn.cursor()

        # Execute SQL query to fetch data from the complaint table
        cursor.execute("SELECT `Name`, `Taxi Model`, `Taxi No`, `Date`, `Email`, `Phone No`, `Complaint Reason`, `Status` FROM complain")
        rows = cursor.fetchall()

        # Insert data into the Treeview table
        for row in rows:
            tree.insert('', 'end', values=row)

        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")

# Function to update the selected row in the database
def update_data():
    selected_item = tree.focus()  # Get the item ID of the selected row
    if selected_item:  # Ensure that a row is selected
        item_details = tree.item(selected_item, 'values')  # Get the details of the selected row
        feedback = feedback_entry.get("1.0", "end-1c")  # Get feedback from the text box
        new_status = status_var.get()  # Get the updated status from the combo box
        email = item_details[4]  # Get email from the selected row

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Arju2003@",
                database="complaintsystem",
                auth_plugin="mysql_native_password",
            )
            cursor = conn.cursor()

            # Update the row in the database based on email
            cursor.execute("UPDATE complain SET `Feedback` = %s, `Status` = %s WHERE `Email` = %s",
                           (feedback, new_status, email))

            # Commit changes and close connection
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Data updated successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error updating data: {e}")

# Create the main window
root = tk.Tk()
root.title("admincomplaints")
root.geometry('990x870')
root.configure(bg='#333333')

Dashboard_label = tk.Label(text='Listed Complaints', bg='#333333', fg="white", font=("Arial 28 underline"))
Dashboard_label.pack()


def admindashboard():
    root.destroy()
    call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/admindashboard.py'])


# Function to handle row selection
def on_select(event):
    selected_item = tree.focus()  # Get the item ID of the selected row
    if selected_item:  # Ensure that a row is selected
        item_details = tree.item(selected_item, 'values')  # Get the details of the selected row
        # Clear previous text
        for widget in detail_frame.winfo_children():
            widget.destroy()
        # Display details in text fields
        for idx, (title, value) in enumerate(zip(tree_columns, item_details)):
            tk.Label(detail_frame, text=title + ":", fg="white", bg="#333333", font=("Arial", 12)).grid(row=idx,
                                                                                                           column=0,
                                                                                                           sticky="e")
            tk.Label(detail_frame, text=value, fg="white", bg="#333333", font=("Arial", 12)).grid(row=idx,
                                                                                                     column=1,
                                                                                                     sticky="w")
        # Add feedback text box
        feedback_label = tk.Label(detail_frame, text="Feedback:", fg="white", bg="#333333", font=("Arial", 12))
        feedback_label.grid(row=idx + 1, column=0, sticky="e")
        global feedback_entry
        feedback_entry = tk.Text(detail_frame, width=40, height=5)
        feedback_entry.grid(row=idx + 1, column=1, sticky="w")

        # Add combo box for status
        status_label = tk.Label(detail_frame, text="Status:", fg="white", bg="#333333", font=("Arial", 12))
        status_label.grid(row=idx + 2, column=0, sticky="e")
        global status_var
        status_var = tk.StringVar(value=item_details[-1])  # Use the status value from the selected row
        status_combo = ttk.Combobox(detail_frame, textvariable=status_var, values=["Pending", "Resolved"],
                                    state="readonly")
        status_combo.grid(row=idx + 2, column=1, sticky="w")

        # Add Update button
        update_button = tk.Button(detail_frame, text="Update", command=update_data, width=10)
        update_button.grid(row=idx + 3, columnspan=2, pady=10)


# Create a Treeview widget for the table
tree = ttk.Treeview(root, columns=('Name', 'Taxi Model', 'Taxi No', 'Date', 'Email', 'Phone No', 'Complaint Reason', 'Status'),
                    show='headings', height=10)

# Define the headings
tree_columns = ['Name', 'Taxi Model', 'Taxi No', 'Date', 'Email', 'Phone No', 'Complaint Reason', 'Status']
for col in tree_columns:
    tree.heading(col, text=col)

# Set column widths
for column in tree_columns:
    tree.column(column, width=120)

# Place the Treeview widget
tree.pack(padx=10, pady=10)

# Bind the selection event to the on_select function
tree.bind("<<TreeviewSelect>>", on_select)

# Create a frame to display details
detail_frame = tk.Frame(root, bg="#333333")
detail_frame.pack(padx=50, pady=10, fill="both")

# Create the "View" button
view_button = tk.Button(root, text="View", command=fetch_data, width=10)
view_button.pack(pady=10)

# submit_button = tk.Button(root, text="Submit", command=submit_complaint, width=10)
# submit_button.pack(pady=10)

back_button = tk.Button(root, text="Back", command=admindashboard, width=10)
back_button.pack(pady=10)

root.mainloop()
