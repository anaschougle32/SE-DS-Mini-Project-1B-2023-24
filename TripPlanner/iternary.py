import textwrap
from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk


def fetch_destinations(state, num_days):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        database='test',
        user='root',
        password='1927__sid'
    )
    cursor = conn.cursor()

    # Execute query to fetch destinations based on state and number of days
    query = "SELECT destination_name FROM destination WHERE state = %s AND num_days = %s"
    cursor.execute(query, (state, num_days))

    destinations = [row[0] for row in cursor.fetchall()]

    # Close cursor and connection
    cursor.close()
    conn.close()

    return destinations


def fetch_itinerary(destination):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        database='test',
        user='root',
        password='1927__sid'
    )
    cursor = conn.cursor()

    # Execute query to fetch itinerary for selected destination
    query = "SELECT day, activity FROM iternary WHERE location = %s ORDER BY day"
    cursor.execute(query, (destination,))

    itinerary = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    conn.close()

    return itinerary


def update_destinations():
    selected_state = state_var.get()
    selected_days = int(days_var.get())

    destinations = fetch_destinations(selected_state, selected_days)
    destination_var.set(destinations[0] if destinations else "No destinations found")
    destination_dropdown['menu'].delete(0, 'end')
    for dest in destinations:
        destination_dropdown['menu'].add_command(label=dest, command=tk._setit(destination_var, dest))


def show_itinerary():
    selected_destination = destination_var.get()
    itinerary = fetch_itinerary(selected_destination)
    populate_treeview(itinerary)


def fetch_image_paths(selected_destination):
    conn = mysql.connector.connect(
        host='localhost',
        database='test',
        user='root',
        password='1927__sid'
    )
    cursor = conn.cursor()

    # Execute query to fetch image paths for selected destination
    query = "SELECT image_path FROM destination_images WHERE destination_id = (SELECT destination_id FROM destination WHERE destination_name = %s)"
    cursor.execute(query, (selected_destination,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return [result[0] for result in results] if results else []


def display_images():
    selected_destination = destination_var.get()
    image_paths = fetch_image_paths(selected_destination)

    # Clear previous images
    for label in image_labels:
        label.config(image=None)

    # Display new images
    for i, path in enumerate(image_paths):
        if i < 3:  # Display maximum of 3 images
            image = Image.open(path)
            photo = ImageTk.PhotoImage(image)

            image_labels[i].config(image=photo)
            image_labels[i].image = photo


def populate_treeview(itinerary):
    treeview.delete(*treeview.get_children())
    for day, activity in itinerary:
        # Wrap the text if it exceeds a certain length
        wrapped_activity = "\n".join(textwrap.wrap(activity, width=70))  # Adjust the width as needed
        treeview.insert('', 'end', values=(day, wrapped_activity))



def create_finaliternarywindow(parent):
    global state_var, days_var, destination_var, destination_dropdown, image_labels, treeview
    # Setting up the window
    iternary_window = Toplevel(parent)
    iternary_window.title("Your Itinerary")
    iternary_window.configure(background="#111F4D")
    iternary_window.resizable(False, False)

    # Positioning the application
    window_width = 1000
    window_height = 630
    screen_width = iternary_window.winfo_screenwidth()
    screen_height = iternary_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    iternary_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # List to store label widgets for images
    image_labels = [tk.Label(iternary_window) for _ in range(3)]

    # Positioning the labels
    for i, label in enumerate(image_labels):
        label.place(x=800, y=100 + i * 185)  # Adjust the position as needed

    state_label = tk.Label(iternary_window, text="Itinerary", font=("italic", 34), fg='#f7f7f7',
                           bg='#111F4D')
    state_label.place(x=400, y=10)

    # State selection dropdown
    state_label = tk.Label(iternary_window, text="Select State:", background="#ADD8E6", font=("Tahoma", 13))
    state_label.place(x=50, y=80)
    state_options = ["Maharashtra", "Delhi", "Goa", "Karnataka", "Uttarakhand"]
    state_var = tk.StringVar(iternary_window)
    state_dropdown = ttk.Combobox(iternary_window, textvariable=state_var, values=state_options, state='readonly',
                                  font=("Arial", 11))
    state_dropdown.place(x=240, y=80)

    # Number of days selection
    days_label = tk.Label(iternary_window, text="Number of Days:", background="#ADD8E6", font=("Tahoma", 13))
    days_label.place(x=50, y=120)
    days_var = tk.StringVar(iternary_window, value="3")
    days_radios = [tk.Radiobutton(iternary_window, text=str(i), variable=days_var, value=str(i)) for i in [3, 5, 8]]
    for i, radio in enumerate(days_radios):
        radio.place(x=240 + i * 60, y=120)

    # Destination display
    destination_label = tk.Label(iternary_window, text="Suitable Destinations:", background="#ADD8E6", font=("Tahoma", 13))
    destination_label.place(x=50, y=200)
    destination_var = tk.StringVar(iternary_window)
    destination_dropdown = tk.OptionMenu(iternary_window, destination_var, "No destinations found")
    destination_dropdown.place(x=240, y=200)

    # Update destinations button
    update_button = tk.Button(iternary_window, text="Show Suitable Destinations", background="white",
                              font=("Arial", 13),
                              command=update_destinations)
    update_button.place(x=50, y=160)

    # Show itinerary button
    show_button = tk.Button(iternary_window, text="Show Itinerary", background="white", font=("Arial", 13),
                            command=lambda: [show_itinerary(), display_images()])
    show_button.place(x=50, y=240)

    # Itinerary Treeview
    treeview_frame = Frame(iternary_window)
    treeview_frame.place(x=50, y=300, width=700, height=350)

    treeview = ttk.Treeview(treeview_frame, columns=("Day", "Activity"), show="headings")

    style = ttk.Style()
    style.configure("Custom.Treeview.Heading", font=("Arial", 14),
                    background="#ADD8E6")  # Adjust font, font size, background, and foreground color as needed

    treeview.heading("Day", text="Day")
    treeview.heading("Activity", text="Activity")

    # Define a custom style for the Treeview
    style = ttk.Style()
    style.configure("Custom.Treeview", rowheight=75, font=("Arial", 12),
                    background="#ADD8E6")  # Adjust font, font size, background, and foreground color as needed

    # Apply the custom style to the Treeview widget
    treeview.config(style="Custom.Treeview")

    treeview.column("Day", width=100)  # Set width of Day column to 100 pixels
    treeview.column("Activity", width=400)  # Set width of Activity column to 400 pixels

    scrollbar_y = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
    scrollbar_y.pack(side="right", fill="y")
    treeview.config(yscrollcommand=scrollbar_y.set)

    scrollbar_x = ttk.Scrollbar(treeview_frame, orient="horizontal", command=treeview.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    treeview.config(xscrollcommand=scrollbar_x.set)

    treeview.pack(side="left", fill="both", expand=True)

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(iternary_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(iternary_window, parent),
                  font=("Arial", 12, 'bold'))
    Back.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    # Configure column sizes
    iternary_window.grid_columnconfigure(0, weight=1, uniform="group1")
    iternary_window.grid_columnconfigure(1, weight=0, uniform="group1")
    iternary_window.grid_columnconfigure(2, weight=0, uniform="group1")

    iternary_window.grid_rowconfigure(2, weight=0)
    iternary_window.grid_rowconfigure(3, weight=0)
    iternary_window.grid_rowconfigure(4, weight=0)
    iternary_window.grid_rowconfigure(5, weight=0)
    iternary_window.grid_rowconfigure(6, weight=0)
    iternary_window.grid_rowconfigure(7, weight=0)
    iternary_window.grid_rowconfigure(8, weight=0)
    iternary_window.grid_rowconfigure(9, weight=0)
    iternary_window.grid_rowconfigure(10, weight=0)
    iternary_window.grid_rowconfigure(11, weight=0)

if __name__ == "__main__":
    window = Tk()
    create_finaliternarywindow(window)
    window.mainloop()
