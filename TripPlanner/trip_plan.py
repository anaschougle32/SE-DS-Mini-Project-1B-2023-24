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
            # image = image.resize((150, 150), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            image_labels[i].config(image=photo)
            image_labels[i].image = photo


def populate_treeview(itinerary):
    treeview.delete(*treeview.get_children())
    for day, activity in itinerary:
        treeview.insert('', 'end', values=(day, activity))


# Create Tkinter GUI
root = tk.Tk()
root.title("Travel Itinerary Planner")
root.configure(background="#111F4D")

window_width = 1000
window_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# List to store label widgets for images
image_labels = [tk.Label(root) for _ in range(3)]

# Positioning the labels
for i, label in enumerate(image_labels):
    label.place(x=800, y=100 + i * 185)  # Adjust the position as needed

state_label = tk.Label(root, text="Iternary", font=("italic", 34), fg='#f7f7f7',
                       bg='#111F4D')
state_label.place(x=400, y=10)

# State selection dropdown
state_label = tk.Label(root, text="Select State:", background="#ADD8E6", font=("Tahoma", 13))
state_label.place(x=50, y=80)
state_options = ["Maharashtra", "Delhi", "Goa", "Karnataka", "Uttarakhand"]
state_var = tk.StringVar(root)
state_dropdown = ttk.Combobox(root, textvariable=state_var, values=state_options, state='readonly', font=("Arial", 11))
state_dropdown.place(x=240, y=80)
# Number of days selection
days_label = tk.Label(root, text="Number of Days:", background="#ADD8E6", font=("Tahoma", 13))
days_label.place(x=50, y=120)
days_var = tk.StringVar(root, value="3")
days_radios = [tk.Radiobutton(root, text=str(i), variable=days_var, value=str(i)) for i in [3, 5, 8]]
for i, radio in enumerate(days_radios):
    radio.place(x=240 + i * 60, y=120)
# Destination display
destination_label = tk.Label(root, text="Suitable Destinations:", background="#ADD8E6", font=("Tahoma", 13))
destination_label.place(x=50, y=200)
destination_var = tk.StringVar(root)
destination_dropdown = tk.OptionMenu(root, destination_var, "No destinations found")
destination_dropdown.place(x=240, y=200)

# Update destinations button
update_button = tk.Button(root, text="Show Suitable Destinations", background="white", font=("Arial", 13),
                          command=update_destinations)
update_button.place(x=50, y=160)

# Show itinerary button
show_button = tk.Button(root, text="Show Itinerary", background="white", font=("Arial", 13),
                        command=lambda: [show_itinerary(), display_images()])
show_button.place(x=50, y=240)

# Itinerary Treeview
treeview = ttk.Treeview(root, columns=("Day", "Activity"), show="headings")

style = ttk.Style()
style.configure("Custom.Treeview.Heading", font=("Arial", 14),
                background="#ADD8E6")  # Adjust font, font size, background, and foreground color as needed

treeview.heading("Day", text="Day")
treeview.heading("Activity", text="Activity")
treeview.place(x=50, y=300, width=700, height=350)

# Define a custom style for the Treeview
style = ttk.Style()
style.configure("Custom.Treeview", rowheight=75, font=("Arial", 12),
                background="#ADD8E6")  # Adjust font, font size, background, and foreground color as needed

# Apply the custom style to the Treeview widget
treeview.config(style="Custom.Treeview")

treeview.column("Day", width=100)  # Set width of Day column to 100 pixels
treeview.column("Activity", width=400)  # Set width of Activity column to 300 pixels

# treeview.tag_configure('data', font=('Arial', 22), )  # Change font and size as needed


root.mainloop()
