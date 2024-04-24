from tkinter import *
import tkinter as tk
import tkintermapview
from usertripdetails import create_tripdetailswindow


def create_mainwindow(parent):
    main_window = Toplevel(parent)
    # main_window.geometry("1000x600")
    main_window.title("Select your destination")
    main_window.configure(background="#111F4D")

    # Positioning the application

    window_width = 900
    window_height = 700

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    main_window.iconphoto(True, icon)

    # Setting up the font
    font_info1 = ('Arial', 30, 'italic')
    font_button = ('Arial', 10, 'bold')
    font_from = ('Arial', 20, 'bold')
    font_to = ('Arial', 20, 'bold')
    font_map_view_button = ('Arial', 10, 'bold')

    # Setting up the first info label stating 'Enter your destination'
    info1_label = Label(main_window,
                        text="Enter your destination",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_info1)
    info1_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    from_label = Label(main_window,
                       text="From",
                       fg='#f7f7f7',
                       bg='#111F4D',
                       font=font_from)
    from_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Drop down menu for "From"

    def on_dropdown_change(value):
        # Function to handle changes in the dropdown selection
        # print("Selected:", value)
        pass

    selected_value = tk.StringVar(main_window)

    # Define options for the dropdown menu
    options = ["Maharashtra",
               "Delhi",
               "Goa",
               "Karnataka"
               ]

    # Create the dropdown menu
    dropdown_menu = tk.OptionMenu(main_window,
                                  selected_value,
                                  *options,
                                  command=on_dropdown_change)
    selected_value.set(options[0])  # Set default value

    # Configure the width of the dropdown menu
    dropdown_menu.config(width=50)

    # Pack the dropdown menu
    dropdown_menu.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the label for "to"

    to_label = Label(main_window,
                     text="To",
                     fg='#f7f7f7',
                     bg='#111F4D',
                     font=font_to)
    to_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Drop down menu for "to"

    def on_dropdown_change(value):
        # Function to handle changes in the dropdown selection
        # print("Selected:", value)
        pass

    selected_value = tk.StringVar(main_window)

    # Define options for the dropdown menu
    options = ["Karnataka",
               "Delhi",
               "Goa",
               "Maharashtra"
               ]

    # Create the dropdown menu
    dropdown_menu = tk.OptionMenu(main_window,
                                  selected_value,
                                  *options,
                                  command=on_dropdown_change)
    selected_value.set(options[0])  # Set default value

    # Configure the width of the dropdown menu
    dropdown_menu.config(width=50)

    # Pack the dropdown menu
    dropdown_menu.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the label for "to"

    suggestedplaces_label = Label(main_window,
                                  text="Suggested Destinations",
                                  fg='#f7f7f7',
                                  bg='#111F4D',
                                  font=font_to)
    suggestedplaces_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Suggested destination
    # Row 1 - Using grid manager
    frame1 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame1.grid(row=6, column=0, padx=10, pady=10)

    left_image = PhotoImage(file='mumbai.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(padx=45, pady=45)

    def open_mumbaimap_window():
        # mumbai_window = tk.Toplevel(window)
        # mumbai_window.title("Mumbai Map")
        mapwidget = tkintermapview.TkinterMapView(tk.Toplevel(main_window), width=420, height=400, corner_radius=0)
        mapwidget.pack()

        # Create a map widget for Mumbai
        marker_1 = mapwidget.set_address("maharashtra, india", marker=True)
        marker_1.set_text("Maharashtra")

    map_view_button = Button(frame1,
                             text="View",
                             foreground='#f7f7f7',
                             background='#D24545',
                             activeforeground='#E43A19',
                             activebackground='#111F4D',
                             command=open_mumbaimap_window,
                             font=font_map_view_button)
    map_view_button.pack()

    check_button = Checkbutton(frame1,
                               text="Mumbai",
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

    frame2 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame2.grid(row=6, column=1, padx=10, pady=10)

    center_image = PhotoImage(file='karnataka.png')
    center_image_label = Label(frame2,
                               image=center_image,
                               bg="#3652AD")
    center_image_label.image = center_image
    center_image_label.pack(padx=45, pady=45)

    def open_karnatakamap_window():
        # mumbai_window = tk.Toplevel(window)
        # mumbai_window.title("Mumbai Map")
        mapwidget = tkintermapview.TkinterMapView(tk.Toplevel(main_window), width=420, height=400, corner_radius=0)
        mapwidget.pack()

        # Create a map widget for Mumbai
        marker_1 = mapwidget.set_address("karnataka, india", marker=True)
        marker_1.set_text("Karnataka")

    map_view_button = Button(frame2,
                             text="View",
                             foreground='#f7f7f7',
                             background='#D24545',
                             activeforeground='#E43A19',
                             activebackground='#111F4D',
                             command=open_karnatakamap_window,
                             font=font_map_view_button)
    map_view_button.pack()

    check_button = Checkbutton(frame2,
                               text="Karnataka",
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

    frame3 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame3.grid(row=6, column=2, padx=10, pady=10)

    # Adding image to the frame
    right_image = PhotoImage(file='delhi.png')
    right_image_label = Label(frame3,
                              image=right_image,
                              bg="#3652AD")
    right_image_label.image = right_image  # Keep a reference to the image
    right_image_label.pack(padx=45, pady=45)

    def open_delhimap_window():
        # mumbai_window = tk.Toplevel(window)
        # mumbai_window.title("Mumbai Map")
        mapwidget = tkintermapview.TkinterMapView(tk.Toplevel(main_window), width=420, height=400, corner_radius=0)
        mapwidget.pack()

        # Create a map widget for Mumbai
        marker_1 = mapwidget.set_address("delhi, india", marker=True)
        marker_1.set_text("Delhi")

    map_view_button = Button(frame3,
                             text="View",
                             foreground='#f7f7f7',
                             background='#D24545',
                             activeforeground='#E43A19',
                             activebackground='#111F4D',
                             command=open_delhimap_window,
                             font=font_map_view_button)
    map_view_button.pack()

    check_button = Checkbutton(frame3,
                               text="Delhi",
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

    # Setting up the button to enter a new window

    def feature_suggestion_window():
        main_window.withdraw()  # Hide the main window
        usertripdetails_window = create_tripdetailswindow(main_window)
        if usertripdetails_window:
            usertripdetails_window.protocol("WM_DELETE_WINDOW",
                                            lambda: close_windows(main_window, usertripdetails_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    Plantrip = Button(main_window,
                      text="Visit",
                      foreground='#f7f7f7',
                      background='#D24545',
                      activeforeground='#E43A19',
                      activebackground='#111F4D',
                      command=feature_suggestion_window,
                      font=font_button
                      )
    Plantrip.grid(row=1, columnspan=4, padx=(0, 50), pady=10, sticky='ne')

    # Setting up the back button
    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(main_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(main_window, parent),
                  # command=back,
                  font=font_button
                  )
    Back.grid(row=1, columnspan=4, padx=(10, 40), pady=10, sticky='sw')

    # Configure column sizes
    main_window.grid_columnconfigure(0, weight=1, uniform="group1")
    main_window.grid_columnconfigure(1, weight=1, uniform="group1")
    main_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    main_window.grid_rowconfigure(2, weight=0)
    main_window.grid_rowconfigure(3, weight=0)
    main_window.grid_rowconfigure(4, weight=0)
    main_window.grid_rowconfigure(5, weight=0)
    main_window.grid_rowconfigure(6, weight=0)
    main_window.grid_rowconfigure(7, weight=0)


if __name__ == "__main__":
    window = Tk()
    create_mainwindow(window)
    window.mainloop()
