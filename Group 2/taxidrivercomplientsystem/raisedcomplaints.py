from subprocess import call
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import mysql.connector
from datetime import datetime
import sys

class RaiseComplaints:
    def __init__(self, email):
        self.email = email

        # Function to submit complaint to MySQL database
        def submit_complaint():
            # Get the form data
            name = self.name_entry.get()
            taxi_model = self.taxi_model_entry.get()
            taxi_no = self.taxi_no_entry.get()
            date_str = self.date_entry.get()  # Get the date string
            phone_no = self.phone_no_entry.get()
            complaint_reason = self.complaint_reason_entry.get("1.0", "end-1c")

            try:
                # Convert date string to datetime object
                date = datetime.strptime(date_str, '%d-%m-%y')

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

                # SQL query to insert data into the complain table
                sql = "INSERT INTO complain (`Name`, `Taxi Model`, `Taxi No`, `Date`, `Email`, `Phone No`, `Complaint Reason`, `status`, `Feedback`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (name, taxi_model, taxi_no, date.strftime('%Y-%m-%d'), self.email, phone_no, complaint_reason, 'Pending', 'Not yet')

                # Execute the SQL query
                mycursor.execute(sql, val)

                # Commit changes to the database
                mydb.commit()

                # Close the cursor and database connection
                mycursor.close()
                mydb.close()

                # Inform the user that the complaint has been submitted
                messagebox.showinfo("Success", "Complaint submitted successfully")

            except mysql.connector.Error as err:
                # Show a message box indicating the error
                messagebox.showerror("Error", f"An error occurred: {err}")

        # Create the root window
        self.root = tk.Tk()
        self.root.title("Raise Complaints")
        self.root.geometry('779x550')
        self.root.configure(bg='#333333')

        # Load and resize the background image
        bg_image = Image.open("C:\\Users\\Arju salmani\\PycharmProjects\\taxidrivercomplientsystem\\bg_image.png")  # Change to your image file path
        bg_image = bg_image.resize((779, 550), Image.LANCZOS)  # Resize image to fit the window
        bg_image = ImageTk.PhotoImage(bg_image)

        # Create a label with the background image and place it on the root window
        background_label = tk.Label(self.root, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = bg_image  # Keep a reference to avoid garbage collection

        # Place the "Complain Form" label at the top center
        complain_label = ttk.Label(self.root, text="Complain Form", font=("Helvetica", 16, "bold"), background='WHITE',
                                   foreground='BLUE')
        complain_label.place(relx=0.5, rely=0.05, anchor='center')

        # Create form fields and labels
        name_label = ttk.Label(self.root, text="Name:")
        name_label.place(x=50, y=100)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.place(x=150, y=100)

        taxi_model_label = ttk.Label(self.root, text="Taxi Model:")
        taxi_model_label.place(x=50, y=130)
        self.taxi_model_entry = ttk.Entry(self.root)
        self.taxi_model_entry.place(x=150, y=130)

        taxi_no_label = ttk.Label(self.root, text="Taxi No:")
        taxi_no_label.place(x=50, y=160)
        self.taxi_no_entry = ttk.Entry(self.root)
        self.taxi_no_entry.place(x=150, y=160)

        date_label = ttk.Label(self.root, text="Date:")
        date_label.place(x=50, y=190)
        self.date_entry = ttk.Entry(self.root)
        self.date_entry.place(x=150, y=190)

        email_label = ttk.Label(self.root, text="Email:")
        email_label.place(x=50, y=220)
        self.email_entry = ttk.Entry(self.root)
        self.email_entry.place(x=150, y=220)
        self.email_entry.insert(0, self.email)  # Insert the email into the entry field

        phone_no_label = ttk.Label(self.root, text="Phone No:")
        phone_no_label.place(x=50, y=250)
        self.phone_no_entry = ttk.Entry(self.root)
        self.phone_no_entry.place(x=150, y=250)

        complaint_reason_label = ttk.Label(self.root, text="Complaint Reason:")
        complaint_reason_label.place(x=50, y=280)
        self.complaint_reason_entry = tk.Text(self.root, height=5, width=30)
        self.complaint_reason_entry.place(x=50, y=310)

        # Create and place buttons
        submit_button = ttk.Button(self.root, text="Submit", command=submit_complaint)
        submit_button.place(relx=0.5, rely=0.9, anchor='center')

        back_button = ttk.Button(self.root, text="Back", command=self.dashboard)
        back_button.place(relx=0.95, rely=0.05, anchor='ne')

        self.root.mainloop()

    def dashboard(self):
        # Close the current window and return to the dashboard
        self.root.destroy()
        call(['python', 'C:/Users/Arju salmani/PycharmProjects/taxidrivercomplientsystem/dashboard.py', self.email])


# Usage
if __name__ == "__main__":
    email = sys.argv[1]  # Get the email from command line argument
    raise_complaints = RaiseComplaints(email)

