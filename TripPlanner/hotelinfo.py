from tkinter import *
import tkinter as tk


def create_hotel(parent):
    hotel_window = Toplevel(parent)
    # main_window.geometry("1000x600")
    hotel_window.title("Select your destination")
    hotel_window.configure(background="#111F4D")

    # Positioning the application

    window_width = 900
    window_height = 700

    screen_width = hotel_window.winfo_screenwidth()
    screen_height = hotel_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    hotel_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    hotel_window.iconphoto(True, icon)

    # Setting up the font
    font_info1 = ('Arial', 30, 'italic')
    font_button = ('Arial', 15, 'bold')
    font_hotelhighlight = ('Arial', 15, 'bold')
    font_to = ('Arial', 20, 'bold')
    font_map_view_button = ('Arial', 10, 'bold')
    font_visit = ('Arial', 20, 'bold')

    info1_label = Label(hotel_window,
                        text="The Taj Mahal Palace",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_info1)
    info1_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

    frame1 = Frame(hotel_window,
                   width=350,
                   height=350,
                   bg="#3652AD")
    frame1.grid(row=1, column=0, columnspan=3, padx=(20, 0), pady=10, sticky='n')

    left_image = PhotoImage(file='taj.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(padx=45, pady=45)

    hotelhighlight_label = Label(hotel_window,
                                 text="Hotel Highlight",
                                 fg='#f7f7f7',
                                 bg='#111F4D',
                                 font=font_hotelhighlight)
    hotelhighlight_label.grid(row=2, column=0, columnspan=3, padx=(10, 200), pady=10, sticky='w')

    luxhotel_label = Label(hotel_window,
                                 text="India's First Luxury Hotel,9 Iconic Restaurants & Bars",
                                 fg='#f7f7f7',
                                 bg='#111F4D',
                                 font=font_hotelhighlight)
    luxhotel_label.grid(row=3, column=0, columnspan=3, padx=(10, 200), pady=0, sticky='w')

    highhotel_label = Label(hotel_window,
                           text="High-tea & Live Music Every Evening",
                           fg='#f7f7f7',
                           bg='#111F4D',
                           font=font_hotelhighlight)
    highhotel_label.grid(row=4, column=0, columnspan=3, padx=(10, 200), pady=0, sticky='w')

    luxury_label = Label(hotel_window,
                            text="Luxury Shopping Arcade",
                            fg='#f7f7f7',
                            bg='#111F4D',
                            font=font_hotelhighlight)
    luxury_label.grid(row=5, column=0, columnspan=3, padx=(10, 200), pady=0, sticky='w')

    address_label = Label(hotel_window,
                         text="Address:-",
                         fg='#f7f7f7',
                         bg='#111F4D',
                         font=font_hotelhighlight)
    address_label.grid(row=6, column=0, columnspan=3, padx=(10, 200), pady=0, sticky='w')

    finaladdress_label = Label(hotel_window,
                          text="Apollo Bunder, Mumbai, Maharashtra, 400 001,India",
                          fg='#f7f7f7',
                          bg='#111F4D',
                          font=font_hotelhighlight)
    finaladdress_label.grid(row=6, column=0, columnspan=3, padx=(120, 0), pady=0, sticky='w')

    price_label = Label(hotel_window,
                               text="Price :-",
                               fg='#f7f7f7',
                               bg='#111F4D',
                               font=font_hotelhighlight)
    price_label.grid(row=7, column=0, columnspan=3, padx=10, pady=0, sticky='w')

    price_count_label = Label(hotel_window,
                        text="10,000/per night",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_hotelhighlight)
    price_count_label.grid(row=7, column=0, columnspan=3, padx=(120,0), pady=0, sticky='w')

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(hotel_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(hotel_window, parent),
                  # command=back,
                  font=font_button
                  )
    Back.grid(row=7, column=0, columnspan=3, padx=(0,10), pady=0, sticky='ne')

    # Configure column sizes
    hotel_window.grid_columnconfigure(0, weight=1, uniform="group1")
    hotel_window.grid_columnconfigure(1, weight=1, uniform="group1")
    hotel_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    hotel_window.grid_rowconfigure(2, weight=0)
    hotel_window.grid_rowconfigure(3, weight=0)
    hotel_window.grid_rowconfigure(4, weight=0)
    hotel_window.grid_rowconfigure(5, weight=0)
    hotel_window.grid_rowconfigure(6, weight=0)
    hotel_window.grid_rowconfigure(7, weight=0)


if __name__ == "__main__":
    window = Tk()
    create_hotel(window)
    window.mainloop()
