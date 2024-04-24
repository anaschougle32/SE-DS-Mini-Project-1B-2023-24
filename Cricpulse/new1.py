import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import mysql.connector as mysql
from PIL import Image, ImageTk
import io
import subprocess
import matplotlib.pyplot as plt

def fetch_runs_by_over_ranges():
    try:
        # Establish connection to the database
        connection = mysql.connect(
            host="localhost",
            user="root",
            password="Parthavi@1204",
            database="cricpulse"
        )

        # Create cursor object to execute SQL queries
        cursor = connection.cursor()

        # SQL query to fetch runs scored in different over ranges
        query = "SELECT 01_05r, 06_10r, 11_15r, 16_20r, 21_25r FROM playerperformance"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows of the result
        result = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        connection.close()

        return result  # Return the fetched data

    except mysql.Error as error:
        print("Error fetching data from the database:", error)
        return None

def plot_runs_by_over_ranges():
    # Fetch data from the database
    data = fetch_runs_by_over_ranges()

    if data:
        # Extracting data for each over range
        data_01_05r = [row[0] for row in data]
        data_06_10r = [row[1] for row in data]
        data_11_15r = [row[2] for row in data]
        data_16_20r = [row[3] for row in data]
        data_21_25r = [row[4] for row in data]

        # Assuming x-axis labels for years
        years = ['2001-2005', '2006-2010', '2011-2015', '2016-2020', '2021-2025']

        # Plotting the line graph
        plt.plot(years, data_01_05r, label='01_05r')
        plt.plot(years, data_06_10r, label='06_10r')
        plt.plot(years, data_11_15r, label='11_15r')
        plt.plot(years, data_16_20r, label='16_20r')
        plt.plot(years, data_21_25r, label='21_25r')

        # Adding labels and title
        plt.xlabel('Years')
        plt.ylabel('Runs')
        plt.title('Runs scored in different over ranges')
        plt.legend()

        # Displaying the line graph
        plt.show()
    else:
        print("No data found.")

# Example usage:

selected_image_path = ""

def clear_main_frame():
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()
def indicate(lb):
    lb.config(bg="white")
def add_image_page():
    clear_main_frame()
    add_image_page_frame = tk.Frame(main_frame)
    add_image_page_frame.pack(fill=tk.BOTH, expand=True)
    image_label = tk.Label(add_image_page_frame, width=100, height=10, bg="white", bd=2, relief="solid")
    image_label.place(relx=0.04, rely=0.05)
    insert_image_button = tk.Button(add_image_page_frame, text="Insert Image", command=insert_image)
    insert_image_button.pack()

def insert_image():
    file_path = filedialog.askopenfilename()  # Open a file dialog to select an image
    if file_path:  # If a file is selected
        try:
            db = mysql.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse",auth_plugin='mysql_native_password')
            c = db.cursor()

            with open(file_path, 'rb') as file:
                image_data = file.read()
            insert_query = "INSERT INTO imageslider (image) VALUES (%s)"
            c.execute(insert_query, (image_data,))
            db.commit()
            print("Image inserted successfully!")

            # Fetch all images again from the database
            image_paths = fetch_images_from_database()

            # Update the image slider with the new list of images
            update_image_slider(image_paths, 0)

        except Exception as e:
            print("Error:", e)
        finally:
            # Close cursor and database connection
            if c:
                c.close()
            if db:
                db.close()





def t20_page():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    t20_page_frame = tk.Frame(main_frame)
    t20_page_frame.pack(fill=tk.BOTH, expand=True)
    t20_label = tk.Label(t20_page_frame,width=25, height=14, bg="white", bd=2, relief="solid")
    t20_label.place(relx=0.04,rely=0.05)
    label_2_image = tk.PhotoImage(file="t20f1.png")
    image_label2 = tk.Label(t20_label, image=label_2_image, bd=0)
    image_label2.image = label_2_image
    image_label2.pack(anchor="center")
    t20_label = tk.Label(t20_page_frame, width=15, height=2,text="T20I Ranking", bg="white")
    t20_label.place(relx=0.4, rely=0.43)
    t20_info = tk.Text(t20_page_frame, wrap="word", height=14, width=65)
    t20_info.insert("1.0",
                    "T20 International cricket, commonly referred to as T20I, is the shortest format of international cricket matches. Each team plays a single innings, which is restricted to a maximum number of overs, usually 20 overs per side. T20 cricket is known for its fast-paced and exciting gameplay, often featuring big hitting and aggressive bowling tactics.")
    t20_info.config(state="disabled")
    t20_info.place(relx=0.3, rely=0.05)
    tree1 = ttk.Treeview(t20_page_frame, columns=("Ranking", "Teams", "Matches", "Points"), show="headings")
    tree1.heading("Ranking", text="Ranking")
    tree1.heading("Teams", text="Teams")
    tree1.heading("Matches", text="Matches")
    tree1.heading("Points", text="Points")
    tree1.place(x=3, y=300, width=760, height=310)


    # Populate the table
    populate_table2(tree1)

def populate_table2(tree1):
    # Insert data into the table
    data = [
        (1, "India", 71, 18867),
        (2, "England", 48, 12305),
        (3, "Australia", 45, 11460)
    ]
    for row in data:
        tree1.insert("", "end", values=row)

def odi_page():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    odi_page_frame = tk.Frame(main_frame)
    odi_page_frame.pack(fill=tk.BOTH, expand=True)
    odi_label = tk.Label(odi_page_frame,width=25, height=14, bg="white", bd=2, relief="solid")
    odi_label.place(relx=0.04,rely=0.05)
    label_2_imageo = tk.PhotoImage(file="download.png")
    image_label2o = tk.Label(odi_label, image=label_2_imageo, bd=0)
    image_label2o.image = label_2_imageo
    image_label2o.pack(anchor="center")
    odi_label = tk.Label(odi_page_frame, width=15, height=2,text="ODI Ranking", bg="white")
    odi_label.place(relx=0.4, rely=0.43)
    odi_info = tk.Text(odi_page_frame, wrap="word", height=14, width=65)
    odi_info.insert("1.0",
                    "One Day International (ODI) cricket is a format of limited-overs cricket where each team gets to bat and bowl for a maximum of 50 overs each. An ODI match typically spans a single day, hence the name One Day. It is one of the three recognized forms of international cricket, alongside Test and Twenty20 International (T20I) cricket.")
    odi_info.config(state="disabled")
    odi_info.place(relx=0.3, rely=0.05)
    treeO = ttk.Treeview(odi_page_frame, columns=("Ranking", "Teams", "Matches", "Points"), show="headings")
    treeO.heading("Ranking", text="Ranking")
    treeO.heading("Teams", text="Teams")
    treeO.heading("Matches", text="Matches")
    treeO.heading("Points", text="Points")
    treeO.place(x=3, y=300, width=760, height=310)


    # Populate the table
    populate_tableO(treeO)

def populate_tableO(treeO):
    # Insert data into the table
    data = [
        (1, "India", 58,7020),
        (2, "AUSTRALIA",45,5309),
        (3, "SOUTH AFRICA",37,4062)
    ]
    for row in data:
        treeO.insert("", "end", values=row)

def test_page():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    test_page_frame = tk.Frame(main_frame)
    test_page_frame.pack(fill=tk.BOTH, expand=True)
    test_label = tk.Label(test_page_frame,width=25, height=14, bg="white", bd=2, relief="solid")
    test_label.place(relx=0.04,rely=0.05)
    label_2_imaget = tk.PhotoImage(file="test.png")
    image_label2t = tk.Label(test_label, image=label_2_imaget, bd=0)
    image_label2t.image = label_2_imaget
    image_label2t.pack(anchor="center")
    odi_label = tk.Label(test_page_frame, width=15, height=2,text="TEST Ranking", bg="white")
    odi_label.place(relx=0.4, rely=0.43)
    odi_info = tk.Text(test_page_frame, wrap="word", height=14, width=65)
    odi_info.insert("1.0",
                    "Test cricket is the longest format of the sport and is considered the pinnacle of cricketing excellence. Matches can last up to five days, with each team batting and bowling twice, provided enough time remains after completing the first innings. Test matches are played over a maximum of 90 overs per day.")
    odi_info.config(state="disabled")
    odi_info.place(relx=0.3, rely=0.05)
    treet = ttk.Treeview(test_page_frame, columns=("Ranking", "Teams", "Matches", "Points"), show="headings")
    treet.heading("Ranking", text="Ranking")
    treet.heading("Teams", text="Teams")
    treet.heading("Matches", text="Matches")
    treet.heading("Points", text="Points")
    treet.place(x=3, y=300, width=760, height=310)


    # Populate the table
    populate_tablet(treet)

def populate_tablet(treet):
    # Insert data into the table
    data = [
        (1, "AUSTRALIA", 37, 4345),
        (2, "INDIA", 32, 3746),
        (3, "ENGLAND", 43, 4941)
    ]
    for row in data:
        treet.insert("", "end", values=row)



def hide_indicate():
    home_indicate.config(bg="blue")
    player_performance_indicate.config(bg="blue")
    player_comparison_indicate.config(bg="blue")
    field_determination_indicate.config(bg="blue")


def indicate_home():
    hide_indicate()
    home_page()
    home_indicate.config(bg="white")
    player_performance_indicate.config(bg="blue")
    player_comparison_indicate.config(bg="blue")
    field_determination_indicate.config(bg="blue")

def indicate_player_performance():
    hide_indicate()
    player_performance_page()
    home_indicate.config(bg="blue")
    player_performance_indicate.config(bg="white")
    player_comparison_indicate.config(bg="blue")
    field_determination_indicate.config(bg="blue")

def indicate_player_comparison():
    hide_indicate()
    player_comparison_page()
    home_indicate.config(bg="blue")
    player_performance_indicate.config(bg="blue")
    player_comparison_indicate.config(bg="white")
    field_determination_indicate.config(bg="blue")

def indicate_field_determination():
    hide_indicate()
    field_determination_page()
    home_indicate.config(bg="blue")
    player_performance_indicate.config(bg="blue")
    player_comparison_indicate.config(bg="blue")
    field_determination_indicate.config(bg="white")
def fetch_images_from_database():
    try:
        db = mysql.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse",
                         auth_plugin='mysql_native_password')
        c = db.cursor()

        c.execute('SELECT image FROM imageslider')
        images = c.fetchall()
        db.close()
        return images
    except mysql.Error as err:
        print("Error:", err)

# Function to update the image slider


def update_image_slider(image_list, current_index):
    if not image_list:
        return
    image_data = image_list[current_index][0]
    image = Image.open(io.BytesIO(image_data))
    resized_image = image.resize((450, 130)) # Adjust the size as needed
    photo = ImageTk.PhotoImage(resized_image)
    image_label.configure(image=photo)
    image_label.image = photo
    # Update index for the next image
    current_index = (current_index + 1) % len(image_list)
    # Call the function again after a certain delay (e.g., 3 seconds)
    root.after(3000, update_image_slider, image_list, current_index)

# Function to navigate to the home page
def home_page():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for home page content
    home_frame = tk.Frame(main_frame,bg="white")
    home_frame.pack(fill=tk.BOTH, expand=True)

    # Create a blue rectangle
    blue_rectangle = tk.Canvas(home_frame, width=760, height=66, bg="blue")
    blue_rectangle.place(x=2, y=0)

    # Create label frame
    label_frame = tk.Frame(home_frame, width=463, height=146, bg="white", bd=2, relief="solid")
    label_frame.place(relx=0.5, rely=0.31, anchor="center")
    # Fetch images from the database
    image_paths = fetch_images_from_database()

    # Create a label for the image slider
    global image_label
    image_label = tk.Label(label_frame, bg="white")
    image_label.pack()
    # Start the image slider
    update_image_slider(image_paths, 0)
    addimage_button = tk.Button(home_frame, text="Add Image", width=20, command=add_image_page)
    addimage_button.place(relx=0.6, rely=0.15)


    # Create additional labels frame
    additional_labels_frame = tk.Frame(home_frame, bg="white")
    additional_labels_frame.place(relx=0.5, rely=0.70, anchor="center")
    # Create label 2 with image
    label_2 = tk.Frame(additional_labels_frame, width=136, height=174, bg="white", bd=2, relief="solid")
    label_2.grid(row=0, column=0, padx=(0, 20))
    label_2_image = tk.PhotoImage(file="t20f1.png")
    image_label2 = tk.Label(label_2, image=label_2_image, bd=0)
    image_label2.image = label_2_image
    image_label2.pack(anchor="center")

    # Create label 3 with image
    label_3 = tk.Frame(additional_labels_frame, width=136, height=174, bg="white", bd=2, relief="solid")
    label_3.grid(row=0, column=1, padx=(20, 20))
    label_3_image = tk.PhotoImage(file="download.png")
    image_label3 = tk.Label(label_3, image=label_3_image, bd=0)
    image_label3.image = label_3_image
    image_label3.pack(anchor="center")

    # Create label 4 with image
    label_4 = tk.Frame(additional_labels_frame, width=136, height=174, bg="white", bd=2, relief="solid")
    label_4.grid(row=0, column=2, padx=(20, 0))
    label_4_image = tk.PhotoImage(file="test.png")
    image_label4 = tk.Label(label_4, image=label_4_image, bd=0)
    image_label4.image = label_4_image
    image_label4.pack(anchor="center")

    t20_button = tk.Button(home_frame,text="T20",width=20,command=t20_page)
    t20_button.place(relx=0.168,rely=0.85)
    odi_button = tk.Button(home_frame, text="ODI", width=20, command=odi_page)
    odi_button.place(relx=0.4, rely=0.85)
    test_button = tk.Button(home_frame, text="Test", width=20, command=test_page)
    test_button.place(relx=0.635, rely=0.85)

def player_performance_page():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    player_performance_frame = tk.Frame(main_frame)
    player_performance_frame.pack(fill=tk.BOTH, expand=True)

    # Create a blue rectangle
    blue_rectangle = tk.Canvas(player_performance_frame, width=760, height=140, bg="blue")
    blue_rectangle.place(x=2, y=0)

    # Calculate the x-coordinate for the button to be at the right side of the rectangle
    button_x = blue_rectangle.winfo_x() + blue_rectangle.winfo_width() - 10

    # Create button inside the blue rectangle
    add_player_button = tk.Button(blue_rectangle, text="Add Player", command=open_playerperformanceadd_py)
    add_player_button.place(relx=0.88, rely=0.5, anchor="center")
    # Calculate the center coordinates of the blue rectangle
    center_x = 150 + 690 / 2
    center_y = 0 + 66 / 2

    # Create text field
    text_field = tk.Entry(player_performance_frame, width=30)
    text_field.place(x=center_x - 170, y=center_y - 0, anchor="center")

    # Create search button
    search_button = tk.Button(player_performance_frame, text="Search", command=plot_runs_by_over_ranges)
    search_button.place(x=center_x - 45, y=center_y - 0, anchor="center")

    # Create label frame 1
    label_frame1 = tk.LabelFrame(player_performance_frame, text="Label Frame 1", width=136, height=174)
    label_frame1.place(x=10, y=200)

    # Create label frame 2
    label_frame2 = tk.LabelFrame(player_performance_frame, text="Label Frame 2", width=136, height=174)
    label_frame2.place(x=156, y=200)

    # Create label frame 3
    label_frame3 = tk.LabelFrame(player_performance_frame, text="Label Frame 3", width=136, height=174)
    label_frame3.place(x=302, y=200)

    # Call the function to populate the table


def player_comparison_page():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player comparison page content
    player_comparison_frame = tk.Frame(main_frame)
    player_comparison_frame.pack(fill=tk.BOTH, expand=True)

    # Create text field 1
    text_field1 = tk.Entry(player_comparison_frame, width=35)
    text_field1.place(relx=0.3, rely=0.1, anchor="center")

    # Create text field 2
    text_field2 = tk.Entry(player_comparison_frame, width=35)
    text_field2.place(relx=0.7, rely=0.1, anchor="center")

    # Create label 1 with black border
    label1_frame = tk.Frame(player_comparison_frame, width=120, height=149, bd=2, relief="solid", bg="white")
    label1_frame.place(relx=0.3, rely=0.3, anchor="center")

    # Create label 2 with black border
    label2_frame = tk.Frame(player_comparison_frame, width=123, height=155, bd=2, relief="solid", bg="white")
    label2_frame.place(relx=0.7, rely=0.3, anchor="center")

    # Create button inside the blue rectangle
    compare_button = tk.Button(player_comparison_frame, text="Compare")
    compare_button.place(relx=0.5, rely=0.32, anchor="center")
 # Create labels for statistics
    stats_labels = [
        "Matches",
        "Runs",
        "Strike Rate",
        "100s/50s",
        "Best Score"
    ]

    # Place labels vertically at the bottom left
    for i, text in enumerate(stats_labels):
        label = tk.Label(player_comparison_frame, text=text)
        label.place(relx=0.02, rely=0.7 + i * 0.05, anchor="w")


def fields():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    fields_frame = tk.Frame(main_frame)
    fields_frame.pack(fill=tk.BOTH, expand=True)

def field_determination_page():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    field_determination_frame = tk.Frame(main_frame)
    field_determination_frame.pack(fill=tk.BOTH, expand=True)

    # Create a blue rectangle
    blue_rectangle = tk.Canvas(field_determination_frame, width=760, height=66, bg="blue")
    blue_rectangle.place(x=2, y=0)

    # Calculate the x-coordinate for the button to be at the right side of the rectangle
    button_x = blue_rectangle.winfo_x() + blue_rectangle.winfo_width() - 10

    # Create button inside the blue rectangle
    add_field_button = tk.Button(blue_rectangle, text="Add Field",command=open_second_py)
    add_field_button.place(relx=0.88, rely=0.5, anchor="center")
    # Calculate the center coordinates of the blue rectangle
    center_x = 150 + 690 / 2
    center_y = 0 + 66 / 2

    # Create text field
    text_field = tk.Entry(field_determination_frame, width=30)
    text_field.place(x=center_x - 170, y=center_y - 0, anchor="center")

    # Create search button
    search_button = tk.Button(field_determination_frame, text="Search")
    search_button.place(x=center_x - 45, y=center_y - 0, anchor="center")

    # Create treeview widget for the table
    tree = ttk.Treeview(field_determination_frame, columns=("Fields", "Blowing style"), show="headings")
    tree.heading("Fields", text="Fields")
    tree.heading("Blowing style", text="Blowing style")

    tree.place(x=3, y=70, width=760, height=610)

    # Populate the table
    populate_table1(tree)

def populate_table1(tree):
    # Insert data into the table
    data = [
        (1, "Arm ball"),
        (2, "Off Spin"),
        (3, "Leg spin")
    ]
    for row in data:
        tree.insert("", "end", values=row)
        # Bind a function to handle treeview item selection
        tree.bind("<ButtonRelease-1>", on_tree_select)

def on_tree_select(event):
        # Call the fields() function when any row is clicked
        fields()
def open_second_py():
    subprocess.call(["python", "second.py"])

def open_playerperformanceadd_py():
    subprocess.call(["python", "playerperformanceadd.py"])

root = tk.Tk()
root.title("Project Window")
root.geometry("935x610")
root.configure(bg="white")
root.geometry("+100+100")

options_frame = tk.Frame(root, width=252, height=490, bg="blue")
options_frame.pack(side="left", fill="y")

buttons = [
    ("Home", indicate_home),
    ("Player Performance", indicate_player_performance),
    ("Player Comparison", indicate_player_comparison),
    ("Field Determination", indicate_field_determination)
]

for i, (text, command) in enumerate(buttons):
    btn = tk.Button(options_frame, text=text, width=20, command=command)
    btn.grid(row=i, column=0, pady=25, padx=10)

home_indicate = tk.Label(options_frame,text='',bg="white")
home_indicate.place(x=3,y=22,width=5,height=32)

player_performance_indicate = tk.Label(options_frame,text='',bg="blue")
player_performance_indicate.place(x=3,y=98,width=5,height=32)

player_comparison_indicate = tk.Label(options_frame,text='',bg="blue")
player_comparison_indicate.place(x=3,y=174,width=5,height=32)

field_determination_indicate = tk.Label(options_frame,text='',bg="blue")
field_determination_indicate.place(x=3,y=250,width=5,height=32)

main_frame = tk.Frame(root, bg='white',highlightbackground='black', highlightthickness=2)  # Set main frame size
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
main_frame.pack_propagate(False)
main_frame.configure(height=490, width=583)

home_page()

root.mainloop()

