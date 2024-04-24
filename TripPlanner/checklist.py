from tkinter import *
from tkinter import messagebox, simpledialog
import mysql.connector


def add_item():
    item = simpledialog.askstring("Add Item", "Enter item to add:")
    if item:
        listbox.insert(END, item)
        save_checklist_to_database()


def remove_item():
    selected_indices = listbox.curselection()
    if selected_indices:
        listbox.delete(selected_indices[0])
        save_checklist_to_database()


def modify_item():
    selected_indices = listbox.curselection()
    if selected_indices:
        index = selected_indices[0]
        new_item = simpledialog.askstring("Modify Item", "Enter new item:", initialvalue=listbox.get(index))
        if new_item:
            listbox.delete(index)
            listbox.insert(index, new_item)
            save_checklist_to_database()


def save_checklist_to_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1927__sid",
        database="test"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM checklist")
    items = listbox.get(0, END)
    for item in items:
        cur.execute("INSERT INTO checklist (item) VALUES (%s)", (item,))
    conn.commit()
    cur.close()
    conn.close()


def clear_list():
    listbox.delete(0, END)
    save_checklist_to_database()


def create_check(parent):
    # Setting up the window
    check_window = Toplevel(parent)
    check_window.title("checklist")
    check_window.configure(background="#111F4D")
    check_window.resizable(False, False)

    # Positioning the application
    window_width = 900
    window_height = 600
    screen_width = check_window.winfo_screenwidth()
    screen_height = check_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    check_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    check_window.iconphoto(True, icon)

    font_check = ('Arial', 30, 'italic')
    font_button = ('Arial', 15, 'bold')
    font_listbox = ('Arial', 20, 'italic')

    # Setting up the "Suggestions" label
    suggestions_label = Label(check_window,
                              text="CHECKLIST",
                              fg='#f7f7f7',
                              bg='#111F4D',
                              font=font_check)
    suggestions_label.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky='n')

    global listbox
    listbox = Listbox(check_window, width=30, height=10, font=font_listbox)
    listbox.grid(row=1, column=1, columnspan=3, padx=80, pady=10, sticky='new')

    # Function to add an item with bullet
    def add_item_with_bullet():
        item = simpledialog.askstring("Add Item", "Enter item to add:")
        if item:
            listbox.insert(END, "• " + item)  # Adding bullet
            save_checklist_to_database()

    add_button = Button(check_window, text="Add Item", foreground='#f7f7f7', background='#D24545',
                        activeforeground='#D24545',
                        activebackground='#A94438', font=font_button, command=add_item_with_bullet)
    add_button.grid(row=3, column=0, padx=5, pady=10, sticky='n')
    remove_button = Button(check_window, text="Remove Item", foreground='#f7f7f7', background='#D24545',
                           activeforeground='#D24545', activebackground='#A94438', font=font_button,
                           command=remove_item)
    remove_button.grid(row=3, column=1, padx=5, pady=10, sticky='n')

    modify_button = Button(check_window, text="Modify Item", foreground='#f7f7f7', background='#D24545',
                           activeforeground='#D24545', activebackground='#A94438', font=font_button,
                           command=modify_item)
    modify_button.grid(row=3, column=2, padx=5, pady=10, sticky='n')

    save_button = Button(check_window, text="Save", foreground='#f7f7f7', background='#D24545',
                         activeforeground='#D24545',
                         activebackground='#A94438', font=font_button, command=save_checklist_to_database)
    save_button.grid(row=3, column=3, padx=5, pady=10, sticky='n')

    clear_button = Button(check_window, text="Clear List", foreground='#f7f7f7', background='#D24545',
                          activeforeground='#D24545', activebackground='#A94438', font=font_button,
                          command=clear_list)
    clear_button.grid(row=3, column=4, padx=5, pady=10, sticky='n')

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(check_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(check_window, parent),
                  font=font_button
                  )
    Back.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    # Configure column sizes
    check_window.grid_columnconfigure(0, weight=1, uniform="group1")
    check_window.grid_columnconfigure(1, weight=1, uniform="group1")
    check_window.grid_columnconfigure(2, weight=1, uniform="group1")
    check_window.grid_columnconfigure(3, weight=1, uniform="group1")
    check_window.grid_columnconfigure(4, weight=1, uniform="group1")

    # Configure row sizes
    check_window.grid_rowconfigure(2, weight=1)
    check_window.grid_rowconfigure(3, weight=1)
    check_window.grid_rowconfigure(4, weight=1)

    check_window.mainloop()


if __name__ == "__main__":
    window = Tk()
    create_check(window)
    window.mainloop()
