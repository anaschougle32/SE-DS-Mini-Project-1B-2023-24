from tkinter import *
import tkinter as tk
from loginsignupbutton import create_loginsignup_window

# Setting Up the app
window = Tk()
# window.geometry("420x400")
window.title("TRIP PLANNER")
window.configure(background="#111F4D")
window_width = 420
window_height = 400

# source :- https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# window.eval('tk::PlaceWindow . center')


# Setting up the icon for the window
# icon = PhotoImage(file='logo.png')
# window.iconphoto(True, icon)

# Setting up the font
font_tripplanner = ('Arial', 30, 'bold')
font_welcome = ("Arial", 10, "bold")
font_info = ("Arial", 10, "bold")
font_button = ("Arial", 10, "bold")

photo = PhotoImage(file='logo2.png')
trip_planner_label = Label(window,
                           text="TRIP PLANNER",
                           font=font_tripplanner,
                           fg='#f7f7f7',
                           bg='#111F4D',
                           image=photo,  # replaces the text with image label
                           compound='top')
trip_planner_label.pack(padx=10, pady=20)

welcome_label = Label(window,
                      text="Welcome,",
                      font=font_welcome,
                      fg='#f7f7f7',
                      bg='#111F4D', )

welcome_label.pack(padx=5, pady=5)

# Setting up the Label For information
infoLabel = tk.Label(window,
                     text="Your go-to companion for efficient tour planning",
                     fg='#f7f7f7',
                     bg='#111F4D',
                     font=font_info)
infoLabel.pack()

infoLabel2 = tk.Label(window,
                      text="Start crafting unforgettable journeys with ease and precision.",
                      fg='#f7f7f7',
                      bg='#111F4D',
                      font=font_info)
infoLabel2.pack()


# Source :- YouTube

def feature_display_window():
    window.withdraw()  # Hide the main window
    loginsignup_window = create_loginsignup_window(window)
    loginsignup_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(window, loginsignup_window))


def close_windows(main_window, popup_window):
    popup_window.destroy()
    main_window.destroy()


# Setting up the entry button

Entry = Button(window,
               text="Start Planning",
               foreground='#f7f7f7',
               background='#D24545',
               activeforeground='#E43A19',
               activebackground='#111F4D',
               command=feature_display_window,
               font=font_button
               )
Entry.pack(padx=10, pady=20)

window.mainloop()
