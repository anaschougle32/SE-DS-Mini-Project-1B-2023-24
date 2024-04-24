from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from dashboard import create_dashboard


def create_register(parent):
    # Setting Up the window
    def open_next_window():
        # Function to open the next window after registration
        register_window.destroy()  # Close the current window
        next_window = create_dashboard(parent)  # Open the next window

    def show_warning():
        # Show warning message if any field is empty
        messagebox.showwarning("Warning", "Please fill all the details")

    def show_error_message(message):
        # Show error message
        messagebox.showerror("Error", message)

    register_window = Toplevel(parent)
    register_window.geometry("460x440")
    register_window.title("Register")
    register_window.configure(background="#111F4D")

    # Positioning the application

    window_width = 460
    window_height = 480

    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    register_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    register_window.iconphoto(True, icon)

    # Setting up the font
    font_Register = ('Arial', 30, 'italic')
    font_Registerinfo = ('Arial', 10, 'italic')
    font_name = ('Arial', 13, 'bold')
    font_email = ('Arial', 13, 'bold')
    font_username = ('Arial', 13, 'bold')
    font_password = ('Arial', 13, 'bold')
    font_register_button = ('Arial', 13, 'bold')
    font_button = ("Arial", 10, "bold")

    # Setting up the "Register" label
    Register_label = Label(register_window,
                           text="REGISTER",
                           fg='#f7f7f7',
                           bg='#111F4D',
                           font=font_Register)
    Register_label.pack(padx=10, pady=10)

    # Setting up the "Register" label info

    Registerinfo_label = Label(register_window,
                               text="Fill the details below",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_Registerinfo)
    Registerinfo_label.pack()

    # Setting up the Register form components/widgets

    # Name label
    Name_label = Label(register_window,
                       text="Full Name:",
                       fg='#f7f7f7',
                       bg='#111F4D',
                       font=font_name,
                       anchor="w")
    Name_label.pack(padx=10, pady=4, anchor="w")

    # Setting up the text field for the name field
    name_field = Entry(register_window,
                       width=50,
                       justify="left",
                       # anchor="w"
                       )
    name_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Email Label
    Email_label = Label(register_window,
                        text="Email:",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_email,
                        anchor="w")
    Email_label.pack(padx=10, pady=4, anchor="w")

    # Setting up the text field for the email field
    email_field = Entry(register_window,
                        width=50,
                        justify="left",
                        # anchor="w"
                        )
    email_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Username Label
    username_label = Label(register_window,
                           text="Username:",
                           fg='#f7f7f7',
                           bg='#111F4D',
                           font=font_username,
                           anchor="w")
    username_label.pack(padx=10, pady=4, anchor="w")

    # Setting up the text field for the age field
    username_field = Entry(register_window,
                           width=50,
                           justify="left",
                           # anchor="w"
                           )
    username_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Password Label
    Password_label = Label(register_window,
                           text="Password:",
                           fg='#f7f7f7',
                           bg='#111F4D',
                           font=font_password,
                           anchor="w")
    Password_label.pack(padx=10, pady=4, anchor="w")

    # Setting up the text field for the age field
    Password_field = Entry(register_window,
                           width=50,
                           justify="left",
                           # anchor="w",
                           show="*"
                           )
    Password_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Setting up the button to enter a new window

    def insert_into_database():
        # Get data from the input fields
        full_name = name_field.get()
        password = Password_field.get()
        email = email_field.get()
        username = username_field.get()

        # Check if any field is empty
        if not full_name or not password:
            show_warning()
            return

        # Initialize connection variable
        connection = None

        try:
            # Establish connection to MySQL database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1927__sid",
                database="test"
            )
            cursor = connection.cursor()

            # Insert data into users table
            sql = "INSERT INTO reg (full_name,email,username,password) VALUES (%s, %s,%s,%s)"
            values = (full_name, email, username, password)
            cursor.execute(sql, values)

            # Commit changes,%
            connection.commit()
            print("Record inserted successfully into users table")

            # Show success message
            messagebox.showinfo("Success", "Registered successfully")

            # Open the next window
            open_next_window()

        except mysql.connector.Error as error:
            error_message = str(error)
            if "Duplicate entry" in error_message:
                show_error_message("User already exists!")
            else:
                show_error_message(f"Failed to insert record into MySQL table: {error_message}")

        finally:
            # Close cursor and connection
            if connection is not None and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    # def feature_register_window():
    #     register_window.withdraw()  # Hide the register window
    #     mainfeature_window = create_dashboard(register_window)
    #     if mainfeature_window:
    #         mainfeature_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(register_window, mainfeature_window))
    #
    # def close_windows(main_window, popup_window):
    #     popup_window.destroy()
    #     main_window.destroy()

    Register = Button(register_window,
                      text="Register",
                      foreground='#f7f7f7',
                      background='#D24545',
                      activeforeground='#E43A19',
                      activebackground='#111F4D',
                      command=insert_into_database,
                      font=font_register_button
                      )
    Register.pack(padx=10, pady=20)

    # Setting up the back button

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(register_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(register_window, parent),
                  # command=back,
                  font=font_button
                  )
    Back.pack(padx=10, anchor='sw')

    return register_window  # Return the created window


if __name__ == "__main__":
    window = Tk()
    create_register(window)
    previous_window = window
    window.mainloop()
