import tkinter as tk
from tkinter import Toplevel, Frame, Label, Button, OptionMenu, StringVar
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk


# Add the new columns to the database table 'suggestion'

# Update the fetch_image_data function to fetch the additional information
def fetch_image_data(destination, location):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='test',
                                             user='root',
                                             password='1927__sid')
        cursor = connection.cursor()

        cursor.execute(
            "SELECT image1, place1, loc1, time1, more1, " \
            "image2, place2, loc2, time2, more2, " \
            "image3, place3, loc3, time3, more3 FROM suggestions WHERE state=%s AND city=%s",
            (destination, location))
        image_data = cursor.fetchone()

        cursor.close()
        connection.close()

        return image_data
    except Error as e:
        print("Error fetching image data from database:", e)
        return None


def resize_image(image_path, width, height):
    try:
        # Open image using PIL
        image = Image.open(image_path)

        # Resize the image while preserving aspect ratio
        image.thumbnail((width, height))

        # Convert Image object to PhotoImage object
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print("Error resizing image:", e)
        return None


# Update the display_images_and_names function to display the additional information
def display_images_and_names(image_labels, name_labels, loc_labels, time_labels, more_labels, image_data):
    for i in range(min(len(image_labels), len(image_data) // 5)):
        image_path = image_data[i * 5]  # Image path is at even indices
        name = image_data[i * 5 + 1]  # Image name is at odd indices
        loc = image_data[i * 5 + 2]  # Location is at indices (odd + 1)
        time = image_data[i * 5 + 3]  # Time is at indices (odd + 2)
        more_info = image_data[i * 5 + 4]  # Additional information

        # Resize image and display in label
        photo_image = resize_image(image_path, 200, 200)
        if photo_image:
            image_labels[i].config(image=photo_image)
            image_labels[i].photo = photo_image  # Keep a reference to the image

        # Display name, location, time, and more information in labels
        name_labels[i].config(text=name)
        loc_labels[i].config(text=loc)
        time_labels[i].config(text=time)
        more_labels[i].config(text=more_info)


def on_display_button_click(state_var, location_var, image_labels, name_labels, loc_labels, time_labels, more_labels):
    # Get selected state and location
    state = state_var.get()
    location = location_var.get()

    # Fetch image data from database
    image_data = fetch_image_data(state, location)

    if image_data:
        # Display images, names, locations, times, and more information in labels
        display_images_and_names(image_labels, name_labels, loc_labels, time_labels, more_labels, image_data)
    else:
        print("No image data found for the given state and location")



def create_suggestion(parent):
    # Setting up the window
    accommodation_window = Toplevel(parent)
    accommodation_window.title("places")
    accommodation_window.configure(background="#111F4D")
    accommodation_window.resizable(False, False)

    input_frame = Frame(accommodation_window, bg='#111F4D')
    input_frame.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    image_frame = Frame(accommodation_window, bg='#111F4D')
    image_frame.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Positioning the application
    window_width = 900
    window_height = 630
    screen_width = accommodation_window.winfo_screenwidth()
    screen_height = accommodation_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    accommodation_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the font
    font_suggestions = ('Arial', 20, 'italic')
    font_button = ('Arial', 15, 'bold')

    # Setting up the "Suggestions" label
    accommodation_label = Label(accommodation_window, text="Search for places below", fg='#f7f7f7', bg='#111F4D',
                                font=font_suggestions)
    accommodation_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

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
            location_var.set('')
            # Populate cities based on the selected state
            location_menu['menu'].delete(0, 'end')
            for city in cities_by_state[selected_state]:
                location_menu['menu'].add_command(label=city, command=lambda city=city: location_var.set(city))

    # Create a dropdown for state selection
    state_var = StringVar(accommodation_window)
    state_var.set('Select State')  # Default value
    state_menu = OptionMenu(accommodation_window, state_var, *cities_by_state.keys(), command=on_state_select)
    state_menu.config(width=50)
    state_menu.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Create a dropdown for location selection
    location_var = StringVar(accommodation_window)
    location_var.set('Select Location')  # Default value
    location_menu = OptionMenu(accommodation_window, location_var, 'Select Location')
    location_menu.config(width=50)
    location_menu.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the back button
    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(accommodation_window, text="Back", foreground='#f7f7f7', background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438', command=lambda: feature_back(accommodation_window, parent),
                  font=font_button)
    Back.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    image_labels = []
    name_labels = []
    loc_labels = []
    time_labels = []
    more_labels = []
    for i in range(3):
        image_label = Label(image_frame)
        image_label.grid(row=0, column=i, padx=10, pady=5)
        image_labels.append(image_label)

        name_label = Label(image_frame)
        name_label.grid(row=1, column=i, padx=10, pady=5)
        name_labels.append(name_label)

        loc_label = Label(image_frame, text="", fg="blue", cursor="hand2", wraplength=200)
        loc_label.grid(row=2, column=i, padx=10, pady=5)
        loc_labels.append(loc_label)

        time_label = Label(image_frame, text="", fg="blue", cursor="hand2", wraplength=200)
        time_label.grid(row=3, column=i, padx=10, pady=5)
        time_labels.append(time_label)

        more_label = Label(image_frame, text="", wraplength=200)
        more_label.grid(row=4, column=i, padx=10, pady=5)
        more_labels.append(more_label)

    # Assuming you have the more_labels variable defined somewhere in your code

    # Call the on_display_button_click function with all required arguments
    Show = Button(accommodation_window, text="Display", foreground='#f7f7f7', background='#D24545',
                  activeforeground='#D24545', activebackground='#A94438', font=font_button,
                  command=lambda: on_display_button_click(state_var, location_var, image_labels,
                                                          name_labels, loc_labels, time_labels, more_labels))

    Show.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Configure column sizes
    accommodation_window.grid_columnconfigure(0, weight=1, uniform="group1")
    accommodation_window.grid_columnconfigure(1, weight=1, uniform="group1")
    accommodation_window.grid_columnconfigure(2, weight=1, uniform="group1")

    accommodation_window.grid_rowconfigure(2, weight=0)
    accommodation_window.grid_rowconfigure(3, weight=0)
    accommodation_window.grid_rowconfigure(4, weight=0)
    accommodation_window.grid_rowconfigure(5, weight=0)
    accommodation_window.grid_rowconfigure(6, weight=0)
    accommodation_window.grid_rowconfigure(7, weight=0)


if __name__ == "__main__":
    window = tk.Tk()
    create_accommodation_window(window)
    window.mainloop()
