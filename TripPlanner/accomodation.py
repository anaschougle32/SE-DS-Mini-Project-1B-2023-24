import webbrowser
from tkinter import *
import tkinter as tk
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
from io import BytesIO


def fetch_image_data(destination, location, price_range):
    try:
        # Connect to the database
        connection = mysql.connector.connect(host='localhost',
                                             database='test',
                                             user='root',
                                             password='1927__sid')
        cursor = connection.cursor()

        # Fetch image data (paths, names, and URLs) from the database based on destination, location, and price range
        cursor.execute(
            "SELECT accomodation1, place1, url1, accomodation2, place2, url2, accomodation3, place3, url3 FROM accom WHERE destination=%s AND location=%s AND pricerange=%s",
            (destination, location, price_range))
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


def display_images_and_names(image_labels, name_labels, url_labels, image_data):
    for i in range(3):
        image_path = image_data[i * 3]  # Image path is at even indices
        name = image_data[i * 3 + 1]  # Image name is at odd indices
        url = image_data[i * 3 + 2]  # Image URL is at indices (odd + 1)

        # Resize image and display in label
        photo_image = resize_image(image_path, 200, 200)
        image_labels[i].config(image=photo_image)
        image_labels[i].photo = photo_image  # Keep a reference to the image

        # Display name in label
        name_labels[i].config(text=name)

        # Display URL as a clickable link
        url_labels[i].config(text=url, fg="blue", cursor="hand2")
        url_labels[i].bind("<Button-1>", lambda e, url=url: callback(url))


def callback(url):
    # Open URL in a web browser when clicked
    webbrowser.open_new(url)


def on_display_button_click(state_var, location_var, price_range_var, image_labels, name_labels, url_labels):
    # Get selected state, location, and price range
    state = state_var.get()
    location = location_var.get()
    price_range = price_range_var.get()

    # Fetch image data from database
    image_data = fetch_image_data(state, location, price_range)

    if image_data:
        # Display images, names, and URLs in labels
        display_images_and_names(image_labels, name_labels, url_labels, image_data)
    else:
        print("No image data found for the given state, location, and price range.")


def create_accomodationwindow(parent, destination_entry=None):
    # Setting up the window
    accomodation_window = Toplevel(parent)
    accomodation_window.title("Accommodation")
    accomodation_window.configure(background="#111F4D")
    accomodation_window.resizable(False, False)

    input_frame = Frame(accomodation_window,
                        bg='#111F4D'
                        )
    input_frame.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    image_frame = Frame(accomodation_window,
                        bg='#111F4D'
                        )
    image_frame.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Positioning the application

    window_width = 900
    window_height = 630

    screen_width = accomodation_window.winfo_screenwidth()
    screen_height = accomodation_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    accomodation_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    # icon = PhotoImage(file='logo.png')
    # accomodation_window.iconphoto(True, icon)

    # Setting up the font
    font_suggestions = ('Arial', 20, 'italic')
    font_nearbyinfo = ('Arial', 15, 'bold')
    font_button = ('Arial', 15, 'bold')
    font_option = ('Arial', 10, 'bold')
    font_view = ('Arial', 10, 'bold')

    # Setting up the "Suggestions" label
    accomodation_label = Label(accomodation_window,
                               text="Search for hotels below",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_suggestions)
    accomodation_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the label for "Here are some nearby places"
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
    state_var = StringVar(accomodation_window)
    state_var.set('Select State')  # Default value
    state_menu = OptionMenu(accomodation_window, state_var, *cities_by_state.keys(), command=on_state_select)
    state_menu.config(width=50)
    # Pack the dropdown menu
    state_menu.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Create a dropdown for location selection
    location_var = StringVar(accomodation_window)
    location_var.set('Select Location')  # Default value
    location_menu = OptionMenu(accomodation_window, location_var, 'Select Location')
    location_menu.config(width=50)
    location_menu.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the back button

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(accomodation_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(accomodation_window, parent),
                  font=font_button
                  )
    Back.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    # Setting up the price range radio button

    def on_radio_change():
        # Function to handle changes in the radio button selection
        # selected_option = radio_var.get()
        # print("Selected option:", selected_option)
        pass

    label = Label(accomodation_window,
                  text="Select a price option:",
                  fg='#f7f7f7',
                  bg='#111F4D',
                  font=font_option
                  )
    label.grid(row=3, columnspan=4, padx=10, pady=10)

    # Create a variable to store the selected option
    price_range_var = StringVar()

    # Create radio buttons
    radio1 = Radiobutton(accomodation_window,
                         text="Low",
                         variable=price_range_var,
                         value="Low",
                         command=on_radio_change)
    radio1.grid(row=4, columnspan=4, padx=(250, 10), pady=10, sticky='w')

    radio2 = Radiobutton(accomodation_window,
                         text="Medium",
                         variable=price_range_var,
                         value="Medium",
                         command=on_radio_change)
    radio2.grid(row=4, columnspan=4, padx=10, pady=10)

    radio3 = Radiobutton(accomodation_window,
                         text="High",
                         variable=price_range_var,
                         value="High",
                         command=on_radio_change)
    radio3.grid(row=4, columnspan=4, padx=(10, 250), pady=10, sticky='ne')

    # Labels to display images
    image_labels = []
    name_labels = []
    url_labels = []
    for i in range(3):
        image_label = Label(image_frame)
        image_label.grid(row=0, column=i, padx=10, pady=5)
        image_labels.append(image_label)

        name_label = Label(image_frame)
        name_label.grid(row=1, column=i, padx=10, pady=5)
        name_labels.append(name_label)

        url_label = Label(image_frame, text="", fg="blue", cursor="hand2", wraplength=200)
        url_label.grid(row=2, column=i, padx=10, pady=5)
        url_labels.append(url_label)

    Show = Button(accomodation_window, text="Display", foreground='#f7f7f7', background='#D24545',
                  activeforeground='#D24545', activebackground='#A94438', font=font_button,
                  command=lambda: on_display_button_click(state_var, location_var, price_range_var,
                                                          image_labels,
                                                          name_labels, url_labels))

    Show.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Configure column sizes
    accomodation_window.grid_columnconfigure(0, weight=1, uniform="group1")
    accomodation_window.grid_columnconfigure(1, weight=1, uniform="group1")
    accomodation_window.grid_columnconfigure(2, weight=1, uniform="group1")

    accomodation_window.grid_rowconfigure(2, weight=0)
    accomodation_window.grid_rowconfigure(3, weight=0)
    accomodation_window.grid_rowconfigure(4, weight=0)
    accomodation_window.grid_rowconfigure(5, weight=0)
    accomodation_window.grid_rowconfigure(6, weight=0)
    accomodation_window.grid_rowconfigure(7, weight=0)


if __name__ == "__main__":
    window = Tk()
    create_accomodationwindow(window)
    window.mainloop()
