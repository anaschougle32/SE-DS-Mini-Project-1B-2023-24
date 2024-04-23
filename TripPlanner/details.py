from tkinter import *
import tkinter as tk
from tkinter import messagebox

import mysql.connector

entry_field = None  # Define entry_field as a global variable
selected_value = None  # Define selected_value as a global variable


def fetch_data(destination, no_of_days):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1927__sid",
        database="tripplanner"
    )
    mycursor = mydb.cursor()

    # Ensure no_of_days is interpreted as an integer
    no_of_days = int(no_of_days)

    # Check if no_of_days is 5 or 7 and set the table name accordingly
    if no_of_days == 5:
        table_name = "day5"
    elif no_of_days == 7:
        table_name = "day7"
    else:
        # For other values of no_of_days, default to the day3 table
        table_name = "day3"

    # Query the database based on selected options
    query = f"SELECT * FROM {table_name} WHERE destination = '{destination}'"
    mycursor.execute(query)
    result = mycursor.fetchone()  # Assuming only one row is returned

    mydb.close()  # Close the database connection

    # Format the itinerary
    if result:
        itinerary = "\n".join([f"{i + 1}) {activity}" for i, activity in enumerate(result[1:])])  # Exclude destination
        return itinerary
    else:
        return None


def show_itineraries():
    global selected_value  # Declare selected_value as global so it can be accessed
    global entry_field  # Declare entry_field as global so it can be accessed

    destination = selected_value.get()
    no_of_days_str = entry_field.get()  # Retrieve value from the entry field

    if not no_of_days_str:
        # Handle case when no value is entered
        itineraries_label.config(text="Please enter number of days.")
        return

    try:
        no_of_days = int(no_of_days_str)
    except ValueError:
        # Handle case when entered value is not a valid integer
        itineraries_label.config(text="Please enter a valid number of days.")
        return

    # Check if the entered number of days is valid
    if no_of_days not in [3, 5, 7]:
        messagebox.showerror("Invalid Number of Days", "Please select a number of days from 3, 5, and 7.")
        return

    result = fetch_data(destination, no_of_days)
    if result:
        itineraries_label.config(text=f"Itineraries: {result}")
    else:
        itineraries_label.config(text="No itineraries found.")


def create_details(parent):
    global entry_field  # Declare entry_field as global so that it can be modified inside the function
    global selected_value  # Declare selected_value as global so it can be accessed

    main_window = Toplevel(parent)
    main_window.title("Details")
    main_window.configure(background="#111F4D")

    # Positioning the application
    window_width = 900
    window_height = 700
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    font_info1 = ('Arial', 20, 'italic')
    font_info2 = ('Arial', 25, 'italic')
    font_button = ('Arial', 15, 'bold')

    info1_label = Label(main_window, text="Enter your destination", fg='#f7f7f7', bg='#111F4D', font=font_info1)
    info1_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    selected_value = tk.StringVar(main_window)
    options = ["Maharashtra", "Delhi", "Goa", "Karnataka"]
    dropdown_menu = tk.OptionMenu(main_window, selected_value, *options)
    selected_value.set(options[0])  # Set default value
    dropdown_menu.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    info2_label = Label(main_window, text="Enter number of days", fg='#f7f7f7', bg='#111F4D', font=font_info2)
    info2_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field = Entry(main_window, width=50, justify="left")
    entry_field.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    Show = Button(main_window, text="Show Itineraries", foreground='#f7f7f7', background='#D24545',
                  activeforeground='#D24545', activebackground='#A94438', font=font_button, command=show_itineraries)
    Show.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    global itineraries_label
    itineraries_label = Label(main_window, text="Itineraries", fg='#f7f7f7', bg='#111F4D', font=font_info1)
    itineraries_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Configure column sizes
    main_window.grid_columnconfigure(0, weight=1, uniform="group1")
    main_window.grid_columnconfigure(1, weight=1, uniform="group1")
    main_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    main_window.grid_rowconfigure(2, weight=0)
    main_window.grid_rowconfigure(3, weight=0)
    main_window.grid_rowconfigure(4, weight=0)
    main_window.grid_rowconfigure(5, weight=0)
    main_window.grid_rowconfigure(6, weight=0)
    main_window.grid_rowconfigure(7, weight=0)


if __name__ == "__main__":
    window = Tk()
    create_details(window)
    window.mainloop()
