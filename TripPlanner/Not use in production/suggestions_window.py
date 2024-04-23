from tkinter import *
import tkinter as tk
import tkintermapview
from accomodation_window import create_accomodationwindow


def create_suggestionwindow(parent):
    # Setting up the window
    suggestions_window = Toplevel(parent)
    suggestions_window.title("Suggestions")
    suggestions_window.configure(background="#111F4D")
    suggestions_window.resizable(False, False)

    # Positioning the application
    window_width = 900
    window_height = 630
    screen_width = suggestions_window.winfo_screenwidth()
    screen_height = suggestions_window.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    suggestions_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='../logo.png')
    suggestions_window.iconphoto(True, icon)

    # Setting up the font
    font_suggestions = ('Arial', 30, 'italic')
    font_nearbyinfo = ('Arial', 15, 'bold')
    font_button = ('Arial', 15, 'bold')
    font_accomodation_button = ('Arial', 15, 'bold')
    font_map_view_button = ('Arial', 6, 'bold')
    font_add_button = ('Arial', 10, 'bold')

    # Setting up the "Suggestions" label
    suggestions_label = Label(suggestions_window,
                              text="SUGGESTIONS FOR PLACES",
                              fg='#f7f7f7',
                              bg='#111F4D',
                              font=font_suggestions)
    suggestions_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the label for "Here are some nearby places"
    # nearbyinfo_label = Label(suggestions_window,
    #                          text="Here are some nearby places you can visit",
    #                          fg='#f7f7f7',
    #                          bg='#111F4D',
    #                          font=font_nearbyinfo)
    # nearbyinfo_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the back button

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(suggestions_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(suggestions_window, parent),
                  font=font_button
                  )
    Back.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='w')

    def on_dropdown_change(value):
        # Function to handle changes in the dropdown selection
        # print("Selected:", value)
        pass

    selected_value = tk.StringVar(suggestions_window)

    # Define options for the dropdown menu
    options = ["Maharashtra",
               "Delhi",
               "Goa",
               "Karnataka"
               ]

    # Create the dropdown menu
    dropdown_menu = tk.OptionMenu(suggestions_window,
                                  selected_value,
                                  *options,
                                  command=on_dropdown_change)
    selected_value.set(options[0])  # Set default value

    # Configure the width of the dropdown menu
    dropdown_menu.config(width=50)

    # Pack the dropdown menu
    dropdown_menu.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    def feature_add():
        pass

    add = Button(suggestions_window,
                 text="Suggest",
                 foreground='#f7f7f7',
                 background='#D24545',
                 activeforeground='#E43A19',
                 activebackground='#111F4D',
                 command=feature_add,
                 font=font_accomodation_button
                 )
    add.grid(row=2, columnspan=3, padx=10, pady=10, sticky='n')
    # Row 1 - Using grid manager
    frame1 = Frame(suggestions_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame1.grid(row=4, column=0, padx=10, pady=15)

    left_image = PhotoImage(file='../location.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(padx=35, pady=25)

    check_button = Checkbutton(frame1,
                               text="Marine Drive",
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

    frame2 = Frame(suggestions_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame2.grid(row=4, column=1, padx=10, pady=15)

    center_image = PhotoImage(file='../location.png')
    center_image_label = Label(frame2,
                               image=center_image,
                               bg="#3652AD")
    center_image_label.image = center_image
    center_image_label.pack(padx=35, pady=25)

    check_button = Checkbutton(frame2,
                               text="Sinhagad Fort",
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

    frame3 = Frame(suggestions_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame3.grid(row=4, column=2, padx=10, pady=15)

    # Adding image to the frame
    right_image = PhotoImage(file='../location.png')
    right_image_label = Label(frame3,
                              image=right_image,
                              bg="#3652AD")
    right_image_label.image = right_image  # Keep a reference to the image
    right_image_label.pack(padx=35, pady=25)

    check_button = Checkbutton(frame3,
                               text="Ajanta and Ellora Caves",
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

    # Row 2 - Using grid manager
    frame4 = Frame(suggestions_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame4.grid(row=5, column=0, padx=10, pady=15)

    left_image = PhotoImage(file='../location.png')
    left_image_label = Label(frame4,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(padx=35, pady=25)

    check_button = Checkbutton(frame4,
                               text="Trimbakeshwar Temple",
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

    frame5 = Frame(suggestions_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame5.grid(row=5, column=1, padx=10, pady=15)

    center_image = PhotoImage(file='../location.png')
    center_image_label = Label(frame5,
                               image=center_image,
                               bg="#3652AD")
    center_image_label.image = center_image
    center_image_label.pack(padx=35, pady=25)

    # def open_mumbaimap_window():
    #     # mumbai_window = tk.Toplevel(window)
    #     # mumbai_window.title("Mumbai Map")
    #     mapwidget = tkintermapview.TkinterMapView(tk.Toplevel(suggestions_window), width=420, height=400, corner_radius=0)
    #     mapwidget.pack()
    #
    #     # Create a map widget for Mumbai
    #     marker_1 = mapwidget.set_address("maharashtra, india", marker=True)
    #     marker_1.set_text("Maharashtra")
    #
    # map_view_button = Button(frame5,
    #                          text="View",
    #                          foreground='#f7f7f7',
    #                          background='#D24545',
    #                          activeforeground='#E43A19',
    #                          activebackground='#111F4D',
    #                          command=open_mumbaimap_window,
    #                          font=font_map_view_button)
    # map_view_button.pack(pady=5)

    check_button = Checkbutton(frame5,
                               text="Karla Caves",
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

    frame6 = Frame(suggestions_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame6.grid(row=5, column=2, padx=10, pady=15)

    # Adding image to the frame
    right_image = PhotoImage(file='../location.png')
    right_image_label = Label(frame6,
                              image=right_image,
                              bg="#3652AD")
    right_image_label.image = right_image  # Keep a reference to the image
    right_image_label.pack(padx=35, pady=25)

    check_button = Checkbutton(frame6,
                               text="Venna Lake",
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

    # Label below row 2 - Using grid manager
    # info2_label = Label(suggestions_window,
    #                     text="Or enter the place you wanna visit :- ",
    #                     fg='#f7f7f7',
    #                     bg='#111F4D',
    #                     font=('Arial', 12))
    # info2_label.grid(row=4, columnspan=4, padx=10, pady=10, sticky='w')

    # Setting up the text field for the age field
    # entry_field = Entry(suggestions_window,
    #                     width=50,
    #                     justify="left",
    #                     # anchor="w"
    #                     )
    # entry_field.grid(row=4, columnspan=4, padx=(50, 0), pady=10)

    # def feature_add():
    #     pass
    #
    #     add = Button(suggestions_window,
    #                  text="Suggest",
    #                  foreground='#f7f7f7',
    #                  background='#D24545',
    #                  activeforeground='#E43A19',
    #                  activebackground='#111F4D',
    #                  command=feature_add,
    #                  font=font_add_button
    #                  )
    #     add.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='ne')

    # def feature_accomodationwindow():
    #     suggestions_window.withdraw()  # Hide the main window
    #     accomodationfeature_window = create_accomodationwindow(suggestions_window)
    #     if accomodationfeature_window:
    #         accomodationfeature_window.protocol("WM_DELETE_WINDOW",
    #                                             lambda: close_windows(window, accomodationfeature_window))
    #
    # def close_windows(main_window, popup_window):
    #     popup_window.destroy()
    #     main_window.destroy()
    #
    # next = Button(suggestions_window,
    #               text="Next",
    #               foreground='#f7f7f7',
    #               background='#D24545',
    #               activeforeground='#E43A19',
    #               activebackground='#111F4D',
    #               command=feature_accomodationwindow,
    #               font=font_accomodation_button
    #               )
    # next.grid(row=4, columnspan=4, padx=(0, 50), pady=10, sticky='se')

    # Configure column sizes
    suggestions_window.grid_columnconfigure(0, weight=1, uniform="group1")
    suggestions_window.grid_columnconfigure(1, weight=1, uniform="group1")
    suggestions_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    suggestions_window.grid_rowconfigure(2, weight=1)
    suggestions_window.grid_rowconfigure(3, weight=1)
    suggestions_window.grid_rowconfigure(4, weight=1)
    suggestions_window.grid_rowconfigure(5, weight=1)

    suggestions_window.mainloop()


if __name__ == "__main__":
    window = Tk()
    create_suggestionwindow(window)
    window.mainloop()
