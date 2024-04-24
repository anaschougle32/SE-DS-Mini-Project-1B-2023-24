from tkinter import *
from register import create_register
from login import create_login


def create_loginsignup_window(parent):
    # Setting Up the window
    loginsignup_window = Toplevel(parent)
    # loginsignup_window.geometry("420x400")
    loginsignup_window.title("Get started")
    loginsignup_window.configure(background="#111F4D")

    # Positioning the application

    window_width = 420
    window_height = 430

    screen_width = loginsignup_window.winfo_screenwidth()
    screen_height = loginsignup_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    loginsignup_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Setting up the icon for the window
    icon = PhotoImage(file='logo.png')
    loginsignup_window.iconphoto(True, icon)

    # Setting up the font
    font_getstarted = ('Arial', 30, 'italic')
    font_Registermessage1 = ('Arial', 10, 'italic')
    font_Registermessage2 = ('Arial', 10, 'italic')
    font_Registermessage3 = ('Arial', 10, 'italic')
    font_Final_Registermessage3 = ('Arial', 10, 'bold')
    font_button = ("Arial", 10, "bold")
    font_useralready = ("Arial", 10, "bold")

    # Setting up the "Get started label"
    getstarted_label = Label(loginsignup_window,
                             text="Get started",
                             fg='#f7f7f7',
                             bg='#111F4D',
                             font=font_getstarted)
    getstarted_label.pack(padx=10, pady=10)

    # Setting up the "Register info label"

    Registermessage1_label = Label(loginsignup_window,
                                   text="Get started and unlock a world of seamless travel planning! ",
                                   fg='#f7f7f7',
                                   bg='#111F4D',
                                   font=font_Registermessage1)
    Registermessage1_label.pack(padx=10, pady=5)

    Registermessage2_label = Label(loginsignup_window,
                                   text="Register now to plan your trips with precision ",
                                   fg='#f7f7f7',
                                   bg='#111F4D',
                                   font=font_Registermessage2)
    Registermessage2_label.pack()

    Registermessage3_label = Label(loginsignup_window,
                                   text="explore destinations like never before.",
                                   fg='#f7f7f7',
                                   bg='#111F4D',
                                   font=font_Registermessage3)
    Registermessage3_label.pack(pady=5)

    Final_Registermessage3_label = Label(loginsignup_window,
                                         text="Click below to register now",
                                         fg='#f7f7f7',
                                         bg='#111F4D',
                                         font=font_Final_Registermessage3)
    Final_Registermessage3_label.pack(pady=5)

    # Setting up the Register button

    def feature_register_window():
        loginsignup_window.withdraw()  # Hide the loginsignup window
        register_window = create_register(loginsignup_window)  # Pass loginsignup_window as the parent
        register_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(loginsignup_window, register_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    Register = Button(loginsignup_window,
                      text="Register",
                      foreground='#f7f7f7',
                      background='#D24545',
                      activeforeground='#E43A19',
                      activebackground='#111F4D',
                      command=feature_register_window,
                      font=font_button
                      )
    Register.pack(padx=10, pady=20)

    # Setting up the "Already a user label"
    useralready_label = Label(loginsignup_window,
                              text="Already a user ?",
                              fg='#f7f7f7',
                              bg='#111F4D',
                              font=font_useralready)
    useralready_label.pack(padx=10, pady=1)

    # Setting up the "Login below"
    loginbelow_label = Label(loginsignup_window,
                             text="Login below",
                             fg='#f7f7f7',
                             bg='#111F4D',
                             font=font_useralready)
    loginbelow_label.pack(padx=10, pady=1)

    # Setting up the login button
    def feature_login():
        loginsignup_window.withdraw()
        login_window = create_login(loginsignup_window)
        if login_window:  # Check if create_login returned a valid window # it was returning a none value had to do this
            login_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(loginsignup_window, login_window))

    def close_windows(main_window, popup_window):
        popup_window.destroy()
        main_window.destroy()

    Login = Button(loginsignup_window,
                   text="Login",
                   foreground='#f7f7f7',
                   background='#D24545',
                   activeforeground='#E43A19',
                   activebackground='#111F4D',
                   command=feature_login,
                   font=font_button
                   )
    Login.pack(padx=10, pady=20)

    # Setting up the back button

    def feature_back(current_window, previous_window):
        current_window.withdraw()  # Hide the current window
        previous_window.deiconify()

    Back = Button(loginsignup_window,
                  text="Back",
                  foreground='#f7f7f7',
                  background='#D24545',
                  activeforeground='#D24545',
                  activebackground='#A94438',
                  command=lambda: feature_back(loginsignup_window, parent),
                  font=font_button
                  )
    Back.pack(padx=10, anchor='sw')

    return loginsignup_window  # Return the created window


if __name__ == "__main__":
    window = Tk()
    create_loginsignup_window(window)
    previous_window = window
    window.mainloop()
