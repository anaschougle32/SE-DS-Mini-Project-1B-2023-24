from tkinter import *
import tkinter as tk
import mysql.connector


def submit_experience(entry_field):
    experience_text = entry_field.get("1.0", "end-1c")
    print("Experience entered:", experience_text)

    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1927__sid",
        database="test"
    )
    cursor = conn.cursor()

    # Insert the experience into the database
    insert_query = "INSERT INTO experiences (experience) VALUES (%s)"
    cursor.execute(insert_query, (experience_text,))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()


def create_expwindow(parent):
    # Setting up the window
    exp_window = Toplevel(parent)
    exp_window.title("Experience")
    exp_window.configure(background="#111F4D")
    exp_window.resizable(False, False)

    # Positioning the application
    window_width = 900
    window_height = 630
    screen_width = exp_window.winfo_screenwidth()
    screen_height = exp_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    exp_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    exp_window.iconphoto(True, icon)

    font_exp = ('Arial', 25, 'italic')
    font_button = ('Arial', 20, 'bold')

    exp_label = Label(exp_window,
                      text="Enter your Experience",
                      fg='#f7f7f7',
                      bg='#111F4D',
                      font=font_exp)
    exp_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field = tk.Text(exp_window, width=70, height=20)
    entry_field.grid(row=1, column=0, columnspan=3, padx=10, pady=15)

    submit_button = Button(exp_window, text="Submit", foreground='#f7f7f7', background='#D24545',
                           activeforeground='#D24545',
                           activebackground='#A94438', font=font_button,
                           command=lambda: submit_experience(entry_field))
    submit_button.grid(row=3, column=1, padx=5, pady=10, sticky='n')

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(exp_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(exp_window, parent),
                  font=font_button
                  )
    Back.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    # Configure column sizes
    exp_window.grid_columnconfigure(0, weight=1, uniform="group1")
    exp_window.grid_columnconfigure(1, weight=1, uniform="group1")
    exp_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    exp_window.grid_rowconfigure(2, weight=1)
    exp_window.grid_rowconfigure(3, weight=1)
    exp_window.grid_rowconfigure(4, weight=1)
    exp_window.grid_rowconfigure(5, weight=1)

    exp_window.mainloop()


if __name__ == "__main__":
    window = Tk()
    create_expwindow(window)
    window.mainloop()
