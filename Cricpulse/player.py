import tkinter as tk
from tkinter import Label, Frame, messagebox
import matplotlib.pyplot as plt
import mysql.connector
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import io
import sys
player_name = sys.argv[1]

root = tk.Tk()
root.title("Player Details")
root.geometry("1200x750")
# Connect to the database
# Make sure to replace the connection details with your own
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Parthavi@1204',
    database='cricpulse'
)
def display_player_details(player_name):
    player_data = fetch_player_data(player_name)
    name = player_data[0]
    rank = player_data[1]
    dob = player_data[2]
    height = player_data[3]
    weight = player_data[4]
    batting_bowling = player_data[5]
    age = player_data[6]
    teams = player_data[7]
    image_path = player_data[8]  # Assuming this is the path to the image file
    innings = player_data[9]
    average = player_data[10]
    highest_score = player_data[11]
    runs = player_data[12]
    fifty_hundreds = player_data[13]
    strike_rate = player_data[14]
    overs = player_data[15]
    wickets = player_data[16]
    best = player_data[17]
    economy_rate = player_data[18]
    if player_data:
        empty_label1.config(text=name)
        empty_label2.config(text=rank)
        empty_label3.config(text=dob)
        empty_label4.config(text=height)
        empty_label5.config(text=weight)
        empty_label6.config(text=batting_bowling)
        empty_label7.config(text=age)
        empty_label8.config(text=teams)
        image = Image.open(io.BytesIO(image_path))
        image = image.resize((200, 200))  # Adjust the size as needed
        photo = ImageTk.PhotoImage(image)


        # Clear any existing widgets inside the frame
        for widget in ame_label.winfo_children():
            widget.destroy()

        # Create a label and display the image
        image_label = tk.Label(ame_label, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack()
        einl.config(text=innings)
        eavg.config(text=average)
        ehs.config(text=highest_score)
        erun.config(text=runs)
        efh.config(text=fifty_hundreds)
        esr.config(text=strike_rate)
        eovers.config(text=overs)
        ewickets.config(text=wickets)
        ebest.config(text=best)
        eeconomy_rate.config(text=economy_rate)

        plot_runs_by_over_ranges(graph_frame, player_name)
        plot_runs_by_over_rangesb(graph_frame1, player_name)
    else:
        messagebox.showerror("Error", f"No data found for player {player_name}")
def fetch_player_data(player_name):
    cursor = connection.cursor()
    query = "SELECT * FROM playerperformance WHERE Name = %s"
    cursor.execute(query, (player_name,))
    player_data = cursor.fetchone()
    cursor.close()
    return player_data
def plot_runs_by_over_ranges(frame,player_name):
    # Retrieve data from the database
    cursor = connection.cursor()
    query = "SELECT 01_05r, 06_10r, 11_15r, 16_20r, 21_25r FROM playerperformance WHERE Name = %s"
    cursor.execute(query, (player_name,))
    data = cursor.fetchone()

    # Extract data into separate lists
    years = ['01-05', '06-10', '11-15', '16-20', '21-25']
    data_values = [data[i] for i in range(len(data))]

    # Plot the line graph
    fig, ax = plt.subplots()
    ax.plot(years, data_values)
    ax.set_xlabel('Over Years')
    ax.set_ylabel('Runs')
    ax.set_title('Runs scored by Over Years for player')
    ax.legend()

    # Resize the plot to fit within the frame
    fig.set_size_inches(5, 4)  # Adjust the size as needed

    # Convert the plot to a Tkinter-compatible canvas
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

def plot_runs_by_over_rangesb(frame,player_name):
    # Retrieve data from the database
    cursor = connection.cursor()
    query = "SELECT  01_05w, 06_10w, 11_15w, 16_20w, 21_25w FROM playerperformance WHERE Name = %s"
    cursor.execute(query, (player_name,))
    data = cursor.fetchone()

    # Extract data into separate lists
    years = ['01-05', '06-10', '11-15', '16-20', '21-25']
    data_values = [data[i] for i in range(len(data))]

    # Plot the line graph
    fig, ax = plt.subplots()
    ax.plot(years, data_values)
    ax.set_xlabel('Over Years')
    ax.set_ylabel('Wickets')
    ax.set_title('Wickets taken by Over Years for player')
    ax.legend()

    # Resize the plot to fit within the frame
    fig.set_size_inches(5, 4)  # Adjust the size as needed

    # Convert the plot to a Tkinter-compatible canvas
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()



#

ame_label = tk.Frame(root, width=187, height=222, bd=1, relief="solid")
ame_label.place(relx=0.10, rely=0.25, anchor='center')
# Labels for player details
# Labels with text
name_label = tk.Label(root, text="Name:", font=("Arial", 12, "bold"))
name_label.place(x=250, y=70)

rank_label = tk.Label(root, text="Rank:", font=("Arial", 12, "bold"))
rank_label.place(x=250, y=100)

dob_label = tk.Label(root, text="DOB:", font=("Arial", 12, "bold"))
dob_label.place(x=250, y=130)

height_label = tk.Label(root, text="Height:", font=("Arial", 12, "bold"))
height_label.place(x=250, y=160)

weight_label = tk.Label(root, text="Weight:", font=("Arial", 12, "bold"))
weight_label.place(x=400, y=70)

batting_bowling_label = tk.Label(root, text="Batting/Bowling:", font=("Arial", 12, "bold"))
batting_bowling_label.place(x=400, y=100)

age_label = tk.Label(root, text="Age:", font=("Arial", 12, "bold"))
age_label.place(x=400, y=130)

teams_label = tk.Label(root, text="Teams:", font=("Arial", 12, "bold"))
teams_label.place(x=400, y=160)

# Empty labels
empty_label1 = tk.Label(root, text="")
empty_label1.place(x=310, y=70)

empty_label2 = tk.Label(root, text="")
empty_label2.place(x=310, y=100)

empty_label3 = tk.Label(root, text="")
empty_label3.place(x=310, y=130)

empty_label4 = tk.Label(root, text="")
empty_label4.place(x=310, y=160)

empty_label5 = tk.Label(root, text="")
empty_label5.place(x=490, y=70)

empty_label6 = tk.Label(root, text="")
empty_label6.place(x=550, y=100)

empty_label7 = tk.Label(root, text="")
empty_label7.place(x=490, y=130)
empty_label8 = tk.Label(root, text="")
empty_label8.place(x=490, y=160)
inl = tk.Label(root, text="Innings:", font=("Arial", 11, "bold"))
inl.place(x=10, y=300)
avg = tk.Label(root, text="Average:", font=("Arial", 11, "bold"))
avg.place(x=70, y=300)
hs = tk.Label(root, text="HighestScore:", font=("Arial", 11, "bold"))
hs.place(x=135, y=300)
run = tk.Label(root, text="Runs:", font=("Arial", 11, "bold"))
run.place(x=240, y=300)
fh = tk.Label(root, text="50_100:", font=("Arial", 11, "bold"))
fh.place(x=285, y=300)
sr = tk.Label(root, text="StrikeRate:", font=("Arial", 11, "bold"))
sr.place(x=330, y=300)

# Empty labels under each horizontal label
einl = tk.Label(root, text="q")
einl.place(x=10, y=320)
eavg = tk.Label(root, text="er")
eavg.place(x=70, y=320)
ehs = tk.Label(root, text="y")
ehs.place(x=135, y=320)
erun = tk.Label(root, text="ty")
erun.place(x=240, y=320)
efh = tk.Label(root, text="e")
efh.place(x=285, y=320)
esr = tk.Label(root, text="e")
esr.place(x=330, y=320)

overs = tk.Label(root, text="Overs:", font=("Arial", 11, "bold"))
overs.place(x=680, y=300)
wickets = tk.Label(root, text="Wickets:", font=("Arial", 11, "bold"))
wickets.place(x=720, y=300)
best = tk.Label(root, text="Best:", font=("Arial", 11, "bold"))
best.place(x=795, y=300)
economy_rate = tk.Label(root, text="EconomyRate:", font=("Arial", 11, "bold"))
economy_rate.place(x=835, y=300)

# Empty labels under each horizontal label
eovers = tk.Label(root, text="ds")
eovers.place(x=700, y=320)
ewickets = tk.Label(root, text="ds")
ewickets.place(x=745, y=320)
ebest = tk.Label(root, text="dfg")
ebest.place(x=790, y=320)
eeconomy_rate = tk.Label(root, text="edr")
eeconomy_rate.place(x=835, y=320)

player_label = tk.Label(root, text="Player Performance", font="times 20 bold", foreground="blue",relief="raised",padx=10, pady=10)
player_label.pack()
graph_frame = Frame(root, width=300, height=100)
graph_frame.place(x=10,y=350)

graph_frame1 = Frame(root, width=300, height=100)
graph_frame1.place(x=630,y=350)

fetch_player_data(player_name)
display_player_details(player_name)

root.mainloop()