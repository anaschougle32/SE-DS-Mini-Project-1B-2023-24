from tkinter import *
import mysql.connector

root = Tk()
root.title('Search')
root.geometry("500x300")

def update(data):
    my_list.delete(0, END)

    for item in data:
        my_list.insert(END, item)

def fillout(e):
    my_entry.delete(0, END)
    my_entry.insert(0, my_list.get(ACTIVE))

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

# Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parthavi@1204",
    database="cricpulse"
)

# Create a cursor
c = conn.cursor()

# Execute a query to fetch data from the database
c.execute("SELECT name FROM playerperformance")
records = c.fetchall()

# Extract names from fetched records
names = [record[0] for record in records]

# Close the cursor and database connection
c.close()
conn.close()

my_label = Label(root, text="Start Typing", font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

my_list = Listbox(root, width=50)
my_list.pack(pady=40)

update(names)

my_list.bind("<<ListboxSelect>>", fillout)

my_entry.bind("<KeyRelease>", check)
root.mainloop()
