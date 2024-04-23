from tkinter import *
import tkinter as tk
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
from io import BytesIO


def fetch_image_data(destination, price_range):
    try:
        # Connect to the database
        connection = mysql.connector.connect(host='localhost',
                                             database='test',
                                             user='root',
                                             password='1927__sid')
        cursor = connection.cursor()

        # Fetch image data (paths and names) from the database based on destination and price range
        cursor.execute(
            "SELECT accomodation1, place1, accomodation2, place2, accomodation3, place3 FROM accomodation WHERE destination=%s AND pricerange=%s",
            (destination, price_range))
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


def display_images_and_names(image_labels, name_labels, image_data):
    for i in range(3):
        image_path = image_data[i * 2]  # Image path is at even indices
        name = image_data[i * 2 + 1]  # Image name is at odd indices

        # Resize image and display in label
        photo_image = resize_image(image_path, 200, 200)
        image_labels[i].config(image=photo_image)
        image_labels[i].photo = photo_image  # Keep a reference to the image

        # Display name in label
        name_labels[i].config(text=name)


def on_display_button_click(destination_entry, price_range_var, image_labels, name_labels):
    # Get destination and price range
    destination = destination_entry.get()
    price_range = price_range_var.get()

    # Fetch image data from database
    image_data = fetch_image_data(destination, price_range)

    if image_data:
        # Display images and names in labels
        display_images_and_names(image_labels, name_labels, image_data)
    else:
        print("No image data found for the given destination and price range.")


def create_accomodationwindow(parent):
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
    font_suggestions = ('Arial', 30, 'italic')
    font_nearbyinfo = ('Arial', 15, 'bold')
    font_button = ('Arial', 15, 'bold')
    font_option = ('Arial', 10, 'bold')
    font_view = ('Arial', 10, 'bold')

    # Setting up the "Suggestions" label
    accomodation_label = Label(accomodation_window,
                               text="ACCOMMODATION",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_suggestions)
    accomodation_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the label for "Here are some nearby places"
    enter_label = Label(accomodation_window,
                        text="Search for accommodations below",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_nearbyinfo)
    enter_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

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

    # Setting up the search bar
    # Setting up the text field for the age field
    destination_entry = Entry(accomodation_window,
                              width=50,
                              justify="left",
                              # anchor="w"
                              )
    destination_entry.grid(row=2, columnspan=4, padx=10, pady=10)

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
    for i in range(3):
        image_label = Label(image_frame)
        image_label.grid(row=0, column=i, padx=10, pady=5)
        image_labels.append(image_label)

        name_label = Label(image_frame)
        name_label.grid(row=1, column=i, padx=10, pady=5)
        name_labels.append(name_label)

    Show = Button(accomodation_window, text="Display", foreground='#f7f7f7', background='#D24545',
                  activeforeground='#D24545', activebackground='#A94438', font=font_button,
                  command=lambda: on_display_button_click(destination_entry, price_range_var, image_labels,
                                                          name_labels))

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
