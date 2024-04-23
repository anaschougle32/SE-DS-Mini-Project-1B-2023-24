from tkinter import *
from hotelinfo import create_hotel


def create_accomodationwindow(parent):
    # Setting up the window
    accomodation_window = Toplevel(parent)
    accomodation_window.title("Accommodation")
    accomodation_window.configure(background="#111F4D")
    accomodation_window.resizable(False, False)

    # Positioning the application

    window_width = 900
    window_height = 630

    screen_width = accomodation_window.winfo_screenwidth()
    screen_height = accomodation_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    accomodation_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='../logo.png')
    accomodation_window.iconphoto(True, icon)

    # Setting up the font
    font_suggestions = ('Arial', 30, 'italic')
    font_nearbyinfo = ('Arial', 15, 'bold')
    font_button = ('Arial', 15, 'bold')
    font_option = ('Arial', 10, 'bold')
    font_view = ('Arial', 10, 'bold')

    # Setting up the "Suggestions" label
    accomodation_label = Label(accomodation_window,
                               text="ACCOMMODATION",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_suggestions)
    accomodation_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the label for "Here are some nearby places"
    enter_label = Label(accomodation_window,
                        text="Search for accommodations below",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_nearbyinfo)
    enter_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the back button

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(accomodation_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(accomodation_window, parent),
                  font=font_button
                  )
    Back.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    # Setting up the search bar
    # Setting up the text field for the age field
    entry_field = Entry(accomodation_window,
                        width=50,
                        justify="left",
                        # anchor="w"
                        )
    entry_field.grid(row=2, columnspan=4, padx=10, pady=10)

    # Setting up the price range radio button

    def on_radio_change():
        # Function to handle changes in the radio button selection
        # selected_option = radio_var.get()
        # print("Selected option:", selected_option)
        pass

    label = Label(accomodation_window,
                  text="Select a price option:",
                  fg='#f7f7f7',
                  bg='#111F4D',
                  font=font_option
                  )
    label.grid(row=3, columnspan=4, padx=10, pady=10)

    # Create a variable to store the selected option
    radio_var = StringVar()

    # Create radio buttons
    radio1 = Radiobutton(accomodation_window,
                         text="Low",
                         variable=radio_var,
                         value="Low",
                         command=on_radio_change)
    radio1.grid(row=4, columnspan=4, padx=(250, 10), pady=10, sticky='w')

    radio2 = Radiobutton(accomodation_window,
                         text="Medium",
                         variable=radio_var,
                         value="Medium",
                         command=on_radio_change)
    radio2.grid(row=4, columnspan=4, padx=10, pady=10)

    radio3 = Radiobutton(accomodation_window,
                         text="High",
                         variable=radio_var,
                         value="High",
                         command=on_radio_change)
    radio3.grid(row=4, columnspan=4, padx=(10, 250), pady=10, sticky='ne')

    # Setting up the labels for suggested accomodations
    # Row 1 - Using grid manager
    frame1 = Frame(accomodation_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame1.grid(row=7, column=0, padx=10, pady=10)

    left_image = PhotoImage(file='../hotel.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(padx=45, pady=45)

    check_button = Checkbutton(frame1,
                               text="KRSNA PALACE",
                               # variable=x,
                               onvalue=1,
                               offvalue=0,
                               # command=display,
                               font=('Arial', 10),
                               fg='#f7f7f7',
                               bg="#3652AD",
                               activeforeground='#00FF00',
                               activebackground='black'
                               )
    check_button.pack()

    def feature_view():
        accomodation_window.withdraw()  # Hide the main window
        hotelinfo_window = create_hotel(accomodation_window)
        if hotelinfo_window:
            hotelinfo_window.protocol("WM_DELETE_WINDOW",
                                      lambda: close_windows(window, hotelinfo_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    info = Button(frame1,
                  text="View",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#E43A19',
                  activebackground='#111F4D',
                  command=feature_view,
                  font=font_view
                  )
    info.pack()

    frame2 = Frame(accomodation_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame2.grid(row=7, column=1, padx=10, pady=10)

    center_image = PhotoImage(file='../hotel.png')
    center_image_label = Label(frame2,
                               image=center_image,
                               bg="#3652AD")
    center_image_label.image = center_image
    center_image_label.pack(padx=45, pady=45)

    check_button = Checkbutton(frame2,
                               text="Raftaar's Retreat",
                               # variable=x,
                               onvalue=1,
                               offvalue=0,
                               # command=display,
                               font=('Arial', 10),
                               fg='#f7f7f7',
                               bg="#3652AD",
                               activeforeground='#00FF00',
                               activebackground='black'
                               )
    check_button.pack()

    info = Button(frame2,
                  text="View",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#E43A19',
                  activebackground='#111F4D',
                  command=feature_view,
                  font=font_view
                  )
    info.pack()

    frame3 = Frame(accomodation_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame3.grid(row=7, column=2, padx=10, pady=10)

    # Adding image to the frame
    right_image = PhotoImage(file='../hotel.png')
    right_image_label = Label(frame3,
                              image=right_image,
                              bg="#3652AD")
    right_image_label.image = right_image  # Keep a reference to the image
    right_image_label.pack(padx=45, pady=45)

    check_button = Checkbutton(frame3,
                               text="Divine's Dorm",
                               # variable=x,
                               onvalue=1,
                               offvalue=0,
                               # command=display,
                               font=('Arial', 10),
                               fg='#f7f7f7',
                               bg="#3652AD",
                               activeforeground='#00FF00',
                               activebackground='black'
                               )
    check_button.pack()

    info = Button(frame3,
                  text="View",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#E43A19',
                  activebackground='#111F4D',
                  command=feature_view,
                  font=font_view
                  )
    info.pack()

    # Setting up the next page button



    # Configure column sizes
    accomodation_window.grid_columnconfigure(0, weight=1, uniform="group1")
    accomodation_window.grid_columnconfigure(1, weight=1, uniform="group1")
    accomodation_window.grid_columnconfigure(2, weight=1, uniform="group1")

    accomodation_window.grid_rowconfigure(2, weight=0)
    accomodation_window.grid_rowconfigure(3, weight=0)
    accomodation_window.grid_rowconfigure(4, weight=0)
    accomodation_window.grid_rowconfigure(5, weight=0)
    accomodation_window.grid_rowconfigure(6, weight=0)
    accomodation_window.grid_rowconfigure(7, weight=0)


if __name__ == "__main__":
    window = Tk()
    create_accomodationwindow(window)
    window.mainloop()
