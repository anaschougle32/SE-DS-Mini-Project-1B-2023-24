from tkinter import *
import tkinter as tk
from tkinter import filedialog
import mysql.connector

# Establish MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1927__sid",
    database="test"
)
mycursor = mydb.cursor()


def insert_accommodation(destination, price_range, location, accommodation1_path, place1, url1, accommodation2_path, place2, url2, accommodation3_path, place3, url3):
    try:
        # MySQL query to insert data
        sql = "INSERT INTO accom (destination, pricerange, location, accomodation1, place1, url1, accomodation2, place2, url2, accomodation3, place3, url3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # Tuple containing values to be inserted
        val = (
            destination, price_range, location, accommodation1_path, place1, url1, accommodation2_path, place2, url2, accommodation3_path, place3, url3)
        # Execute the query
        mycursor.execute(sql, val)
        # Commit changes to the database
        mydb.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        # Rollback changes in case of any error
        mydb.rollback()

def create_uploadwindow(parent):
    # Setting up the window
    uploadacc_window = Toplevel(parent)
    uploadacc_window.title("Upload")
    uploadacc_window.configure(background="#111F4D")
    uploadacc_window.resizable(False, False)

    # Positioning the application

    window_width = 900
    window_height = 630

    screen_width = uploadacc_window.winfo_screenwidth()
    screen_height = uploadacc_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    uploadacc_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    # icon = PhotoImage(file='logo.png')
    # uploadacc_window.iconphoto(True, icon)

    accommodation1_paths = []
    accommodation2_paths = []
    accommodation3_paths = []

    # Setting up the font
    font_option = ('Arial', 15, 'bold')

    # Setting up the "Suggestions" label
    accomodation_label = Label(uploadacc_window,
                               text="ACCOMMODATION UPLOAD",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_option)
    accomodation_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    enter_label = Label(uploadacc_window,
                        text="Type the state name below",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_option)
    enter_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field = Entry(uploadacc_window, width=50, justify="left")
    entry_field.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    enter_label2 = Label(uploadacc_window,
                         text="Type the price range below",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_option)
    enter_label2.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field2 = Entry(uploadacc_window, width=50, justify="left")  # Define entry_field2
    entry_field2.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    enter_label2 = Label(uploadacc_window,
                         text="Enter the location",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_option)
    enter_label2.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field6 = Entry(uploadacc_window, width=50, justify="left")  # Define entry_field2
    entry_field6.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    enter_label3 = Label(uploadacc_window,
                         text="Enter the names of hotels",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_option)
    enter_label3.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field3 = Entry(uploadacc_window, width=30, justify="left")
    entry_field3.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    entry_field4 = Entry(uploadacc_window, width=30, justify="left")
    entry_field4.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field5 = Entry(uploadacc_window, width=30, justify="left")
    entry_field5.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky='ne')

    def upload1():
        try:
            # Open file dialog to select image
            filename = filedialog.askopenfilename()
            # Append the selected path to the list
            accommodation1_paths.append(filename)
        except Exception as e:
            print("Error:", e)

    def upload2():
        try:
            # Open file dialog to select image
            filename = filedialog.askopenfilename()
            # Append the selected path to the list
            accommodation2_paths.append(filename)
        except Exception as e:
            print("Error:", e)

    def upload3():
        try:
            # Open file dialog to select image
            filename = filedialog.askopenfilename()
            # Append the selected path to the list
            accommodation3_paths.append(filename)
        except Exception as e:
            print("Error:", e)

    info = Button(uploadacc_window,
                  text="Upload img 1",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#E43A19',
                  activebackground='#111F4D',
                  command=upload1,
                  font=font_option
                  )
    info.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    info2 = Button(uploadacc_window,
                   text="Upload img 2",
                   foreground='#f7f7f7',
                   background='#D24545',
                   activeforeground='#E43A19',
                   activebackground='#111F4D',
                   command=upload2,
                   font=font_option
                   )
    info2.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    info3 = Button(uploadacc_window,
                   text="Upload img 3",
                   foreground='#f7f7f7',
                   background='#D24545',
                   activeforeground='#E43A19',
                   activebackground='#111F4D',
                   command=upload3,
                   font=font_option
                   )
    info3.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky='ne')

    enter_label3 = Label(uploadacc_window,
                         text="Enter the url of hotels",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_option)
    enter_label3.grid(row=10, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field7 = Entry(uploadacc_window, width=30, justify="left")
    entry_field7.grid(row=11, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    entry_field8 = Entry(uploadacc_window, width=30, justify="left")
    entry_field8.grid(row=11, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field9 = Entry(uploadacc_window, width=30, justify="left")
    entry_field9.grid(row=11, column=0, columnspan=3, padx=10, pady=10, sticky='ne')

    def save_data():
        try:
            # Get the destination and price range from entry fields
            destination = entry_field.get()
            price_range = entry_field2.get()

            # Get the location from entry field
            location = entry_field6.get()

            # Get the values of place1, place2, place3 from entry fields
            place1 = entry_field3.get()
            place2 = entry_field4.get()
            place3 = entry_field5.get()

            # Get the values of URL1, URL2, URL3 from entry fields
            url1 = entry_field7.get()
            url2 = entry_field8.get()
            url3 = entry_field9.get()

            # Insert data into the database
            insert_accommodation(destination, price_range, location, accommodation1_paths[0], place1, url1,
                                 accommodation2_paths[0], place2, url2, accommodation3_paths[0], place3, url3)

            # Clear entry fields and image path lists
            entry_field.delete(0, tk.END)
            entry_field2.delete(0, tk.END)
            entry_field3.delete(0, tk.END)
            entry_field4.delete(0, tk.END)
            entry_field5.delete(0, tk.END)
            entry_field6.delete(0, tk.END)
            entry_field7.delete(0, tk.END)
            entry_field8.delete(0, tk.END)
            entry_field9.delete(0, tk.END)
            accommodation1_paths.clear()
            accommodation2_paths.clear()
            accommodation3_paths.clear()

            print("Data saved successfully!")
        except Exception as e:
            print("Error:", e)

    save_button = Button(uploadacc_window,
                         text="Save Data",
                         foreground='#f7f7f7',
                         background='#D24545',
                         activeforeground='#E43A19',
                         activebackground='#111F4D',
                         command=save_data,
                         font=font_option
                         )
    save_button.grid(row=12, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Configure column sizes
    uploadacc_window.grid_columnconfigure(0, weight=1, uniform="group1")
    uploadacc_window.grid_columnconfigure(1, weight=1, uniform="group1")
    uploadacc_window.grid_columnconfigure(2, weight=1, uniform="group1")

    uploadacc_window.grid_rowconfigure(2, weight=0)
    uploadacc_window.grid_rowconfigure(3, weight=0)
    uploadacc_window.grid_rowconfigure(4, weight=0)
    uploadacc_window.grid_rowconfigure(5, weight=0)
    uploadacc_window.grid_rowconfigure(6, weight=0)
    uploadacc_window.grid_rowconfigure(7, weight=0)
    uploadacc_window.grid_rowconfigure(8, weight=0)
    uploadacc_window.grid_rowconfigure(9, weight=0)
    uploadacc_window.grid_rowconfigure(10, weight=0)
    uploadacc_window.grid_rowconfigure(11, weight=0)
    uploadacc_window.grid_rowconfigure(12, weight=0)


if __name__ == "__main__":
    window = Tk()
    create_uploadwindow(window)
    window.mainloop()
