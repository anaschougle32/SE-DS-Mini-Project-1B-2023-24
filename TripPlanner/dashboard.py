from tkinter import *
import tkinter as tk
from mainwindow import create_mainwindow
from details import create_details
from suggestion import create_suggestion
from basic import create_basic
from checklist import create_check
from tkinter import PhotoImage
from accomodation import create_accomodationwindow
from exp import create_expwindow
from budget import create_budget
from iternary import create_finaliternarywindow
from review import TripPlannerApp


def create_dashboard(parent):
    dash_board = Toplevel(parent)

    dash_board.title("Select your destination")
    dash_board.configure(background="#111F4D")
    dash_board.resizable(False, False)

    # Create two frames with different background colors
    frame1 = tk.Frame(dash_board, bg="#ADD8E6", width=800, height=90)
    frame2 = tk.Frame(dash_board, bg="#111F4D", width=800, height=450)

    # Place the frames in the root window, one below the other
    frame1.pack(side="top", fill="both", expand=True)
    frame2.pack(side="top", fill="both", expand=True)

    # Positioning the application

    window_width = 800
    window_height = 600

    screen_width = dash_board.winfo_screenwidth()
    screen_height = dash_board.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    dash_board.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the font
    font_info1 = ('Arial', 30, 'italic')
    font_button = ('Arial', 15, 'bold')
    font_from = ('Arial', 10, 'italic')
    font_to = ('Arial', 20, 'bold')
    font_map_view_button = ('Arial', 10, 'bold')

    # Setting up the first info label stating 'Enter your destination'

    def on_plan_trip():

        dash_board.withdraw()  # Hide the dashboard window
        mainwindow = create_finaliternarywindow(dash_board)
        if mainwindow:
            mainwindow.protocol("WM_DELETE_WINDOW", lambda: close_windows(dash_board, mainwindow))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    plan_button = tk.Button(frame2,
                            text="Plan your trip",
                            fg='#f7f7f7',
                            bg='#111F4D',
                            font=font_button,
                            command=on_plan_trip,
                            )
    plan_button.place(x=50, y=60)

    def show_additional_buttons():
        button2.place(x=80, y=170)
        button3.place(x=80, y=210)

    def feature_placewindow():
        dash_board.withdraw()  # Hide the main window
        place_window = create_suggestion(dash_board)
        if place_window:
            place_window.protocol("WM_DELETE_WINDOW",
                                  lambda: close_windows(window, place_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    def feature_accomodationwindow():
        dash_board.withdraw()  # Hide the main window
        accomo_window = create_accomodationwindow(dash_board)
        if accomo_window:
            accomo_window.protocol("WM_DELETE_WINDOW",
                                   lambda: close_windows(window, accomo_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    sug_button = tk.Button(frame2,
                           text="Get Suggestions",
                           fg='#f7f7f7',
                           bg='#111F4D',
                           font=font_button,
                           command=show_additional_buttons)
    sug_button.place(x=50, y=115)
    button2 = tk.Button(frame2, text="PLaces", font=font_from, command=feature_placewindow)
    button3 = tk.Button(frame2, text="Accomodation", font=font_from, command=feature_accomodationwindow)

    def basic_ness():
        dash_board.withdraw()  # Hide the main window
        basic_n_window = create_basic(dash_board)
        if basic_n_window:
            basic_n_window.protocol("WM_DELETE_WINDOW",
                                    lambda: close_windows(window, basic_n_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    basic_button = tk.Button(frame2,
                             text="Basic Necessities",
                             fg='#f7f7f7',
                             bg='#111F4D',
                             command=basic_ness,
                             font=font_button,
                             )
    basic_button.place(x=50, y=250)

    def check():
        dash_board.withdraw()  # Hide the main window
        check_n_window = create_check(dash_board)
        if check_n_window:
            check_n_window.protocol("WM_DELETE_WINDOW",
                                    lambda: close_windows(window, check_n_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    check_button = tk.Button(frame2,
                             text="Create Checklist",
                             fg='#f7f7f7',
                             bg='#111F4D',
                             command=check,
                             font=font_button,
                             )
    check_button.place(x=50, y=300)

    def budget():
        dash_board.withdraw()  # Hide the main window
        bud_n_window = create_budget(dash_board)
        if bud_n_window:
            bud_n_window.protocol("WM_DELETE_WINDOW",
                                  lambda: close_windows(window, bud_n_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    check_button = tk.Button(frame2,
                             text="Budget Calculator",
                             fg='#f7f7f7',
                             bg='#111F4D',
                             command=budget,
                             font=font_button,
                             )
    check_button.place(x=50, y=350)

    # def experience():
    #     dash_board.withdraw()  # Hide the main window
    #     exp_n_window = create_expwindow(dash_board)
    #     if exp_n_window:
    #         exp_n_window.protocol("WM_DELETE_WINDOW",
    #                               lambda: close_windows(window, exp_n_window))
    #
    # def close_windows(main_window, popup_window):
    #     popup_window.destroy()
    #     main_window.destroy()
    #
    # check_button = tk.Button(frame2,
    #                          text="Enter your Experience",
    #                          fg='#f7f7f7',
    #                          bg='#111F4D',
    #                          command=experience,
    #                          font=font_button,
    #                          )
    # check_button.place(x=50, y=400)

    def open_review_page(parent):
        """Open the review GUI page."""
        dash_board.withdraw()
        review_window = tk.Toplevel(parent)
        review_app = TripPlannerApp(review_window)

    review_button = tk.Button(frame2,
                              text="User Review",
                              fg='#f7f7f7',
                              bg='#111F4D',
                              command=lambda: open_review_page(parent),
                              font=font_button,
                              )
    review_button.place(x=50, y=400)

    info1_label = Label(frame1,
                        text="TRIP PLANNER",
                        fg='#f7f7f7',
                        bg='#111F4D',
                        font=font_info1)
    info1_label.place(x=300, y=45)

    frame3 = Frame(frame2,
                   width=500,
                   height=350,
                   bg="#111F4D")
    frame3.place(x=250, y=20)

    left_image = PhotoImage(file='output.png')
    left_image_label = Label(frame3,
                             image=left_image,
                             bg="white", height=300, width=450)
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(padx=25, pady=25)


if __name__ == "__main__":
    window = Tk()
    create_dashboard(window)
    window.mainloop()
