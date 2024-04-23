from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
from tkinter import Button, Frame, Label, Entry, PhotoImage, Canvas, Scrollbar, Toplevel
import mysql.connector
from PIL import Image, ImageTk
import tkinter as tk
class agent1:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("EstateInsight")
        self.main_window.resizable(False, False)
        self.main_window.configure(bg='white')

        font_info = ("Arial", 19, "bold")

        # setting up the app header
        header = Label(main_window,
                       text="EstateInsight",
                       bg="#B31312",
                       fg="white",
                       font=font_info,
                       anchor=W,
                       relief=SUNKEN,
                       bd=1,
                       pady=3)
        header.pack(fill=X, side=TOP)

        # setting up geometry for app
        window_width = 1000
        window_height = 660
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)
        self.main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # setting up icon for window title
        icon = PhotoImage(file='Images/estate.png')
        self.main_window.iconphoto(True, icon)

        self.canvas = Canvas(main_window, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(main_window, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.data_frame = Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.data_frame, anchor=tk.NW)

        # Connect to the database
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#22107031#',
            database='estateinsight'
        )

        # Fetch data from the database and create frames dynamically
        self.create_frames()

        self.data_frame.bind("<Configure>", self.on_frame_configure)

        # setting up the back page button
        back_button = Button(main_window, bg='#B31312', fg='white', text='<<Back',command=self.back)
        back_button.place(relx=0.93, rely=0.08)

    def create_frames(self):
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()

                # Execute your query to fetch data from the database
                cursor.execute("SELECT idagent, name, email, phoneno, profilepic FROM agent")

                # Fetch all rows
                rows = cursor.fetchall()

                for i, row in enumerate(rows):
                    idagent, name, email, phoneno, profilepic_path, = row

                    # Load profile picture as image
                    profilepic = PhotoImage(file=profilepic_path)

                    frame = Frame(self.data_frame, highlightthickness=2, width=800, height=200, bg='white',
                                  highlightbackground='black')
                    frame.pack(fill=tk.X, padx=10, pady=10, side=tk.TOP)

                    image_frame = Frame(frame, background='white', highlightbackground='black', highlightthickness=2)
                    image_frame.pack(padx=10, pady=10, side=tk.LEFT)

                    img_button = Button(image_frame, image=profilepic, bd=1, width=120, height=120)
                    img_button.image = profilepic  # Keep a reference to the image to prevent garbage collection
                    img_button.pack()

                    chat_button = Button(frame, text="Chat", bg='#B31312', fg='white',
                                         command=lambda id=idagent: self.chat(id))
                    chat_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 10))

                    name_label = Label(frame, text=name, font=('Bold', 17), bg='white')
                    name_label.pack(side=tk.LEFT, padx=(20, 0), pady=(10, 0))

                    email_label = Label(frame, text='Email:', font=('Bold', 15), bg='white')
                    email_label.pack(side=tk.LEFT, padx=(20, 0))

                    email_value = Label(frame, text=email, font=(15), bg='white')
                    email_value.pack(side=tk.LEFT)

                    phone_label = Label(frame, text='Phone No:', font=('Bold', 15), bg='white')
                    phone_label.pack(side=tk.LEFT, padx=(20, 0))

                    phone_value = Label(frame, text=phoneno, font=(15), bg='white')
                    phone_value.pack(side=tk.LEFT)

        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)

    def display_image(self, frame, image_path):
        try:
            # Open image using PIL
            image = Image.open(image_path)

            # Resize image
            image.thumbnail((200, 200))

            # Convert Image object to PhotoImage object
            photo_image = ImageTk.PhotoImage(image)

            # Display image in label
            label = Label(frame, image=photo_image, bg="white")
            label.image = photo_image  # Keep a reference to the image
            label.pack(side=tk.LEFT)

        except Exception as e:
            print("Error displaying image:", e)

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def c(self):
        self.main_window.destroy()
        import chat

    def chat(self, agent_id):

        # Insert a notification into the agent's table in the database
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()

                # Assuming you have an 'agents' table with columns 'agent_id' and 'notification'
                notification_message = "You have a new chat message"  # The notification message

                # Execute the query to insert the notification
                sql_update = ("UPDATE agent SET notification = %s WHERE idagent = %s")
                cursor.execute(sql_update,
                               (notification_message, agent_id))

                self.conn.commit()  # Commit the transaction

                # Print a message indicating that the notification has been sent
                print("Notification sent successfully!")
                self.c()



        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)

    def back(self):
        self.main_window.destroy()
        import Homepage1


main_window = Tk()
obj = agent1(main_window)
main_window.mainloop()