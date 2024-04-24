import io
import tkinter as tk
from tkinter import ttk, END, filedialog
import subprocess
import mysql.connector
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

global image_label1

root = tk.Tk()
root.title("Project Window")
root.geometry("935x610")
root.configure(bg="white")
root.geometry("+100+100")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Parthavi@1204",
    database="cricpulse",
    auth_plugin='mysql_native_password'
)
cursor = db.cursor()

def delete_last_image():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse", auth_plugin='mysql_native_password')
        c = db.cursor()

        # Fetch the ID of the last inserted image
        c.execute('SELECT MAX(id) FROM imageslider')
        image_id = c.fetchone()[0]

        # Delete the last inserted image from the database
        delete_query = "DELETE FROM imageslider WHERE id = %s"
        c.execute(delete_query, (image_id,))
        db.commit()
        print("Last inserted image deleted successfully!")

        # Fetch all images again from the database
        image_paths = fetch_images_from_database()

        # Update the image slider with the new list of images
        update_image_slider(image_paths, 0)

        # Show a message box to notify the user
        messagebox.showinfo("Success", "Last image deleted successfully!")

    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "Failed to delete last image!")
    finally:
        if c:
            c.close()
        if db:
            db.close()

def delete_all_images():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse", auth_plugin='mysql_native_password')
        c = db.cursor()

        # Delete all images from the database
        delete_query = "DELETE FROM imageslider"
        c.execute(delete_query)
        db.commit()
        print("All images deleted successfully!")

        # Clear the image slider
        image_label.configure(image=None)

        # Show a message box to notify the user
        messagebox.showinfo("Success", "All images deleted successfully!")

    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "Failed to delete all images!")
    finally:
        if c:
            c.close()
        if db:
            db.close()

def add_image_page():
    global image_label1
    clear_main_frame()
    add_image_page_frame = tk.Frame(main_frame)
    add_image_page_frame.pack(fill=tk.BOTH, expand=True)
    image_label1 = tk.Frame(add_image_page_frame, width=700, height=156, bg="white", bd=2, relief="solid")
    image_label1.place(relx=0.04, rely=0.05)
    insert_image_button = tk.Button(add_image_page_frame, text="Insert Image", command=insert_image)
    insert_image_button.place(relx=0.1,rely=0.5)
    delete_last_image_button = tk.Button(add_image_page_frame, text="Delete Last Image", command=delete_last_image)
    delete_last_image_button.place(relx=0.3,rely=0.5)
    delete_all_images_button = tk.Button(add_image_page_frame, text="Delete All Images", command=delete_all_images)
    delete_all_images_button.place(relx=0.5,rely=0.5)

def insert_image():
    file_path = filedialog.askopenfilename()  # Open a file dialog to select an image
    if file_path:
        # If a file is selected
        image = Image.open(file_path)
        image = image.resize((700, 156))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)

        # Create a label and display the image
        image_label = tk.Label(image_label1, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack()
    try:
            db = mysql.connector.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse",auth_plugin='mysql_native_password')
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
        if c:
            c.close()
        if db:
            db.close()
def fetch_images_from_database():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse",
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
def update_datatest():
    try:
        teams=team_entryt.get()
        ranking=int(ranking_entryt.get())
        matches=int(matches_entryt.get())
        points=float(points_entryt.get())
        query = "update test set ranking=%s,matches=%s,points=%s where teams=%s"
        values=(ranking,matches,points,teams)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_dataodi():
    try:
        teams=teams_entryo.get()
        ranking=int(ranking_entryo.get())
        matches=int(matches_entryo.get())
        points=float(points_entryo.get())
        query = "update odi set ranking=%s,matches=%s,points=%s where teams=%s"
        values=(ranking,matches,points,teams)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_datat20():
    try:
        teams=team_entrytt.get()
        ranking=int(ranking_entrytt.get())
        matches=int(matches_entrytt.get())
        points=float(points_entrytt.get())
        query = "update twenty set ranking=%s,matches=%s,points=%s where teams=%s"
        values=(ranking,matches,points,teams)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_data_test():
    # Get the name from the name text field
    team = team_entryt.get()

    # Query to fetch data from the database based on the name
    query = "SELECT * FROM test WHERE Teams = %s"
    cursor.execute(query, (team,))
    result = cursor.fetchall()

    # Check if any data is found
    if result:
        # Since there may be multiple rows, we'll only display the data from the first row
        row_data = result[0]

        # Populate the text fields with the fetched data
        team_entryt.delete(0, tk.END)
        team_entryt.insert(tk.END, row_data[0])  # Name

        ranking_entryt.delete(0, tk.END)
        ranking_entryt.insert(tk.END, row_data[1])  # Rank

        matches_entryt.delete(0, tk.END)
        matches_entryt.insert(tk.END, row_data[2])  # DOB

        points_entryt.delete(0, tk.END)
        points_entryt.insert(tk.END, row_data[3])
    else:
        # If no data is found, show a message
        messagebox.showinfo("Error", "No data found for the entered name")

def fetch_data_odi():
    # Get the name from the name text field
    team = teams_entryo.get()

    # Query to fetch data from the database based on the name
    query = "SELECT * FROM odi WHERE Teams = %s"
    cursor.execute(query, (team,))
    result = cursor.fetchall()

    # Check if any data is found
    if result:
        # Since there may be multiple rows, we'll only display the data from the first row
        row_data = result[0]

        # Populate the text fields with the fetched data
        teams_entryo.delete(0, tk.END)
        teams_entryo.insert(tk.END, row_data[0])  # Name

        ranking_entryo.delete(0, tk.END)
        ranking_entryo.insert(tk.END, row_data[1])  # Rank

        matches_entryo.delete(0, tk.END)
        matches_entryo.insert(tk.END, row_data[2])  # DOB

        points_entryo.delete(0, tk.END)
        points_entryo.insert(tk.END, row_data[3])
    else:
        # If no data is found, show a message
        messagebox.showinfo("Error", "No data found for the entered name")
def fetch_data_t20():
    # Get the name from the name text field
    team = team_entrytt.get()

    # Query to fetch data from the database based on the name
    query = "SELECT * FROM twenty WHERE Teams = %s"
    cursor.execute(query, (team,))
    result = cursor.fetchall()

    # Check if any data is found
    if result:
        # Since there may be multiple rows, we'll only display the data from the first row
        row_data = result[0]

        # Populate the text fields with the fetched data
        team_entrytt.delete(0, tk.END)
        team_entrytt.insert(tk.END, row_data[0])  # Name

        ranking_entrytt.delete(0, tk.END)
        ranking_entrytt.insert(tk.END, row_data[1])  # Rank

        matches_entrytt.delete(0, tk.END)
        matches_entrytt.insert(tk.END, row_data[2])  # DOB

        points_entrytt.delete(0, tk.END)
        points_entrytt.insert(tk.END, row_data[3])
    else:
        # If no data is found, show a message
        messagebox.showinfo("Error", "No data found for the entered name")
def delete_datatest():
    try:
        team = team_entryt.get()

        # Delete data from the table
        query = "DELETE FROM test WHERE Teams = %s"
        cursor.execute(query, (team,))
        db.commit()

        messagebox.showinfo("Success", "Data deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def delete_dataodi():
    try:
        team = teams_entryo.get()

        # Delete data from the table
        query = "DELETE FROM odi WHERE Teams = %s"
        cursor.execute(query, (team,))
        db.commit()

        messagebox.showinfo("Success", "Data deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def delete_datat20():
    try:
        team = team_entrytt.get()

        # Delete data from the table
        query = "DELETE FROM twenty WHERE Teams = %s"
        cursor.execute(query, (team,))
        db.commit()

        messagebox.showinfo("Success", "Data deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def fetch_runs_by_over_ranges():
    try:

        # Create cursor object to execute SQL queries


        # SQL query to fetch runs scored in different over ranges
        query = "SELECT 01_05r, 06_10r, 11_15r, 16_20r, 21_25r FROM playerperformance WHERE Name = %s"

        # Execute the query
        cursor.execute(query, ('gdkd',))

        # Fetch all rows of the result
        result = cursor.fetchall()

        # Close cursor and connection
        cursor.close()


        return result  # Return the fetched data

    except mysql.connector.Error as error:
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


def clear_main_frame():
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()
def indicate(lb):
    lb.config(bg="white")
def insert_dataODI():
    try:
        teams=teams_entryo.get()
        ranking=int(ranking_entryo.get())
        matches=int(matches_entryo.get())
        points=float(points_entryo.get())
        query = "insert into odi(Teams,Ranking,Matches,Points)VALUES(%s,%s,%s,%s)"
        values=(teams,ranking,matches,points)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def insert_datatest():
    try:
        teams=team_entryt.get()
        ranking=int(ranking_entryt.get())
        matches=int(matches_entryt.get())
        points=float(points_entryt.get())
        query = "insert into test(Teams,Ranking,Matches,Points)VALUES(%s,%s,%s,%s)"
        values=(teams,ranking,matches,points)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def insert_datat20():
    try:
        teams=team_entrytt.get()
        ranking=int(ranking_entrytt.get())
        matches=int(matches_entrytt.get())
        points=float(points_entrytt.get())
        query = "insert into twenty(Teams,Ranking,Matches,Points)VALUES(%s,%s,%s,%s)"
        values=(teams,ranking,matches,points)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def test_page_admin():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    test_page_admin_frame = tk.Frame(main_frame)
    test_page_admin_frame.pack(fill=tk.BOTH, expand=True)

    # Label and TextField for search

    # Labels and TextFields for teams, ranking, matches, and points
    teams_label = tk.Label(test_page_admin_frame, text="Teams:", font="times 12 bold")
    teams_label.place(relx=0.04, rely=0.2)

    ranking_label = tk.Label(test_page_admin_frame, text="Ranking:", font="times 12 bold")
    ranking_label.place(relx=0.04, rely=0.35)

    matches_label = tk.Label(test_page_admin_frame, text="Matches:", font="times 12 bold")
    matches_label.place(relx=0.5, rely=0.2)

    points_label = tk.Label(test_page_admin_frame, text="Points:", font="times 12 bold")
    points_label.place(relx=0.5, rely=0.35)

    global team_entryt  # Corrected variable name
    global ranking_entryt  # Corrected variable name
    global matches_entryt  # Corrected variable name
    global points_entryt  # Corrected variable name

    team_entryt = tk.Entry(test_page_admin_frame, font="times 12 bold")
    team_entryt.place(relx=0.15, rely=0.2)

    ranking_entryt = tk.Entry(test_page_admin_frame, font="times 12 bold")
    ranking_entryt.place(relx=0.15, rely=0.35)

    matches_entryt = tk.Entry(test_page_admin_frame, font="times 12 bold")
    matches_entryt.place(relx=0.6, rely=0.2)

    points_entryt = tk.Entry(test_page_admin_frame, font="times 12 bold")
    points_entryt.place(relx=0.6, rely=0.35)

    add_button = tk.Button(test_page_admin_frame, text="Add", font="times 12 bold", bg="white", command=insert_datatest)
    add_button.place(relx=0.1, rely=0.6)

    update_button = tk.Button(test_page_admin_frame, text="Update", font="times 12 bold", bg="white",command=update_datatest)
    update_button.place(relx=0.4, rely=0.6)

    delete_button = tk.Button(test_page_admin_frame, text="Delete", font="times 12 bold", bg="white",command=delete_datatest)
    delete_button.place(relx=0.7, rely=0.6)

    fetch_button = tk.Button(test_page_admin_frame, text="Fetch", font="times 12 bold", bg="white",command=fetch_data_test)
    fetch_button.place(relx=0.7, rely=0.7)

def odi_page_admin():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    odi_page_admin_frame = tk.Frame(main_frame)
    odi_page_admin_frame.pack(fill=tk.BOTH, expand=True)

    # Label and TextField for search

    # Labels and TextFields for teams, ranking, matches, and points
    teams_label = tk.Label(odi_page_admin_frame, text="Teams:", font="times 12 bold")
    teams_label.place(relx=0.04, rely=0.2)

    ranking_label = tk.Label(odi_page_admin_frame, text="Ranking:", font="times 12 bold")
    ranking_label.place(relx=0.04, rely=0.35)

    matches_label = tk.Label(odi_page_admin_frame, text="Matches:", font="times 12 bold")
    matches_label.place(relx=0.5, rely=0.2)

    points_label = tk.Label(odi_page_admin_frame, text="Points:", font="times 12 bold")
    points_label.place(relx=0.5, rely=0.35)
    global teams_entryo  # Corrected variable name
    global ranking_entryo  # Corrected variable name
    global matches_entryo  # Corrected variable name
    global points_entryo  # Corrected variable name

    teams_entryo = tk.Entry(odi_page_admin_frame, font="times 12 bold")
    teams_entryo.place(relx=0.15, rely=0.2)

    ranking_entryo = tk.Entry(odi_page_admin_frame, font="times 12 bold")
    ranking_entryo.place(relx=0.15, rely=0.35)

    matches_entryo = tk.Entry(odi_page_admin_frame, font="times 12 bold")
    matches_entryo.place(relx=0.6, rely=0.2)

    points_entryo = tk.Entry(odi_page_admin_frame, font="times 12 bold")
    points_entryo.place(relx=0.6, rely=0.35)

    add_button = tk.Button(odi_page_admin_frame, text="Add", font="times 12 bold", bg="white",command=insert_dataODI)
    add_button.place(relx=0.1, rely=0.6)

    update_button = tk.Button(odi_page_admin_frame, text="Update", font="times 12 bold", bg="white",command=update_dataodi)
    update_button.place(relx=0.4, rely=0.6)

    delete_button = tk.Button(odi_page_admin_frame, text="Delete", font="times 12 bold", bg="white",command=delete_dataodi)
    delete_button.place(relx=0.7, rely=0.6)
    fetch_button = tk.Button(odi_page_admin_frame, text="Fetch", font="times 12 bold", bg="white",command=fetch_data_odi)
    fetch_button.place(relx=0.7, rely=0.7)


def t20_page_admin():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    t20_page_admin_frame = tk.Frame(main_frame,)
    t20_page_admin_frame.pack(fill=tk.BOTH, expand=True)
    # Label and TextField for search


    # Labels and TextFields for teams, ranking, matches, and points
    teams_label = tk.Label(t20_page_admin_frame, text="Teams:", font="times 12 bold")
    teams_label.place(relx=0.04, rely=0.2)

    ranking_label = tk.Label(t20_page_admin_frame, text="Ranking:", font="times 12 bold")
    ranking_label.place(relx=0.04, rely=0.35)

    matches_label = tk.Label(t20_page_admin_frame, text="Matches:", font="times 12 bold")
    matches_label.place(relx=0.5, rely=0.2)

    points_label = tk.Label(t20_page_admin_frame, text="Points:", font="times 12 bold")
    points_label.place(relx=0.5, rely=0.35)
    global team_entrytt  # Corrected variable name
    global ranking_entrytt  # Corrected variable name
    global matches_entrytt  # Corrected variable name
    global points_entrytt

    team_entrytt = tk.Entry(t20_page_admin_frame, font="times 12 bold")
    team_entrytt.place(relx=0.15, rely=0.2)

    ranking_entrytt = tk.Entry(t20_page_admin_frame, font="times 12 bold")
    ranking_entrytt.place(relx=0.15, rely=0.35)

    matches_entrytt = tk.Entry(t20_page_admin_frame, font="times 12 bold")
    matches_entrytt.place(relx=0.6, rely=0.2)

    points_entrytt = tk.Entry(t20_page_admin_frame, font="times 12 bold")
    points_entrytt.place(relx=0.6, rely=0.35)
    add_button = tk.Button(t20_page_admin_frame, text="Add", font="times 12 bold",bg="white",command=insert_datat20)
    add_button.place(relx=0.1, rely=0.6)

    update_button = tk.Button(t20_page_admin_frame, text="Update", font="times 12 bold",bg="white",command=update_datat20)
    update_button.place(relx=0.4, rely=0.6)

    delete_button = tk.Button(t20_page_admin_frame, text="Delete", font="times 12 bold",bg="white",command=delete_datat20)
    delete_button.place(relx=0.7, rely=0.6)
    fetch_button = tk.Button(t20_page_admin_frame, text="Fetch", font="times 12 bold", bg="white",command=fetch_data_t20)
    fetch_button.place(relx=0.7, rely=0.7)
def t20_page():
    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    t20_page_frame = tk.Frame(main_frame)
    t20_page_frame.pack(fill=tk.BOTH, expand=True)
    t20_label = tk.Label(t20_page_frame,width=25, height=14, bg="white", bd=2, relief="solid")
    t20_label.place(relx=0.04,rely=0.05)
    t20_admin_button = tk.Button(t20_page_frame, text="Change", font="times 12 bold",command=t20_page_admin)
    t20_admin_button.place(relx=0.85, rely=0.01)
    label_2_image = tk.PhotoImage(file="t20f1.png")
    image_label2 = tk.Label(t20_label, image=label_2_image, bd=0)
    image_label2.image = label_2_image
    image_label2.pack(anchor="center")
    t20_label = tk.Label(t20_page_frame, width=15, height=2,text="T20I Ranking", bg="white")
    t20_label.place(relx=0.4, rely=0.43)
    t20_info = tk.Text(t20_page_frame, wrap="word", height=13, width=65)
    t20_info.insert("1.0",
                    "T20 International cricket, commonly referred to as T20I, is the shortest format of international cricket matches. Each team plays a single innings, which is restricted to a maximum number of overs, usually 20 overs per side. T20 cricket is known for its fast-paced and exciting gameplay, often featuring big hitting and aggressive bowling tactics.")
    t20_info.config(state="disabled")
    t20_info.place(relx=0.3, rely=0.06)
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
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor = conn.cursor()

    # Execute the query to select Rank and Name columns from playerperformance table
    query = "SELECT * FROM twenty ORDER BY Ranking ASC"
    cursor.execute(query)

    # Fetch all rows from the result set
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Change the headings
    tree1.heading("Teams", text="Ranking")
    tree1.heading("Ranking", text="Teams")
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
    odi_admin_button = tk.Button(odi_page_frame, text="Change", font="times 12 bold", command=odi_page_admin)
    odi_admin_button.place(relx=0.85, rely=0.01)
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
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor = conn.cursor()

    # Execute the query to select Rank and Name columns from playerperformance table
    query = "SELECT * FROM odi ORDER BY Ranking ASC"
    cursor.execute(query)

    # Fetch all rows from the result set
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Change the headings
    treeO.heading("Teams", text="Ranking")
    treeO.heading("Ranking", text="Teams")
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
    test_admin_button = tk.Button(test_page_frame, text="Change", font="times 12 bold", command=test_page_admin)
    test_admin_button.place(relx=0.85, rely=0.01)
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
    odi_info.place(relx=0.3, rely=0.06)
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
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor = conn.cursor()

    # Execute the query to select Rank and Name columns from playerperformance table
    query = "SELECT * FROM test ORDER BY Ranking ASC"
    cursor.execute(query)

    # Fetch all rows from the result set
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Change the headings
    treet.heading("Teams", text="Ranking")
    treet.heading("Ranking", text="Teams")
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
    label_frame = tk.Frame(home_frame, width=550, height=156, bg="white", bd=2, relief="solid")
    label_frame.place(relx=0.5, rely=0.31, anchor="center")
    # Fetch images from the database
    image_paths = fetch_images_from_database()

    # Create a label for the image slider
    global image_label
    image_label = tk.Label(label_frame,bg="white")
    image_label.pack()
    # Start the image slider
    update_image_slider(image_paths, 0)
    addimage_button = tk.Button(home_frame, text="Add Image", width=20, command=add_image_page)
    addimage_button.place(x=600, y=35)
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



def on_select(event):
    # Get selected item from the treeview
    selected_item = event.widget.selection()[0]

    # Get the name from the selected item
    selected_name = event.widget.item(selected_item, 'values')[1]

    # Open player.py script and pass the selected name as an argument
    subprocess.Popen(['python', 'player.py', selected_name])

def player_performance_page():
    # Clear the main frame
    global my_entry
    clear_main_frame()

    # Create a frame for player performance content
    player_performance_frame = tk.Frame(main_frame)
    player_performance_frame.pack(fill=tk.BOTH, expand=True)

    # Create a blue rectangle
    blue_rectangle = tk.Canvas(player_performance_frame, width=760, height=106, bg="blue")
    blue_rectangle.place(x=2, y=0)

    # Calculate the x-coordinate for the button to be at the right side of the rectangle
    button_x = blue_rectangle.winfo_x() + blue_rectangle.winfo_width() - 10

    # Create button inside the blue rectangle
    add_player_button = tk.Button(blue_rectangle, text="Add Player",command=open_playerperformanceadd_py)
    add_player_button.place(relx=0.88, rely=0.5, anchor="center")
    # Calculate the center coordinates of the blue rectangle
    center_x = 150 + 690 / 2
    center_y = 0 + 66 / 2

    # Create text field for search
    my_entry = tk.Entry(player_performance_frame)
    my_entry.place(x=center_x - 170, y=center_y - 0, anchor="center")
    my_list = tk.Listbox(player_performance_frame,height=3)
    my_list.place(x=center_x - 231, y=center_y + 10)


    # Create search button
    search_button = tk.Button(player_performance_frame, text="Search",command=search_player)
    search_button.place(x=center_x - 45, y=center_y - 0, anchor="center")

    # Function to update treeview based on search
    def update(data):
        my_list.delete(0, END)

        for item in data:
            my_list.insert(END, item)

    def fillout(e):
        my_entry.delete(0, END)
        my_entry.insert(0, my_list.get(tk.ACTIVE))

    def check(e):
        typed = my_entry.get()

        if typed == '':
            data = names
        else:
            data = []
            for item in names:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)

    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor = conn.cursor()

    # Execute the query to select Rank and Name columns from playerperformance table
    query = "SELECT name FROM playerperformance"
    cursor.execute(query)

    # Fetch all rows from the result set
    records = cursor.fetchall()
    names = [record[0] for record in records]

    # Close the cursor and connection
    cursor.close()
    conn.close()
    update(names)

    my_list.bind("<<ListboxSelect>>", fillout)

    my_entry.bind("<KeyRelease>", check)

    # Call the check function when the search button is clicked

    # Call the check function when the search button is clicked
    tree1p = ttk.Treeview(player_performance_frame, columns=("Ranking","Player"), show="headings")
    tree1p.heading("Ranking", text="Ranking")
    tree1p.heading("Player", text="Player")
    tree1p.place(x=3, y=110, width=760, height=610)

    # Populate the table

    # Create treeview widget for the table
    tree1p.bind("<<TreeviewSelect>>", on_select)

    # Populate the table
    populate_table2p(tree1p)


def populate_table2p(tree1p):
    # Insert data into the table
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor11 = conn.cursor()

    # Execute the query to select Name and Rank columns from playerperformance table
    query = "SELECT * FROM playerperformance ORDER BY `Rank` ASC"

    cursor11.execute(query)

    # Fetch all rows from the result set
    data = cursor11.fetchall()

    # Close the cursor and connection
    cursor11.close()
    conn.close()

    # Clear existing data in the table
    for row in tree1p.get_children():
        tree1p.delete(row)

    # Change the headings
    tree1p.heading("Ranking", text="Rank")
    tree1p.heading("Player", text="Name")

    # Populate the table with fetched data
    for row in data:
        # Insert only two columns (Name and Rank) into the table
        tree1p.insert("", "end", values=(row[1], row[0]))
        # Note: The order is (Rank, Name)







def player_comparison_page():
    # Clear the main frame
    global einl, eavg, ehs, erun, efh, esr, einl3, eavg3, ehs1, erun1, efh1, esr1, einl1, eavg1, ehs2, erun2, text_field1, text_field2, label1_frame, label2_frame

    clear_main_frame()

    # Create a frame for player comparison page content
    player_comparison_frame = tk.Frame(main_frame)
    player_comparison_frame.pack(fill=tk.BOTH, expand=True)

    # Create text field 1
    text_field1 = tk.Entry(player_comparison_frame, width=35)
    text_field1.place(relx=0.3, rely=0.03, anchor="center")

    # Create text field 2
    text_field2 = tk.Entry(player_comparison_frame, width=35)
    text_field2.place(relx=0.7, rely=0.03, anchor="center")

    # Create label 1 with black border
    label1_frame = tk.Frame(player_comparison_frame, width=120, height=149, bd=2, relief="solid", bg="white")
    label1_frame.place(relx=0.3, rely=0.3, anchor="center")

    # Create label 2 with black border
    label2_frame = tk.Frame(player_comparison_frame, width=123, height=155, bd=2, relief="solid", bg="white")
    label2_frame.place(relx=0.7, rely=0.3, anchor="center")

    # Create button inside the blue rectangle
    compare_button = tk.Button(player_comparison_frame, text="Compare",command=displayingplayers)
    compare_button.place(relx=0.5, rely=0.32, anchor="center")
 # Create labels for statistics
    inl = tk.Label(player_comparison_frame, text="Innings:", font=("Arial", 11, "bold"))
    inl.place(relx=0.04,rely=0.55)
    hs = tk.Label(player_comparison_frame, text="HighestScore:", font=("Arial", 11, "bold"))
    hs.place(relx=0.04,rely=0.6)
    run = tk.Label(player_comparison_frame, text="Runs:", font=("Arial", 11, "bold"))
    run.place(relx=0.04,rely=0.65)
    sr = tk.Label(player_comparison_frame, text="Strike Rate:", font=("Arial", 11, "bold"))
    sr.place(relx=0.04, rely=0.7)
    ov = tk.Label(player_comparison_frame, text="Overs:", font=("Arial", 11, "bold"))
    ov.place(relx=0.04, rely=0.75)
    wk = tk.Label(player_comparison_frame, text="Wickets:", font=("Arial", 11, "bold"))
    wk.place(relx=0.04, rely=0.8)
    er = tk.Label(player_comparison_frame, text="EconomyRate:", font=("Arial", 11, "bold"))
    er.place(relx=0.04, rely=0.85)
    best = tk.Label(player_comparison_frame, text="Best:", font=("Arial", 11, "bold"))
    best.place(relx=0.04, rely=0.9)
    # Empty labels under each horizontal label
    einl = tk.Label(player_comparison_frame, text="")
    einl.place(relx=0.2, rely=0.55)
    eavg = tk.Label(player_comparison_frame, text="")
    eavg.place(relx=0.2, rely=0.6)
    ehs = tk.Label(player_comparison_frame, text="")
    ehs.place(relx=0.2, rely=0.65)
    erun = tk.Label(player_comparison_frame, text="")
    erun.place(relx=0.2, rely=0.7)
    efh = tk.Label(player_comparison_frame, text="")
    efh.place(relx=0.2, rely=0.75)
    esr = tk.Label(player_comparison_frame, text="")
    esr.place(relx=0.2, rely=0.8)
    # Empty labels under each horizontal label
    einl3 = tk.Label(player_comparison_frame, text="")
    einl3.place(relx=0.2, rely=0.85)
    eavg3 = tk.Label(player_comparison_frame, text="")
    eavg3.place(relx=0.2, rely=0.9)
    ehs1 = tk.Label(player_comparison_frame, text="")
    ehs1.place(relx=0.6, rely=0.55)
    erun1 = tk.Label(player_comparison_frame, text="")
    erun1.place(relx=0.6, rely=0.6)
    efh1 = tk.Label(player_comparison_frame, text="")
    efh1.place(relx=0.6, rely=0.65)
    esr1 = tk.Label(player_comparison_frame, text="")
    esr1.place(relx=0.6, rely=0.7)
    # Empty labels under each horizontal label
    einl1 = tk.Label(player_comparison_frame, text="")
    einl1.place(relx=0.6, rely=0.75)
    eavg1 = tk.Label(player_comparison_frame, text="")
    eavg1.place(relx=0.6, rely=0.8)
    ehs2 = tk.Label(player_comparison_frame, text="")
    ehs2.place(relx=0.6, rely=0.85)
    erun2 = tk.Label(player_comparison_frame, text="")
    erun2.place(relx=0.6, rely=0.9)
    # Create Listbox 1
    listbox1 = tk.Listbox(player_comparison_frame, width=35, height=3)
    listbox1.place(relx=0.3, rely=0.09, anchor="center")

    # Create Listbox 2
    listbox2 = tk.Listbox(player_comparison_frame, width=35, height=3)
    listbox2.place(relx=0.7, rely=0.09, anchor="center")

    # Function to update Listbox 1 based on search
    def update_listbox1(data):
        listbox1.delete(0, tk.END)
        for item in data:
            listbox1.insert(tk.END, item)

    # Function to update Listbox 2 based on search
    def update_listbox2(data):
        listbox2.delete(0, tk.END)
        for item in data:
            listbox2.insert(tk.END, item)
    def fillout1(e):
        text_field1.delete(0, END)
        text_field1.insert(0, listbox1.get(tk.ACTIVE))
    def fillout2(e):
        text_field2.delete(0, END)
        text_field2.insert(0, listbox2.get(tk.ACTIVE))



    # Function to handle search in Listbox 1
    def search_listbox1(e):
        typed = text_field1.get().lower()
        filtered_data = [item for item in player_names if typed in item.lower()]
        update_listbox1(filtered_data)

    # Function to handle search in Listbox 2
    def search_listbox2(e):
        typed = text_field2.get().lower()
        filtered_data = [item for item in player_names if typed in item.lower()]
        update_listbox2(filtered_data)

    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor = conn.cursor()

    # Execute the query to select names from playerperformance table
    query = "SELECT name FROM playerperformance"
    cursor.execute(query)

    # Fetch all rows from the result set
    records = cursor.fetchall()
    player_names = [record[0] for record in records]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Update both Listboxes with player names
    update_listbox1(player_names)
    update_listbox2(player_names)

    # Bind events to handle search in Listbox 1 and Listbox 2
    text_field1.bind("<KeyRelease>", search_listbox1)
    text_field2.bind("<KeyRelease>", search_listbox2)
    listbox1.bind("<<ListboxSelect>>", fillout1)
    listbox2.bind("<<ListboxSelect>>", fillout2)




def displayingplayers():
    displayplayer1()
    displayplayer2()
def displayplayer1():
    Player1 = text_field1.get()
    query = "SELECT * FROM playerperformance WHERE Name = %s"
    cursor.execute(query, (Player1,))
    result = cursor.fetchone()
    name = result[0]
    rank = result[1]
    dob = result[2]
    height = result[3]
    weight = result[4]
    batting_bowling = result[5]
    age = result[6]
    teams = result[7]
    image_path = result[8]  # Assuming this is the path to the image file
    innings = result[9]
    average = result[10]
    highest_score = result[11]
    runs = result[12]
    fifty_hundreds = result[13]
    strike_rate = result[14]
    overs = result[15]
    wickets = result[16]
    best = result[17]
    economy_rate = result[18]
    if result:
        image = Image.open(io.BytesIO(image_path))
        image = image.resize((120, 149))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)

        # Clear any existing widgets inside the frame
        for widget in label1_frame.winfo_children():
            widget.destroy()

        # Create a label and display the image
        image_label = tk.Label(label1_frame, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack()
        ehs1.config(text=innings)
        erun1.config(text=highest_score)
        efh1.config(text=runs)
        esr1.config(text=strike_rate)
        einl1.config(text=overs)
        eavg1.config(text=wickets)
        ehs2.config(text=economy_rate)
        erun2.config(text=best)
    else:
        messagebox.showerror("Error", f"No data found for player {Player1}")

def displayplayer2():
    Player2 = text_field2.get()
    query = "SELECT * FROM playerperformance WHERE Name = %s"
    cursor.execute(query, (Player2,))
    result = cursor.fetchone()
    name = result[0]
    rank = result[1]
    dob = result[2]
    height = result[3]
    weight = result[4]
    batting_bowling = result[5]
    age = result[6]
    teams = result[7]
    image_path = result[8]  # Assuming this is the path to the image file
    innings = result[9]
    average = result[10]
    highest_score = result[11]
    runs = result[12]
    fifty_hundreds = result[13]
    strike_rate = result[14]
    overs = result[15]
    wickets = result[16]
    best = result[17]
    economy_rate = result[18]
    if result:
        image = Image.open(io.BytesIO(image_path))
        image = image.resize((120, 149))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)

        # Clear any existing widgets inside the frame
        for widget in label2_frame.winfo_children():
            widget.destroy()

        # Create a label and display the image
        image_label = tk.Label(label2_frame, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack()
        einl.config(text=innings)
        eavg.config(text=highest_score)
        ehs.config(text=runs)
        erun.config(text=strike_rate)
        efh.config(text=overs)
        esr.config(text=wickets)
        einl3.config(text=economy_rate)
        eavg3.config(text=best)
    else:
        messagebox.showerror("Error", f"No data found for player {Player2}")

def fields():
    # Clear the main frame
    clear_main_frame()
    # Clear the main frame
    # Create a frame for player performance content
    fields_frame = tk.Frame(main_frame)
    fields_frame.pack(fill=tk.BOTH, expand=True)
    Field_label = tk.Label(fields_frame, text="Field Determination", font="times 20 bold", foreground="blue", relief="raised",
                        padx=10, pady=10)
    Field_label.pack()
    label2_frame = tk.Frame(fields_frame, width=200, height=325, bd=2, relief="solid", bg="white")
    label2_frame.place(relx=0.84, rely=0.45, anchor="center")

    bowlingstyleEntry = tk.Label(fields_frame,text="Bowling Style", font="times 15 bold")
    bowlingstyleEntry.place(x=40, y=110)
    bowlingstyleEntryt = tk.Label(fields_frame, text="Bowling Style", font="times 15 bold")
    bowlingstyleEntryt.place(x=40, y=170)

    bowlingtypeEntryi = tk.Entry(fields_frame, font="times 15 bold", width=20, bg="white")
    bowlingtypeEntryi.place(x=270, y=110)
    bowlingtypeEntryT = tk.Entry(fields_frame, font="times 15 bold", width=20, bg="white")
    bowlingtypeEntryT.place(x=270, y=170)
    fieldinfo_label = tk.Label(fields_frame, text="Field Information", font="times 15 bold")
    fieldinfo_label.place(x=40, y=200)
    field_info = tk.Text(fields_frame, wrap="word", height=20, width=55, bd=2)
    field_info.place(x=45, y=250)

def playerp():
    clear_main_frame()

    # Create a frame for player performance content
    pp_frame = tk.Frame(main_frame)
    pp_frame.pack(fill=tk.BOTH, expand=True)
    label_frame = tk.Frame(pp_frame,width=200, height=255, bg="white", bd=2, relief="solid")
    label_frame.place(relx=0.2, rely=0.31, anchor="center")

    Full_name_label = tk.Label(pp_frame, text="Full Name", font="times 15 bold")
    Full_name_label.place(x=300, y=100, width=120, height=25)

    Height_label = tk.Label(pp_frame, text="Height", font="times 15 bold")
    Height_label.place(x=300, y=150, width=120, height=25)

    Weight_Score_label = tk.Label(pp_frame, text="Weight", font="times 15 bold")
    Weight_Score_label.place(x=300, y=200, width=120, height=25)

    DOB_label = tk.Label(pp_frame, text="Date Of Birth", font="times 15 bold")
    DOB_label.place(x=500, y=100, width=120, height=25)

    Teams_label = tk.Label(pp_frame, text="Team", font="times 15 bold")
    Teams_label.place(x=500, y=150, width=120, height=25)

    # Labels for headers
    headers = ["FORMAT", "Mat", "Inns", "NO", "Runs", "HS", "Ave", "100s", "50s", "6s", "Ct", "St"]
    for i, header in enumerate(headers):
        tk.Label(pp_frame, text=header, font=("Helvetica", 10, "bold")).place(x=i * 50 + 100, y=450, width=60, height=25)

    # Data
    data = [
        ["overall", 52, 80, 10, 6996, "334", 99.94, 29, 13, 6, 32, 0],
        ["LF", 234, 338, 43, 28067, "452*", 95.14, 117, 69, "-", 131, 1]
    ]

    # Displaying data
    for i, row in enumerate(data, start=1):
        for j, item in enumerate(row):
            tk.Label(pp_frame, text=item).place(x=j * 50 + 100, y=i * 25 + 450, width=60, height=25)

# Function to handle search button click


def on_select1(event1):
    # Get selected item from the treeview
    selected_item = event1.widget.selection()[0]

    # Get the name from the selected item
    selected_name = event1.widget.item(selected_item, 'values')[1]

    # Open player.py script and pass the selected name as an argument
    subprocess.Popen(['python', 'field_display.py', selected_name])

def field_determination_page():
    global my_entryf

    # Clear the main frame
    clear_main_frame()

    # Create a frame for player performance content
    field_determination_frame = tk.Frame(main_frame)
    field_determination_frame.pack(fill=tk.BOTH, expand=True)

    # Create a blue rectangle
    blue_rectangle = tk.Canvas(field_determination_frame, width=760, height=106, bg="blue")
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
    my_entryf = tk.Entry(field_determination_frame)
    my_entryf.place(x=center_x - 170, y=center_y - 0, anchor="center")
    my_listf = tk.Listbox(field_determination_frame, height=3)
    my_listf.place(x=center_x - 231, y=center_y + 10)

    # Create search button
    search_button = tk.Button(field_determination_frame, text="Search", command=search_button_click)
    search_button.place(x=center_x - 45, y=center_y - 0, anchor="center")


    # Function to update treeview based on search
    def update(data):
        my_listf.delete(0, END)

        for item in data:
            my_listf.insert(END, item)

    def fillout(e):
        my_entryf.delete(0, END)
        my_entryf.insert(0, my_listf.get(tk.ACTIVE))

    def check(e):
        typed = my_entryf.get()

        if typed == '':
            data = names
        else:
            data = []
            for item in names:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)

    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor = conn.cursor()

    # Execute the query to select Rank and Name columns from playerperformance table
    query = "SELECT bowling_style FROM field"
    cursor.execute(query)

    # Fetch all rows from the result set
    records = cursor.fetchall()
    names = [record[0] for record in records]

    # Close the cursor and connection
    cursor.close()
    conn.close()
    update(names)

    my_listf.bind("<<ListboxSelect>>", fillout)

    my_entryf.bind("<KeyRelease>", check)
    # Create search button

    # Create treeview widget for the table
    tree = ttk.Treeview(field_determination_frame, columns=("Bowling style", "Bowling type"), show="headings")
    tree.heading("Bowling style", text="Bowling style")
    tree.heading("Bowling style", text="Bowling style")

    tree.place(x=3, y=110, width=760, height=610)

    # Populate the table
    tree.bind("<<TreeviewSelect>>", on_select1)

    # Populate the table
    populate_table1(tree)

def populate_table1(tree):
    # Insert data into the table
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor110 = conn.cursor()

    # Execute the query to select Name and Rank columns from playerperformance table
    query = "select * from field"
    cursor110.execute(query)

    # Fetch all rows from the result set
    data = cursor110.fetchall()

    # Close the cursor and connection
    cursor110.close()
    conn.close()

    # Clear existing data in the table
    for row in tree.get_children():
        tree.delete(row)

    # Change the headings
    tree.heading("Bowling style", text="Bowling Type")
    tree.heading("Bowling type", text="Bowling Style")

    # Populate the table with fetched data
    for row in data:
        # Insert only two columns (Name and Rank) into the table
        tree.insert("", "end", values=(row[1], row[0]))
        # Note: The order is (Rank, Name)


def on_tree_select(event):
        # Call the fields() function when any row is clicked
        fields()

# Function to handle search button click
def search_button_click():
    bs = my_entryf.get()
    subprocess.call(["python","field_display.py",bs])
def search_player():
    player_name = my_entry.get()
    if player_name:
        try:
            subprocess.Popen(['python', 'player.py', player_name])
        except FileNotFoundError:
            messagebox.showerror("Error", "player.py not found")
    else:
        messagebox.showerror("Error", "Please enter a player name")


def open_second_py():
    subprocess.call(["python", "second.py"])

def open_playerperformanceadd_py():
    subprocess.call(["python", "playerperformanceadd.py"])


def logout():
    # Destroy the current tkinter window
    root.destroy()

    # Call the choosing window script
    subprocess.call(["python", "choosingwindow.py"])


options_frame = tk.Frame(root, width=252, height=490, bg="blue")
options_frame.pack(side="left", fill="y")

buttons = [
    ("Home", indicate_home),
    ("Player Performance", indicate_player_performance),
    ("Player Comparison", indicate_player_comparison),
    ("Field Determination", indicate_field_determination),
    ("Logout",logout)
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
