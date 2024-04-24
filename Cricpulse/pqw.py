import tkinter as tk
import mysql.connector

# Function to fetch data from the database
def fetch_data_from_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Parthavi@1204",
        database="cricpulse"
    )
    cursor = conn.cursor()

    # Execute the query to retrieve data
    query = "SELECT Innings, Average, HighestScore, Runs, 50_100, StrikeRate FROM playerperformance WHERE Name=gdkd'"
    cursor.execute(query)

    # Fetch all rows from the result set
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return data

# Creating the main window
root = tk.Tk()
root.geometry("900x600")
root.title("Player Stats")

label_framem = tk.Frame(width=850, height=300, bd=2, relief="solid")
label_framem.place(relx=0.5, rely=0.31, anchor="center")

label_frame = tk.Frame(label_framem,width=140, height=185, bg="white", bd=2, relief="solid")
label_frame.place(relx=0.15, rely=0.50, anchor="center")

# Labels for player information
Full_name_label = tk.Label(label_framem, text="Full Name", font=("Helvetica", 10, "bold"))
Full_name_label.place(x=300, y=100, width=100, height=25)

Height_label = tk.Label(label_framem, text="Height", font=("Helvetica", 10, "bold"))
Height_label.place(x=300, y=150, width=100, height=25)

Weight_Score_label = tk.Label(label_framem, text="Weight", font=("Helvetica", 10, "bold"))
Weight_Score_label.place(x=300, y=200, width=100, height=25)

DOB_label = tk.Label(label_framem, text="Date Of Birth", font=("Helvetica", 10, "bold"))
DOB_label.place(x=600, y=100, width=100, height=25)

Teams_label = tk.Label(label_framem, text="Team", font=("Helvetica", 10, "bold"))
Teams_label.place(x=600, y=150, width=100, height=25)

# Headers for batting statistics
headers = ["Innings", "Average", "HighestScore", "Runs", "50_100", "StrikeRate"]

# Display headers
for i, header in enumerate(headers):
    tk.Label(root, text=header, font=("Helvetica", 10, "bold")).place(x=i*110 + 10, y=500, width=100, height=25)

# Fetch data from the database
data = fetch_data_from_database()

# Displaying data
for i, row in enumerate(data, start=1):
    for j, item in enumerate(row):
        # Calculate width for each column based on the length of the data
        width = max(len(str(item)), 5) * 10
        tk.Label(root, text=item).place(x=j*110 + 10, y=i*25 + 500, width=100, height=25)

root.mainloop()
