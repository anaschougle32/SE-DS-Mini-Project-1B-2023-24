import tkinter as tk
from tkinter import Toplevel, Label, OptionMenu, StringVar, Button
import mysql.connector


def fetch_data(state, city):
    # Connect to MySQL database (replace with your database credentials)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1927__sid",
        database="test"
    )
    mycursor = mydb.cursor()

    # Query the database based on selected options
    query = f"SELECT place, location, timing, more_info FROM suggest WHERE state = '{state}' AND city = '{city}'"
    mycursor.execute(query)
    results = mycursor.fetchall()

    mydb.close()  # Close the database connection

    # Format the results
    formatted_results = []
    for result in results:
        formatted_result = "\n".join([f"• {detail}" for detail in result])
        formatted_results.append(formatted_result)

    return formatted_results


def create_suggestion(parent):
    # Setting up the window
    suggestions_window = Toplevel(parent)
    suggestions_window.title("Suggestions")
    suggestions_window.configure(background="#111F4D")
    suggestions_window.resizable(False, False)

    # Positioning the application
    window_width = 900
    window_height = 700

    screen_width = suggestions_window.winfo_screenwidth()
    screen_height = suggestions_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    suggestions_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    font_suggestions = ('Arial', 25, 'italic')
    font_button = ('Arial', 15, 'italic')

    suggestions_label = Label(suggestions_window,
                              text="SUGGESTIONS FOR PLACES",
                              fg='#f7f7f7',
                              bg='#111F4D',
                              font=font_suggestions)
    suggestions_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Define a dictionary of cities for each state
    cities_by_state = {
        'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik'],
        'Delhi': ['Delhi'],
        'Karnataka': ['Bangalore', 'Mysore', 'Hubli', 'Mangalore']
    }

    def on_state_select(*args):
        selected_state = state_var.get()
        if selected_state:
            # Clear previous cities
            city_var.set('')
            # Populate cities based on the selected state
            city_menu['menu'].delete(0, 'end')
            for city in cities_by_state[selected_state]:
                city_menu['menu'].add_command(label=city, command=lambda city=city: city_var.set(city))

    # Create a dropdown for state selection
    state_var = StringVar(suggestions_window)
    state_var.set('Select State')  # Default value
    state_menu = OptionMenu(suggestions_window, state_var, *cities_by_state.keys(), command=on_state_select)
    state_menu.config(width=50)
    # Pack the dropdown menu
    state_menu.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Create a dropdown for city selection
    city_var = StringVar(suggestions_window)
    city_var.set('Select City')  # Default value
    city_menu = OptionMenu(suggestions_window, city_var, 'Select City')
    city_menu.config(width=50)
    # Pack the dropdown menu
    city_menu.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    def on_suggest_button_click():
        state = state_var.get()
        city = city_var.get()
        if state != 'Select State' and city != 'Select City':
            # Fetch and display information
            places_info = fetch_data(state, city)
            if places_info:
                # Display information in each label
                for i, info in enumerate(places_info):
                    if i < 3:  # Assuming you have only 3 labels
                        information_labels[i].config(text=info)
            else:
                # If no places found, clear all labels
                for label in information_labels:
                    label.config(text="No places found for the selected location.")

    Show = Button(suggestions_window, text="Suggest", foreground='#f7f7f7', background='#D24545',
                  activeforeground='#D24545', activebackground='#A94438', font=font_button,
                  command=on_suggest_button_click
                  )

    Show.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Create label widgets for displaying information
    information_labels = []
    for i in range(3):  # Assuming you want to display information in three labels
        label = Label(suggestions_window, bg="#3652AD", width=25, height=15, font=("Arial", 15))
        label.grid(row=4, column=i, padx=10, pady=10, sticky='n')
        information_labels.append(label)

        def feature_back(current_window, previous_window):
            current_window.withdraw()  # Hide the current window
            previous_window.deiconify()

        Back = Button(suggestions_window,
                      text="Back",
                      foreground='#f7f7f7',
                      background='#D24545',
                      activeforeground='#D24545',
                      activebackground='#A94438',
                      command=lambda: feature_back(suggestions_window, parent),
                      font=font_button
                      )
        Back.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='w')

        suggestions_window.grid_columnconfigure(0, weight=1, uniform="group1")
        suggestions_window.grid_columnconfigure(1, weight=1, uniform="group1")
        suggestions_window.grid_columnconfigure(2, weight=1, uniform="group1")

        suggestions_window.grid_rowconfigure(2, weight=0)
        suggestions_window.grid_rowconfigure(3, weight=0)
        suggestions_window.grid_rowconfigure(4, weight=0)
        suggestions_window.grid_rowconfigure(5, weight=0)
        suggestions_window.grid_rowconfigure(6, weight=0)
        suggestions_window.grid_rowconfigure(7, weight=0)


# Example usage
root = tk.Tk()
create_suggestion(root)
root.mainloop()
