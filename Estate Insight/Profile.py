from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


class profile:
    def __init__(self,root):
        self.root = root
        self.add_user_pic = tk.PhotoImage(file='Images/estate.png')

        # def create_self.root(parent):
        # self.root = Toplevel(parent)

        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 15, "bold")

        one = Label(root,
                    text="EstateInsight",
                    bg="#B31312",
                    fg="white",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=1,
                    height=1)
        one.pack(fill=X, side=TOP)
        name_label = Label(one,
                           text='Insert Name',
                           bg='#B31312',
                           fg='white',
                           bd=0)
        name_label.place(relx=0.85, rely=0.1)  # name
        down_arrow = Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
        down_arrow.pack()
        down_arrow.menu = Menu(down_arrow)
        down_arrow["menu"] = down_arrow.menu
        down_arrow.menu.add_checkbutton(label="Profile")
        down_arrow.menu.add_checkbutton(label="Agents")
        down_arrow.place(relx=0.92)  # drop down arrow

        # app color
        self.root.configure(bg='white')

        # setting up geometry for app
        window_width = 1000
        window_height = 660

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # setting up icon for window title
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)

        # setting up the main parts
        gender_selection = tk.StringVar()  # gender string def

        # pic upload
        self.pic_path = tk.StringVar()
        self.pic_path.set('')

        def open_pic():
            path = askopenfilename()

            if path:
                self.img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                self.pic_path.set(path)

                add_pic_butt.config(image=self.img)
                add_pic_butt.image = self.img

        whole_page_frame = tk.Frame(root, bg='white', highlightthickness=2)

        # adding top text
        top_text = tk.Label(whole_page_frame, text='Complete your profile',
                            bg='white',
                            fg='black',
                            font=('Bold', 17))
        top_text.place(relx=0.01, rely=0.01)

        # adding the profile pic insertion
        add_pic_frame = tk.Frame(whole_page_frame,
                                 highlightbackground='black',
                                 highlightthickness=2,
                                 bg='white')
        add_pic_butt = tk.Button(add_pic_frame, image=self.add_user_pic, bd=0,
                                 command=open_pic)  # the pic upload button
        add_pic_butt.pack()
        add_pic_frame.place(relx=0.01, rely=0.08, width=105, height=105)

        # adding name entry box
        enter_name = tk.Label(whole_page_frame, text='Enter Name', font=('Bold', 15), bg='white')
        enter_name.place(relx=0.01, rely=0.3)
        enter_name_ent = tk.Entry(whole_page_frame, font=('Bold', 15),
                                  highlightcolor='black', highlightbackground='gray',
                                  highlightthickness=2)  # name entry button
        enter_name_ent.place(relx=0.01, rely=0.35)

        # adding gender selection
        gender_select = tk.Label(whole_page_frame, text='Specify Gender',
                                 font=('Bold', 15), bg='white')
        gender_select.place(relx=0.65, rely=0.3)
        male = tk.Radiobutton(whole_page_frame, text='Male',
                              font=('Bold', 15), bg='white',
                              variable=gender_selection, value='male')  # male button
        male.place(relx=0.65, rely=0.35)
        female = tk.Radiobutton(whole_page_frame, text='Female',
                                font=('Bold', 15), bg='white',
                                variable=gender_selection, value='female')  # female button
        female.place(relx=0.74, rely=0.35)
        other = tk.Radiobutton(whole_page_frame, text='Other',
                               font=('Bold', 15), bg='white',
                               variable=gender_selection, value='other')  # other button
        other.place(relx=0.85, rely=0.35)
        gender_selection.set('male')

        # adding email entry box
        enter_email = tk.Label(whole_page_frame, text='Enter Email', font=('Bold', 15), bg='white')
        enter_email.place(relx=0.01, rely=0.5)
        enter_email_ent = tk.Entry(whole_page_frame, font=('Bold', 15),
                                   highlightcolor='black', highlightbackground='gray',
                                   highlightthickness=2)  # email entry button
        enter_email_ent.place(relx=0.01, rely=0.55)

        # adding mobile no. entry box
        enter_mobile = tk.Label(whole_page_frame, text='Mobile No.', font=('Bold', 15), bg='white')
        enter_mobile.place(relx=0.65, rely=0.5)
        enter_mobile_ent = tk.Entry(whole_page_frame, font=('Bold', 15),
                                    highlightcolor='black', highlightbackground='gray',
                                    highlightthickness=2)  # mobile no. entry button
        enter_mobile_ent.place(relx=0.65, rely=0.55)

        # adding city entry box
        enter_city = tk.Label(whole_page_frame, text='Enter City', font=('Bold', 15), bg='white')
        enter_city.place(relx=0.01, rely=0.7)
        enter_city_ent = tk.Entry(whole_page_frame, font=('Bold', 15),
                                  highlightcolor='black', highlightbackground='gray',
                                  highlightthickness=2)  # city entry button
        enter_city_ent.place(relx=0.01, rely=0.75)

        # adding register entry box
        enter_register = tk.Label(whole_page_frame, text='Register as', font=('Bold', 15), bg='white')
        enter_register.place(relx=0.65, rely=0.7)
        enter_register_ent = tk.Entry(whole_page_frame, font=('Bold', 15),
                                      highlightcolor='black', highlightbackground='gray',
                                      highlightthickness=2)  # register entry button
        enter_register_ent.place(relx=0.65, rely=0.75)

        # adding the submit button
        submit_butt = tk.Button(whole_page_frame, text="Save",
                                font=('Bold', 15), bg='#B31312',
                                fg='white', bd=1,command=self.home)
        submit_butt.place(relx=0.5, rely=0.95, anchor=CENTER)

        whole_page_frame.pack(pady=3)
        whole_page_frame.pack_propagate(False)
        whole_page_frame.configure(width=980, height=600)

        # setting up the back page button

        back_button = Button(root, bg='#B31312', fg='white', text='<<Back',command=self.back)
        back_button.place(relx=0.9, rely=0.1)

    def home(self):
        self.root.destroy()
        import Homepage1
    def back(self):
        self.root.destroy()
        import Homepage1


root=Tk()
obj = profile(root)
root.mainloop()

