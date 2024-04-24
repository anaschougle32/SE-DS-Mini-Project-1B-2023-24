from tkinter import *


def create_finaliternarywindow(parent):
    # Setting up the window
    iternary_window = Toplevel(parent)
    iternary_window.title("Your Itenary")
    iternary_window.configure(background="#111F4D")
    iternary_window.resizable(False, False)

    # Positioning the application

    window_width = 900
    window_height = 630

    screen_width = iternary_window.winfo_screenwidth()
    screen_height = iternary_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    iternary_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    iternary_window.iconphoto(True, icon)

    # Setting up the font
    font_iternary = ('Arial', 30, 'italic')
    font_nearbyinfo = ('Arial', 15, 'bold')
    font_sublabels = ('Arial', 12, 'bold')
    font_button = ('Arial', 12, 'bold')

    # Setting up the "Suggestions" label
    itenary_label = Label(iternary_window,
                          text=" Your Itenary",
                          fg='#f7f7f7',
                          bg='#111F4D',
                          font=font_iternary)
    itenary_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the "from" label
    from_label = Label(iternary_window,
                       text="From",
                       fg='#f7f7f7',
                       bg='#111F4D',
                       font=font_nearbyinfo)
    from_label.grid(row=1, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=2, column=0, padx=20, pady=10, sticky='w')

    # Setting up the "to" label
    to_label = Label(iternary_window,
                     text="To",
                     fg='#f7f7f7',
                     bg='#111F4D',
                     font=font_nearbyinfo)
    to_label.grid(row=1, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='n')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=2, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='n')

    # Setting up the "accomodation" label

    # Setting up the "trip details" label
    tripdetails_label = Label(iternary_window,
                              text="Trip details",
                              fg='#f7f7f7',
                              bg='#111F4D',
                              font=font_nearbyinfo)
    tripdetails_label.grid(row=3, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    type_of_trip_label = Label(iternary_window,
                               text="Type of trip",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_sublabels)
    type_of_trip_label.grid(row=4, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=4, column=0, columnspan=3, padx=(130, 0), pady=10, sticky='w')

    no_of_people_label = Label(iternary_window,
                               text="No of people",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_sublabels)
    no_of_people_label.grid(row=4, column=0, columnspan=3, padx=(0, 220), pady=10, sticky='n')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=4, column=0, columnspan=3, padx=(110, 0), pady=10, sticky='n')

    no_of_people_label = Label(iternary_window,
                               text="No of days",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_sublabels)
    no_of_people_label.grid(row=4, column=0, columnspan=3, padx=(0, 220), pady=10, sticky='ne')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=4, column=0, columnspan=3, padx=(130, 40), pady=10, sticky='ne')

    specific_destination_label = Label(iternary_window,
                                       text="Specific Destination",
                                       fg='#f7f7f7',
                                       bg='#111F4D',
                                       font=font_sublabels)
    specific_destination_label.grid(row=5, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=5, column=0, columnspan=3, padx=(190, 0), pady=10, sticky='w')

    # Days configuration label and sublabel
    day1_label = Label(iternary_window,
                                       text="Day 1",
                                       fg='#f7f7f7',
                                       bg='#111F4D',
                                       font=font_nearbyinfo)
    day1_label.grid(row=6, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=7, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame2 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame2.grid(row=7, column=0, columnspan=3, padx=(200, 0), pady=10, sticky='w')

    frame3 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame3.grid(row=7, column=0, columnspan=3, padx=(400, 0), pady=10, sticky='w')

    day2_label = Label(iternary_window,
                       text="Day 2",
                       fg='#f7f7f7',
                       bg='#111F4D',
                       font=font_nearbyinfo)
    day2_label.grid(row=8, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=9, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame2 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame2.grid(row=9, column=0, columnspan=3, padx=(200, 0), pady=10, sticky='w')

    frame3 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame3.grid(row=9, column=0, columnspan=3, padx=(400, 0), pady=10, sticky='w')

    day3_label = Label(iternary_window,
                       text="Day 3",
                       fg='#f7f7f7',
                       bg='#111F4D',
                       font=font_nearbyinfo)
    day3_label.grid(row=10, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame1 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame1.grid(row=11, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='w')

    frame2 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame2.grid(row=11, column=0, columnspan=3, padx=(200, 0), pady=10, sticky='w')

    frame3 = Frame(iternary_window,
                   width=150,
                   height=30,
                   bg="#3652AD")
    frame3.grid(row=11, column=0, columnspan=3, padx=(400, 0), pady=10, sticky='w')

    #setting up the back button
    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(iternary_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(iternary_window, parent),
                  font=font_button
                  )
    Back.grid(row=11, column=0, columnspan=3, padx=10, pady=10, sticky='ne')

    # Configure column sizes
    iternary_window.grid_columnconfigure(0, weight=1, uniform="group1")
    iternary_window.grid_columnconfigure(1, weight=0, uniform="group1")
    iternary_window.grid_columnconfigure(2, weight=0, uniform="group1")

    iternary_window.grid_rowconfigure(2, weight=0)
    iternary_window.grid_rowconfigure(3, weight=0)
    iternary_window.grid_rowconfigure(4, weight=0)
    iternary_window.grid_rowconfigure(5, weight=0)
    iternary_window.grid_rowconfigure(6, weight=0)
    iternary_window.grid_rowconfigure(7, weight=0)
    iternary_window.grid_rowconfigure(8, weight=0)
    iternary_window.grid_rowconfigure(9, weight=0)
    iternary_window.grid_rowconfigure(10, weight=0)
    iternary_window.grid_rowconfigure(11, weight=0)

if __name__ == "__main__":
    window = Tk()
    create_finaliternarywindow(window)
    window.mainloop()
