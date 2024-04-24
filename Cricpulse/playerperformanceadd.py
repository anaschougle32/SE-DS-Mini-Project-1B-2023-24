import tkinter as tk
from datetime import datetime

import mysql.connector
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO


root = tk.Tk()
root.geometry("935x610")
root.configure(bg="white")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Parthavi@1204",
    database="cricpulse",
    auth_plugin='mysql_native_password'
)
cursor = db.cursor()


def select_image():
    global image_path
    image_path = filedialog.askopenfilename()
    display_selected_image(image_path)


def display_selected_image(image_path):
    try:
        global label_framei

        # Clear any existing widgets inside the frame
        for widget in label_framei.winfo_children():
            widget.destroy()

        # Load the image
        image = Image.open(image_path)
        image = image.resize((200, 200))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)

        # Create a label and display the image
        image_label = tk.Label(label_framei, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack()  # Use pack() to display the label inside the frame
    except Exception as e:
        messagebox.showerror("Error", f"Error displaying image: {e}")


def clear_text_fields():
    # Clear all text fields
    name_textfield.delete(0, 'end')
    dob_textfield.delete(0, 'end')
    text_field_height.delete(0, 'end')
    text_field_weight.delete(0, 'end')
    text_field_bats_bowls.delete(0, 'end')
    text_field_age.delete(0, 'end')
    text_field_teams.delete(0, 'end')
    inning_textfield.delete(0, 'end')
    average_textfield.delete(0, 'end')
    hs_textfield.delete(0, 'end')
    runs_textfield.delete(0, 'end')
    fittyhundredt_textfield.delete(0, 'end')
    sr_textfield.delete(0, 'end')
    over_textfield.delete(0, 'end')
    wicket_textfield.delete(0, 'end')
    best_textfield.delete(0, 'end')
    er_textfield.delete(0, 'end')
    text_field1.delete(0, 'end')
    text_field2.delete(0, 'end')
    text_field3.delete(0, 'end')
    text_field4.delete(0, 'end')
    text_field5.delete(0, 'end')
    text_field6.delete(0, 'end')
    text_field7.delete(0, 'end')
    text_field8.delete(0, 'end')
    text_field9.delete(0, 'end')
    text_field10.delete(0, 'end')
    wins_lost_text_field.delete(0, 'end')
    rank_textfield.delete(0,'end')

    # Clear the previewed image
    clear_previewed_image()


def clear_previewed_image():
    for widget in label_framei.winfo_children():
        widget.destroy()
def insert_data():
    try:
        global image_path

        if image_path == "":
            messagebox.showerror("Error", "Please select an image.")
            return
        # Get values from tkinter fields
        name = name_textfield.get()
        dob_str = dob_textfield.get()  # Assuming dob_textfield contains date in format "DD/MM/YYYY"
        dob = datetime.strptime(dob_str, "%d/%m/%Y").date()
        height = float(text_field_height.get())
        weight = float(text_field_weight.get())
        batting_bowling = text_field_bats_bowls.get()
        age = int(text_field_age.get())
        teams = text_field_teams.get()
        innings = int(inning_textfield.get())
        average = float(average_textfield.get())
        highest_score = int(hs_textfield.get())
        runs = int(runs_textfield.get())
        fifty_hundreds = int(fittyhundredt_textfield.get())
        strike_rate = float(sr_textfield.get())
        overs = float(over_textfield.get())
        wickets = int(wicket_textfield.get())
        best = best_textfield.get()
        economy_rate = float(er_textfield.get())
        r_01_05 = int(text_field1.get())
        r_06_10 = int(text_field2.get())
        r_11_15 = int(text_field3.get())
        r_16_20 = int(text_field4.get())
        r_21_25 = int(text_field5.get())
        w_01_05 = int(text_field6.get())
        w_06_10 = int(text_field7.get())
        w_11_15 = int(text_field8.get())
        w_16_20 = int(text_field9.get())
        w_21_25 = int(text_field10.get())
        wins_lost = wins_lost_text_field.get()
        rank = int(rank_textfield.get())  # Get rank from the text field

        # Read image file in binary mode
        with open(image_path, 'rb') as file:
            image_data = file.read()

        # Insert data into the table
        query = """INSERT INTO playerperformance 
                    (Name, `Rank`, DOB, Height, Weight, BattingBowling, Age, Teams, Image, Innings, Average, HighestScore, 
                    Runs, 50_100, StrikeRate, Overs, Wickets, Best, EconomyRate, 01_05r, 06_10r, 11_15r, 
                    16_20r, 21_25r, 01_05w, 06_10w, 11_15w, 16_20w, 21_25w, Wins_Lost) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (name,rank, dob, height, weight, batting_bowling, age, teams, image_data, innings, average, highest_score,
                  runs, fifty_hundreds, strike_rate, overs, wickets, best, economy_rate, r_01_05, r_06_10, r_11_15,
                  r_16_20, r_21_25, w_01_05, w_06_10, w_11_15, w_16_20, w_21_25, wins_lost)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def fetch_data():
    # Get the name from the name text field
    name = name_textfield.get()

    # Query to fetch data from the database based on the name
    query = "SELECT * FROM playerperformance WHERE Name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchall()

    # Check if any data is found
    if result:
        # Since there may be multiple rows, we'll only display the data from the first row
        row_data = result[0]

        # Populate the text fields with the fetched data
        name_textfield.delete(0, tk.END)
        name_textfield.insert(tk.END, row_data[0])  # Name

        rank_textfield.delete(0, tk.END)
        rank_textfield.insert(tk.END, row_data[1])  # Rank

        dob_textfield.delete(0, tk.END)
        dob_textfield.insert(tk.END, row_data[2])  # DOB

        text_field_height.delete(0, tk.END)
        text_field_height.insert(tk.END, row_data[3])  # Height

        text_field_weight.delete(0, tk.END)
        text_field_weight.insert(tk.END, row_data[4])  # Weight

        text_field_bats_bowls.delete(0, tk.END)
        text_field_bats_bowls.insert(tk.END, row_data[5])  # BattingBowling

        text_field_age.delete(0, tk.END)
        text_field_age.insert(tk.END, row_data[6])  # Age

        text_field_teams.delete(0, tk.END)
        text_field_teams.insert(tk.END, row_data[7])  # Teams

        # Fetch and display the image
        image_data = row_data[8]  # Image
        if image_data:
            image = Image.open(BytesIO(image_data))
            image = image.resize((200, 200))  # Adjust the size as needed
            photo = ImageTk.PhotoImage(image)

            global label_framei
            # Clear any existing widgets inside the frame
            for widget in label_framei.winfo_children():
                widget.destroy()

            # Create a label and display the image
            image_label = tk.Label(label_framei, image=photo)
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.pack()  # Use pack() to display the label inside the frame

        inning_textfield.delete(0, tk.END)
        inning_textfield.insert(tk.END, row_data[9])  # Innings

        average_textfield.delete(0, tk.END)
        average_textfield.insert(tk.END, row_data[10])  # Average

        hs_textfield.delete(0, tk.END)
        hs_textfield.insert(tk.END, row_data[11])  # HighestScore

        runs_textfield.delete(0, tk.END)
        runs_textfield.insert(tk.END, row_data[12])  # Runs

        fittyhundredt_textfield.delete(0, tk.END)
        fittyhundredt_textfield.insert(tk.END, row_data[13])  # 50_100

        sr_textfield.delete(0, tk.END)
        sr_textfield.insert(tk.END, row_data[14])  # StrikeRate

        over_textfield.delete(0, tk.END)
        over_textfield.insert(tk.END, row_data[15])  # Overs

        wicket_textfield.delete(0, tk.END)
        wicket_textfield.insert(tk.END, row_data[16])  # Wickets

        best_textfield.delete(0, tk.END)
        best_textfield.insert(tk.END, row_data[17])  # Best

        er_textfield.delete(0, tk.END)
        er_textfield.insert(tk.END, row_data[18])  # EconomyRate

        text_field1.delete(0, tk.END)
        text_field1.insert(tk.END, row_data[19])  # 01_05r

        text_field2.delete(0, tk.END)
        text_field2.insert(tk.END, row_data[20])  # 06_10r

        text_field3.delete(0, tk.END)
        text_field3.insert(tk.END, row_data[21])  # 11_15r

        text_field4.delete(0, tk.END)
        text_field4.insert(tk.END, row_data[22])  # 16_20r

        text_field5.delete(0, tk.END)
        text_field5.insert(tk.END, row_data[23])  # 21_25r

        text_field6.delete(0, tk.END)
        text_field6.insert(tk.END, row_data[24])  # 01_05w

        text_field7.delete(0, tk.END)
        text_field7.insert(tk.END, row_data[25])  # 06_10w

        text_field8.delete(0, tk.END)
        text_field8.insert(tk.END, row_data[26])  # 11_15w

        text_field9.delete(0, tk.END)
        text_field9.insert(tk.END, row_data[27])  # 16_20w

        text_field10.delete(0, tk.END)
        text_field10.insert(tk.END, row_data[28])  # 21_25w

        wins_lost_text_field.delete(0, tk.END)
        wins_lost_text_field.insert(tk.END, row_data[29])  # Wins_Lost

    else:
        # If no data is found, show a message
        messagebox.showinfo("Error", "No data found for the entered name")
def update_data():
    try:
        global image_path

        if image_path == "":
            messagebox.showerror("Error", "Please select an image.")
            return

        # Get values from tkinter fields
        name = name_textfield.get()
        dob_str = dob_textfield.get()  # Assuming dob_textfield contains date in format "DD/MM/YYYY"
        dob = datetime.strptime(dob_str, "%d/%m/%Y").date()
        height = float(text_field_height.get())
        weight = float(text_field_weight.get())
        batting_bowling = text_field_bats_bowls.get()
        age = int(text_field_age.get())
        teams = text_field_teams.get()
        innings = int(inning_textfield.get())
        average = float(average_textfield.get())
        highest_score = int(hs_textfield.get())
        runs = int(runs_textfield.get())
        fifty_hundreds = fittyhundredt_textfield.get()  # Assuming this is a string field for "50/100"
        strike_rate = float(sr_textfield.get())
        overs = float(over_textfield.get())
        wickets = int(wicket_textfield.get())
        best = best_textfield.get()
        economy_rate = float(er_textfield.get())
        r_01_05 = int(text_field1.get())
        r_06_10 = int(text_field2.get())
        r_11_15 = int(text_field3.get())
        r_16_20 = int(text_field4.get())
        r_21_25 = int(text_field5.get())
        w_01_05 = int(text_field6.get())
        w_06_10 = int(text_field7.get())
        w_11_15 = int(text_field8.get())
        w_16_20 = int(text_field9.get())
        w_21_25 = int(text_field10.get())
        wins_lost = wins_lost_text_field.get()
        rank = int(rank_textfield.get())  # Get rank from the text field

        # Read image file in binary mode
        with open(image_path, 'rb') as file:
            image_data = file.read()

        # Establish connection to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Parthavi@1204",
            database="cricpulse"
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Prepare the SQL query
        update_query = """UPDATE playerperformance SET
    `Rank` = %s, `DOB` = %s, `Height` = %s, `Weight` = %s, `BattingBowling` = %s, `Age` = %s,
    `Teams` = %s, `Image` = %s, `Innings` = %s, `Average` = %s, `HighestScore` = %s,
    `Runs` = %s, `50_100` = %s, `StrikeRate` = %s, `Overs` = %s, `Wickets` = %s, `Best` = %s,
    `EconomyRate` = %s, `01_05r` = %s, `06_10r` = %s, `11_15r` = %s, `16_20r` = %s, `21_25r` = %s,
    `01_05w` = %s, `06_10w` = %s, `11_15w` = %s, `16_20w` = %s, `21_25w` = %s, `Wins_Lost` = %s
WHERE `Name` = %s
 """

        # Execute the query
        cursor.execute(update_query, (
            rank, dob, height, weight, batting_bowling, age, teams, image_data, innings, average, highest_score,
            runs, fifty_hundreds, strike_rate, overs, wickets, best, economy_rate, r_01_05, r_06_10, r_11_15,
            r_16_20, r_21_25, w_01_05, w_06_10, w_11_15, w_16_20, w_21_25, wins_lost, name
        ))

        # Commit changes
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Data updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def delete_data():
    try:
        name = name_textfield.get()

        # Delete data from the table
        query = "DELETE FROM playerperformance WHERE Name = %s"
        cursor.execute(query, (name,))
        db.commit()
        clear_text_fields()
        clear_previewed_image()
        messagebox.showinfo("Success", "Data deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

global label_framei
label_framei = tk.Frame(root, width=187, height=222, bd=1, relief="solid")
label_framei.place(relx=0.15, rely=0.25, anchor='center')

select_image_button = tk.Button(root, text="Select Image", command=select_image)
select_image_button.place(relx=0.1, rely=0.45)
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.place(relx=0.01, rely=0.45)
submit_button = tk.Button(root, text="Delete", width=20,command=delete_data)
submit_button.place(relx=0.8, rely=0.95)
clear_button = tk.Button(root, text="Clear Text Fields", command=clear_text_fields)
clear_button.place(relx=0.2, rely=0.95)
submit_button = tk.Button(root, text="Update", width=20,command=update_data)
submit_button.place(relx=0.6, rely=0.95)
submit_button = tk.Button(root, text="Submit", width=20, command=insert_data)
submit_button.place(relx=0.4, rely=0.95)
label1rank_frame = tk.Label(root, text="Ranking", width=10, height=1)
label1rank_frame.place(relx=0.1, rely=0.55, anchor="center")
rank_textfield = tk.Entry(root, width=20)
rank_textfield.place(relx=0.15, rely=0.53)
label1_frame = tk.Label(root, text="Name", width=10, height=1)
label1_frame.place(relx=0.1, rely=0.59, anchor="center")
name_textfield = tk.Entry(root, width=20)
name_textfield.place(relx=0.15, rely=0.57)
label2_frame = tk.Label(root, text="Date of birth", width=10, height=1)
label2_frame.place(relx=0.1, rely=0.65, anchor="center")
dob_textfield = tk.Entry(root, width=20)
dob_textfield.place(relx=0.15, rely=0.63)
label_height = tk.Label(root, text="Height")
label_height.place(relx=0.1, rely=0.70, anchor="center")
text_field_height = tk.Entry(root, width=20)
text_field_height.place(relx=0.15, rely=0.68, anchor="w")

label_weight = tk.Label(root, text="Weight")
label_weight.place(relx=0.1, rely=0.75, anchor="center")
text_field_weight = tk.Entry(root, width=20)
text_field_weight.place(relx=0.15, rely=0.73, anchor="w")

label_bats_bowls = tk.Label(root, text="Bats/Bowls")
label_bats_bowls.place(relx=0.1, rely=0.82, anchor="center")
text_field_bats_bowls = tk.Entry(root, width=20)
text_field_bats_bowls.place(relx=0.15, rely=0.80, anchor="w")

label_age = tk.Label(root, text="Age")
label_age.place(relx=0.1, rely=0.89, anchor="center")
text_field_age = tk.Entry(root, width=20)
text_field_age.place(relx=0.15, rely=0.87, anchor="w")

label_teams = tk.Label(root, text="Teams")
label_teams.place(relx=0.1, rely=0.96, anchor="center")
text_field_teams = tk.Entry(root, width=20)
text_field_teams.place(relx=0.15, rely=0.94, anchor="w")

batting_frame = tk.Frame(root, width=250, height=222, bd=1, relief="solid")
batting_frame.place(relx=0.5, rely=0.25, anchor='center')
batting_heading = tk.Label(batting_frame, text="Batting", font=("Helvetica", 10, "bold"))
batting_heading.place(relx=0.5, rely=0.05, anchor="center")

batting_labels = ["Innings", "Average", "Highest Score", "Runs", "50s/100s", "Strike Rate"]
batting_text_fields = []

for index, batting_label_text in enumerate(batting_labels):
    label = tk.Label(batting_frame, text=batting_label_text)
    label.place(relx=0.5, rely=0.15 + index * 0.1, anchor="e")

inning_textfield = tk.Entry(batting_frame, width=15)
inning_textfield.place(relx=0.55, rely=0.12)
average_textfield = tk.Entry(batting_frame, width=15)
average_textfield.place(relx=0.55, rely=0.22)
hs_textfield = tk.Entry(batting_frame, width=15)
hs_textfield.place(relx=0.55, rely=0.32)
runs_textfield = tk.Entry(batting_frame, width=15)
runs_textfield.place(relx=0.55, rely=0.42)
fittyhundredt_textfield = tk.Entry(batting_frame, width=15)
fittyhundredt_textfield.place(relx=0.55, rely=0.52)
sr_textfield = tk.Entry(batting_frame, width=15)
sr_textfield.place(relx=0.55, rely=0.62)

bowling_frame = tk.Frame(root, width=250, height=222, bd=1, relief="solid")
bowling_frame.place(relx=0.85, rely=0.25, anchor='center')

bowling_heading = tk.Label(bowling_frame, text="Bowling", font=("Helvetica", 10, "bold"))
bowling_heading.place(relx=0.5, rely=0.05, anchor="center")

bowling_labels = ["Overs:", "Wickets:", "Best:", "Economy Rate:"]
bowling_text_fields = []

for index, bowling_label_text in enumerate(bowling_labels):
    label = tk.Label(bowling_frame, text=bowling_label_text)
    label.place(relx=0.48, rely=0.15 + index * 0.1, anchor="e")

over_textfield = tk.Entry(bowling_frame, width=15)
over_textfield.place(relx=0.55, rely=0.12)
wicket_textfield = tk.Entry(bowling_frame, width=15)
wicket_textfield.place(relx=0.55, rely=0.22)
best_textfield = tk.Entry(bowling_frame, width=15)
best_textfield.place(relx=0.55, rely=0.32)
er_textfield = tk.Entry(bowling_frame, width=15)
er_textfield.place(relx=0.55, rely=0.42)

captaincy_frame = tk.Frame(root, width=250, height=222, bd=1, relief="solid")
captaincy_frame.place(relx=0.85, rely=0.65, anchor='center')

captaincy_heading = tk.Label(captaincy_frame, text="Captaincy", font=("Helvetica", 10, "bold"))
captaincy_heading.place(relx=0.5, rely=0.05, anchor="center")

wins_lost_label = tk.Label(captaincy_frame, text="Wins:")
wins_lost_label.place(relx=0.48, rely=0.25, anchor="e")

wins_lost_text_field = tk.Entry(captaincy_frame, width=15)
wins_lost_text_field.place(relx=0.5, rely=0.25, anchor="w")

runs_wickets_frame = tk.Frame(root, width=250, height=222, bd=1, relief="solid")
runs_wickets_frame.place(relx=0.5, rely=0.65, anchor='center')

runs_wickets_heading = tk.Label(runs_wickets_frame, text="RUNS/WICKETS", font=("Helvetica", 10, "bold"))
runs_wickets_heading.place(relx=0.5, rely=0.05, anchor="center")
runs_label = tk.Label(runs_wickets_frame, text="Runs")
runs_label.place(x=100, y=40)

wickets_label = tk.Label(runs_wickets_frame, text="Wickets")
wickets_label.place(x=170, y=40)

runs_wickets_labels = ["2001-2005:", "2006-2010:", "2011-2015:", "2016-2020:", "2021-2025:"]
runs_wickets_text_fields = []

for a, runs_wickets_label_text in enumerate(runs_wickets_labels):
    label = tk.Label(runs_wickets_frame, text=runs_wickets_label_text)
    label.place(relx=0.30, rely=0.30 + a * 0.1, anchor="e")

text_field1 = tk.Entry(runs_wickets_frame, width=10)
text_field1.place(relx=0.3, rely=0.30, anchor="w")
text_field2 = tk.Entry(runs_wickets_frame, width=10)
text_field2.place(relx=0.3, rely=0.40, anchor="w")
text_field3 = tk.Entry(runs_wickets_frame, width=10)
text_field3.place(relx=0.3, rely=0.50, anchor="w")
text_field4 = tk.Entry(runs_wickets_frame, width=10)
text_field4.place(relx=0.3, rely=0.60, anchor="w")
text_field5 = tk.Entry(runs_wickets_frame, width=10)
text_field5.place(relx=0.3, rely=0.70, anchor="w")
text_field6 = tk.Entry(runs_wickets_frame, width=10)
text_field6.place(relx=0.6, rely=0.30, anchor="w")
text_field7 = tk.Entry(runs_wickets_frame, width=10)
text_field7.place(relx=0.6, rely=0.40, anchor="w")
text_field8 = tk.Entry(runs_wickets_frame, width=10)
text_field8.place(relx=0.6, rely=0.50, anchor="w")
text_field9 = tk.Entry(runs_wickets_frame, width=10)
text_field9.place(relx=0.6, rely=0.60, anchor="w")
text_field10 = tk.Entry(runs_wickets_frame, width=10)
text_field10.place(relx=0.6, rely=0.70, anchor="w")

root.mainloop()
