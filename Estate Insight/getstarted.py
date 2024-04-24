from tkinter import *
import tkinter as tk

class getstarted:
    def __init__(self, window):
        # Setting Up the app
        self.window = window
        self.window.title("EstateInsight")

        # Setting up the position of the app
        self.window_width = 500
        self.window_height = 500

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position = int((screen_width - self.window_width) / 2)
        y_position = int((screen_height - self.window_height) / 2)

        self.window.geometry(f"{self.window_width}x{self.window_height}+{x_position}+{y_position}")

        # Setting up the appearance
        self.window.configure(background="white")

        # Setting up the icon for the window
        self.icon = PhotoImage(file='Images/estate.png')
        self.window.iconphoto(True, self.icon)

        # Setting up the font
        font_moodlift = ('Arial', 30, 'bold')
        font_welcome = ("Arial", 15, "bold")
        font_info = ("Brush Script MT", 23)
        font_button = ("Arial", 10, "bold")

        # Setting up the intro for the image label
        self.photo = PhotoImage(file='Images/estate.png')
        language_language_label = Label(window,
                                        text="EstateInsight",
                                        font=font_moodlift,
                                        fg='black',
                                        bg='white',
                                        image=self.photo,  # replaces the text with image label
                                        compound='top')
        language_language_label.pack(padx=10, pady=20)


        # Setting up the Label For information
        infoLabel = tk.Label(window,
                             text="The Real Estate Discovery Platform",
                             fg='black',
                             bg='white',
                             font=font_info)
        infoLabel.pack()

        Entry = Label(window,
                      text="LogIn As",
                      foreground='Black',
                      background='white',
                      font=5,
                      #relief=GROOVE
                      )
        Entry.pack(padx=10, pady=20)

        userButt = Button(window,
                          text=" User ",
                          bg="#b31312",
                          fg='white',
                          border=0,
                          font=1,
                          command=self.user)
        userButt.place(relx=0.26, rely=0.65)

        agentButt = Button(window,
                           text="Agent",
                           bg="#b31312",
                           fg='white',
                           border=0,
                           font=1,
                           command=self.agent)
        agentButt.place(relx=0.45, rely=0.65)

        adminButt = Button(window,
                           text="Admin",
                           bg="#b31312",
                           fg='white',
                           border=0,
                           font=1,
                           command=self.admin)
        adminButt.place(relx=0.65, rely=0.65)

    def admin(self):
        self.window.destroy()
        print("Admin button clicked")
        import Admin_Page

    def agent(self):
        self.window.destroy()
        import agentlogin

    def user(self):
        self.window.destroy()
        import login


window = Tk()
obj = getstarted(window)
window.mainloop()
