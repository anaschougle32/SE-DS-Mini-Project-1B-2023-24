import tkinter as tk
from tkinter import ttk, messagebox
from subprocess import call
import mysql.connector
import sys

class UserComplaintStatus:
    def __init__(self, email):
        self.email = email
        self.root = tk.Tk()
        self.root.title("User Complaint Status")
        self.root.geometry('1760x600')
        self.root.configure(bg='#333333')

        self.tree = ttk.Treeview(self.root, columns=('Name', 'Taxi Model', 'Taxi No', 'Date', 'Email', 'Phone No', 'Complaint Reason', 'Status','Feedback'),
                            show='headings', height=10)

        # Define the headings
        self.tree.heading('Name', text='Name')
        self.tree.heading('Taxi Model', text='Taxi Model')
        self.tree.heading('Taxi No', text='Taxi No')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Phone No', text='Phone No')
        self.tree.heading('Complaint Reason', text='Complaint Reason')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Feedback',text='Feedback')

        # Set column widths
        for column in self.tree['columns']:
            self.tree.column(column, width=120)

        # Place the Treeview widget
        self.tree.pack(padx=10, pady=10)

        # Create the frame to display details
        self.detail_frame = tk.Frame(self.root, bg='#333333')
        self.detail_frame.pack(pady=10)

        # Bind the treeview select event to the on_select method
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # Create the "View" button to fetch and display complaints
        self.view_button = tk.Button(self.root, text="View", command=self.fetch_complaints)
        self.view_button.pack(pady=10)

        def dashboard():
            self.root.destroy()
            call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/dashboard.py',self.email])
        
        back_button = tk.Button(self.root, text="back", command=dashboard)
        back_button.pack(pady=10)

        # Call fetch_complaints function initially to populate the table
        self.fetch_complaints()

        self.root.mainloop()
    
    def fetch_complaints(self):
        try:
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Arju2003@",
                database="complaintsystem",
                auth_plugin="mysql_native_password",
            )

            # Create a cursor object to execute SQL queries
            mycursor = mydb.cursor()

            # SQL query to fetch complaints for the logged-in user's email
            query = "SELECT * FROM complain WHERE Email = %s"

            # Execute the query with the logged-in user's email
            print("Executing SQL query:", query, "with email:", self.email)
            mycursor.execute(query, (self.email,))

            # Fetch all the rows
            data = mycursor.fetchall()

            # Clear existing items in the Treeview
            self.tree.delete(*self.tree.get_children())

            # Insert fetched data into the Treeview table
            if len(data) != 0:
                for entry in data:
                    # Insert each row into the Treeview
                    self.tree.insert('', 'end', values=entry)
            else:
                print("No data found for email:", self.email)

            # Commit changes and close database connection
            mydb.commit()
            mycursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            # Display error message if an error occurs
            messagebox.showerror("Error", f"An error occurred: {err}")
            print("MySQL error:", err)

    def on_select(self, event):
        selected_item = self.tree.selection()[0]  # Get the selected item
        item_details = self.tree.item(selected_item, 'values')  # Get the details of the selected row
        
        # Clear previous details in the frame
        for widget in self.detail_frame.winfo_children():
            widget.destroy()

        # Display details in the frame
        for idx, (title, value) in enumerate(zip(self.tree["columns"], item_details)):
            tk.Label(self.detail_frame, text=title + ":", fg="white", bg="#333333", font=("Arial", 12)).grid(row=idx, column=0, sticky="e")
            tk.Label(self.detail_frame, text=value, fg="white", bg="#333333", font=("Arial", 12)).grid(row=idx, column=1, sticky="w")

if __name__ == "__main__":
    email = sys.argv[1]  # Get the email from command line argument
    user_complaint_status = UserComplaintStatus(email)
