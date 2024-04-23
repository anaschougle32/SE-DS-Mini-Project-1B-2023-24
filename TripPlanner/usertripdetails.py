from tkinter import *
import tkinter as tk
from finaliternary import create_finaliternarywindow


def create_tripdetailswindow(parent):
    userdetails_window = Toplevel(parent)
    # main_window.geometry("1000x600")
    userdetails_window.title("Trip Configuration")
    userdetails_window.configure(background="#111F4D")

    # Positioning the application

    window_width = 1000
    window_height = 600

    screen_width = userdetails_window.winfo_screenwidth()
    screen_height = userdetails_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    userdetails_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    userdetails_window.iconphoto(True, icon)

    # Setting up the font
    font_tripconfig = ('Arial', 30, 'italic')
    font_nearbyinfo = ('Arial', 15, 'bold')

    # Setting up the "Suggestions" label
    tripconfig_label = Label(userdetails_window,
                             text="Trip Configuration",
                             fg='#f7f7f7',
                             bg='#111F4D',
                             font=font_tripconfig)
    tripconfig_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the label for "Here are some nearby places"
    completedetails_label = Label(userdetails_window,
                                  text="Fill the details below",
                                  fg='#f7f7f7',
                                  bg='#111F4D',
                                  font=font_nearbyinfo)
    completedetails_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the label for "members"
    Members_label = Label(userdetails_window,
                          text="Select your type of trip",
                          fg='#f7f7f7',
                          bg='#111F4D',
                          font=font_nearbyinfo)
    Members_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    # Setting up the group and solo radio button

    def on_radio_change():
        # Function to handle changes in the radio button selection
        # selected_option = radio_var.get()
        # print("Selected option:", selected_option)
        pass

    # Create a variable to store the selected option
    radio_var = StringVar()

    # Create radio buttons
    radio1 = Radiobutton(userdetails_window,
                         text="Solo",
                         variable=radio_var,
                         value="solo",
                         command=on_radio_change)
    radio1.grid(row=3, columnspan=4, padx=(400, 10), pady=10, sticky='w')

    radio2 = Radiobutton(userdetails_window,
                         text="Group",
                         variable=radio_var,
                         value="group",
                         command=on_radio_change)
    radio2.grid(row=3, columnspan=4, padx=(10, 400), pady=10, sticky='ne')

    # Setting up the label for "name of trip"
    nameoftrip_label = Label(userdetails_window,
                             text="Name of trip",
                             fg='#f7f7f7',
                             bg='#111F4D',
                             font=font_nearbyinfo)
    nameoftrip_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field = Entry(userdetails_window,
                        width=50,
                        justify="left",
                        # anchor="w"
                        )
    entry_field.grid(row=5, columnspan=4, pady=10)

    # Setting up the label for "no.of.days"
    noofpoeple_label = Label(userdetails_window,
                           text="No of people",
                           fg='#f7f7f7',
                           bg='#111F4D',
                           font=font_nearbyinfo)
    noofpoeple_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field = Entry(userdetails_window,
                        width=50,
                        justify="left",
                        # anchor="w"
                        )
    entry_field.grid(row=7, columnspan=4, pady=10)

    # Setting up the label for "budget"
    budget_label = Label(userdetails_window,
                         text="No of days",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_nearbyinfo)
    budget_label.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field = Entry(userdetails_window,
                        width=50,
                        justify="left",
                        # anchor="w"
                        )
    entry_field.grid(row=9, columnspan=4, pady=10)

    # Drop down menu for "to"

    # def on_dropdown_change(value):
    #     # Function to handle changes in the dropdown selection
    #     # print("Selected:", value)
    #     pass
    #
    # selected_value = tk.StringVar(userdetails_window)
    #
    # # Define options for the dropdown menu
    # options = ["Trimbe",
    #            "Her Mind",
    #            "Her dad's account",
    #            "her best friend +"
    #            ]
    #
    # # Create the dropdown menu
    # dropdown_menu = tk.OptionMenu(userdetails_window,
    #                               selected_value,
    #                               *options,
    #                               command=on_dropdown_change)
    # selected_value.set(options[0])  # Set default value
    #
    # # Configure the width of the dropdown menu
    # dropdown_menu.config(width=50)
    #
    # # Pack the dropdown menu
    # dropdown_menu.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    def feature_accomodationwindow():
        userdetails_window.withdraw()  # Hide the main window
        iternary_window = create_finaliternarywindow(userdetails_window)
        if iternary_window:
            iternary_window.protocol("WM_DELETE_WINDOW",
                                     lambda: close_windows(window, iternary_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    next = Button(userdetails_window,
                  text="Next",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#E43A19',
                  activebackground='#111F4D',
                  command=feature_accomodationwindow,
                  font=font_nearbyinfo
                  )
    next.grid(row=10, columnspan=4, padx=(0, 50), pady=10, sticky='se')

    # setting up the back button
    # Setting up the back button
    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(userdetails_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(userdetails_window, parent),
                  # command=back,
                  font=font_nearbyinfo
                  )
    Back.grid(row=10, columnspan=4, padx=(10, 40), pady=10, sticky='sw')

    # Setting up the label for "budget"
    budget_label = Label(userdetails_window,
                         text="Enter the place you specifically want to visit",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_nearbyinfo)
    budget_label.grid(row=10, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    entry_field = Entry(userdetails_window,
                        width=50,
                        justify="left",
                        # anchor="w"
                        )
    entry_field.grid(row=11, columnspan=4, pady=10)


    # Configure column sizes
    userdetails_window.grid_columnconfigure(0, weight=1, uniform="group1")
    userdetails_window.grid_columnconfigure(1, weight=1, uniform="group1")
    userdetails_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    userdetails_window.grid_rowconfigure(2, weight=0)
    userdetails_window.grid_rowconfigure(3, weight=0)
    userdetails_window.grid_rowconfigure(4, weight=0)
    userdetails_window.grid_rowconfigure(5, weight=0)
    userdetails_window.grid_rowconfigure(6, weight=0)
    userdetails_window.grid_rowconfigure(7, weight=0)
    userdetails_window.grid_rowconfigure(8, weight=0)
    userdetails_window.grid_rowconfigure(9, weight=0)
    userdetails_window.grid_rowconfigure(10, weight=0)
    userdetails_window.grid_rowconfigure(11, weight=0)

    userdetails_window.mainloop()


if __name__ == "__main__":
    window = Tk()
    create_tripdetailswindow(window)
    window.mainloop()
