from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from dashboard import create_dashboard


def create_login(parent):
    def open_next_window():
        # Function to open the next window after successful login
        login_window.destroy()  # Close the login window
        next_window = create_dashboard(parent)  # Open the next window
        next_window.mainloop()  # Start the event loop for the next window

    def validate_login():
        # Function to validate login credentials
        username = username_field.get()
        password = Password_field.get()

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

            # Execute the query to check if the user exists
            sql = "SELECT * FROM reg WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            if user:
                # If user exists, open the next window
                open_next_window()
            else:
                # If user doesn't exist or credentials are incorrect, show error message
                messagebox.showerror("Error", "Invalid username or password")

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)

        finally:
            # Close cursor and connection
            if connection is not None and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    login_window = Toplevel(parent)
    # login_window.geometry("460x440")
    login_window.title("Login")
    login_window.configure(background="#111F4D")

    # Positioning the application

    window_width = 460
    window_height = 480

    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    login_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    login_window.iconphoto(True, icon)

    # Setting up the font
    font_login = ('Arial', 30, 'italic')
    font_username = ('Arial', 13, 'bold')
    font_password = ('Arial', 13, 'bold')
    font_login_button = ('Arial', 13, 'bold')
    font_button = ("Arial", 10, "bold")

    # Setting up the "login" label
    login_label = Label(login_window,
                        text="LOGIN",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_login)
    login_label.pack(padx=50, pady=50)

    # Username Label
    username_label = Label(login_window,
                           text="Username:",
                           fg='#f7f7f7',
                           bg='#111F4D',
                           font=font_username,
                           anchor="w")
    username_label.pack(padx=10, pady=4, anchor="w")
   # Setting up the text field for the age field
    # Setting up the text field for the age field
    username_field = Entry(login_window,
                           width=50,
                           justify="left",
                           # anchor="w"
                           )
    username_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Password Label
    Password_label = Label(login_window,
                           text="Password:",
                           fg='#f7f7f7',
                           bg='#111F4D',
                           font=font_password,
                           anchor="w")
    Password_label.pack(padx=10, pady=4, anchor="w")

    # Setting up the text field for the age field
    Password_field = Entry(login_window,
                           width=50,
                           justify="left",
                           # anchor="w",
                           show="*"
                           )
    Password_field.pack(pady=7, padx=(7, 0), anchor="w")

    # Setting up the button to login

    # Setting up the button to enter a new window

    # def feature_mainwindow():
    #      login_window.withdraw()  # Hide the main window
    #     dashboard_window = create_dashboard(login_window)
    # if dashboard_window:
    #         dashboard_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(login_window, dashboard_window))
    #
    #  def close_windows(main_window, popup_window):
    #     popup_window.destroy()
    #     main_window.destroy()

    Login = Button(login_window,
                   text="Login",
                   foreground='#f7f7f7',
                   background='#D24545',
                   activeforeground='#E43A19',
                   activebackground='#111F4D',
                   command=validate_login,
                   font=font_button
                   )
    Login.pack(padx=10, pady=20)

    # Setting up the back button

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(login_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(login_window, parent),
                  # command=back,
                  font=font_button
                  )
    Back.pack(padx=10, anchor='sw')

    return login_window


if __name__ == "__main__":
    window = Tk()
    create_login(window)
    window.mainloop()
