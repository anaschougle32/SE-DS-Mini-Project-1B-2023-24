import tkinter as tk
from tkinter import Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector

# Connect to the database
# Make sure to replace the connection details with your own
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Parthavi@1204',
    database='cricpulse'
)

def plot_runs_by_over_ranges(frame):
    # Retrieve data from the database
    cursor = connection.cursor()
    query = "SELECT 01_05r, 06_10r, 11_15r, 16_20r, 21_25r FROM playerperformance WHERE Name = %s"
    cursor.execute(query, ('gdkd',))
    data = cursor.fetchone()

    # Extract data into separate lists
    years = ['01_05r', '06_10r', '11_15r', '16_20r', '21_25r']
    data_values = [data[i] for i in range(len(data))]

    # Plot the line graph
    fig, ax = plt.subplots()
    ax.plot(years, data_values)
    ax.set_xlabel('Over Ranges')
    ax.set_ylabel('Runs')
    ax.set_title('Runs scored by Over Ranges for player gdkd')
    ax.legend()

    # Convert the plot to a Tkinter-compatible canvas
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

if __name__ == "__main__":
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Graph Display")

    # Create a frame to contain the plot
    graph_frame = Frame(root, width=800, height=500)
    graph_frame.pack()

    # Call the function to plot the graph
    plot_runs_by_over_ranges(graph_frame)

    # Start the Tkinter event loop
    root.mainloop()
