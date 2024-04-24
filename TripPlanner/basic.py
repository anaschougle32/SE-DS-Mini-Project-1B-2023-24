import tkinter as tk
from tkinter import Toplevel, Label, OptionMenu, StringVar, Button
import mysql.connector


def fetch_data(state, city, category):
    # Connect to MySQL database (replace with your database credentials)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1927__sid",
        database="test"
    )
    mycursor = mydb.cursor()

    # Define column names based on category
    if category == "grocery":
        columns = ["location", "store1", "phn_no1", "store2", "phn_no2"]
        name_index = 1
        detail_index = 0
        info_format = "{name} - {detail}"
    elif category == "hospital":
        columns = ["location", "hospital1", "call_on", "hospital2", "phn_no2"]
        name_index = 1
        detail_index = 0
        info_format = "{name} - {detail}"
    elif category == "restaurants":
        columns = ["location", "restaurant1", "phn_no1", "restaurant2", "phn_no2"]
        name_index = 1
        detail_index = 0
        info_format = "{name}, {detail}"

    # Construct the SELECT query using the appropriate column names
    query = f"SELECT {', '.join(columns)} FROM {category} WHERE state = '{state}' AND city = '{city}'"

    mycursor.execute(query)
    results = mycursor.fetchall()

    mydb.close()  # Close the database connection

    # Format the results
    formatted_results = []
    for result in results:
        locations_info = ""
        # Concatenate restaurant names and phone numbers
        for i in range(name_index, len(result), 2):
            if result[i] is not None and result[i+1] is not None:
                name = result[i]
                detail = result[i+1]
                locations_info += info_format.format(name=name, detail=detail) + ", "
        locations_info = locations_info.rstrip(", ")  # Remove trailing comma and space
        formatted_result = f"• Location: {result[detail_index]}\n• {category.capitalize()}: {locations_info}"
        formatted_results.append(formatted_result)

    return formatted_results



def create_basic(parent):
    # Setting up the window
    basic_window = Toplevel(parent)
    basic_window.title("Basic Necessities")
    basic_window.configure(background="#111F4D")
    basic_window.resizable(False, False)

    window_width = 900
    window_height = 630
    screen_width = basic_window.winfo_screenwidth()
    screen_height = basic_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    basic_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    font_basic = ('Arial', 30, 'italic')
    font_button = ('Arial', 15, 'italic')

    # Setting up the "Suggestions" label
    basic_label = Label(basic_window,
                        text="Basic Necessities",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_basic)
    basic_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

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
    state_var = StringVar(basic_window)
    state_var.set('Select State')  # Default value
    state_menu = OptionMenu(basic_window, state_var, *cities_by_state.keys(), command=on_state_select)
    state_menu.config(width=50)
    # Pack the dropdown menu
    state_menu.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Create a dropdown for city selection
    city_var = StringVar(basic_window)
    city_var.set('Select City')  # Default value
    city_menu = OptionMenu(basic_window, city_var, 'Select City')
    city_menu.config(width=50)
    # Pack the dropdown menu
    city_menu.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    def on_category_button_click(category):
        state = state_var.get()
        city = city_var.get()
        if state != 'Select State' and city != 'Select City':
            # Fetch and display information
            places_info = fetch_data(state, city, category)
            if places_info:
                info_text.config(text="\n\n".join(places_info))
            else:
                info_text.config(text="No information available.")

    # Create buttons for different categories
    Show1 = Button(basic_window, text="Grocery", foreground='#f7f7f7', background='#D24545',
                   activeforeground='#D24545', activebackground='#A94438', font=font_button,
                   command=lambda: on_category_button_click("grocery"))
    Show1.grid(row=3, column=0, padx=5, pady=10, sticky='n')

    Show2 = Button(basic_window, text="Hospitals", foreground='#f7f7f7', background='#D24545',
                   activeforeground='#D24545', activebackground='#A94438', font=font_button,
                   command=lambda: on_category_button_click("hospital"))
    Show2.grid(row=3, column=1, padx=5, pady=10, sticky='n')

    Show3 = Button(basic_window, text="Restaurants", foreground='#f7f7f7', background='#D24545',
                   activeforeground='#D24545', activebackground='#A94438', font=font_button,
                   command=lambda: on_category_button_click("restaurants"))
    Show3.grid(row=3, column=2, padx=5, pady=10, sticky='n')

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(basic_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(basic_window, parent),
                  font=font_button
                  )
    Back.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    # Label to display information
    info_text = Label(basic_window, bg="#3652AD", width=50, height=13, font=("Arial", 15))
    info_text.grid(row=4, column=0, columnspan=3, padx=80, pady=10, sticky='new')

    # Configure column sizes
    basic_window.grid_columnconfigure(0, weight=1, uniform="group1")
    basic_window.grid_columnconfigure(1, weight=1, uniform="group1")
    basic_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    basic_window.grid_rowconfigure(2, weight=1)
    basic_window.grid_rowconfigure(3, weight=1)
    basic_window.grid_rowconfigure(4, weight=1)
    basic_window.grid_rowconfigure(5, weight=1)

    basic_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    create_basic(root)
    root.mainloop()
