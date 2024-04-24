from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from Homepage1 import Homepage1



class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        self.img = PhotoImage(file='Images/estate_size.png')
        Label(root, image=self.img, bg="white").place(x=140, y=120)

        self.frame = Frame(root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        heading = Label(self.frame, text='LOGIN', fg='BLACK', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        # Username column code
        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            name = self.user.get()
            if name == '':
                self.user.insert(0, 'Username')

        self.user = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "Username")
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        # Password column code
        def on_enter(e):
            self.password.delete(0, 'end')

        def on_leave(e):
            name = self.password.get()
            if name == '':
                self.password.insert(0, 'Password')

        self.password = Entry(self.frame, width=25, fg='black', border=0, bg='white',show="*", font=('Microsoft Yahei UI Light', 11))
        self.password.place(x=30, y=150)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', on_enter)
        self.password.bind('<FocusOut>', on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        # Button Code
        Button(self.frame, width=39, pady=7, text='LOGIN', bg='#B31312', fg='white', border=0, command=self.login).place(x=35, y=204)
        label2 = Label(self.frame, text="Dont have an account?", fg='black', bg='white',
                       font=('Microsoft Yahei UI Light', 9))
        label2.place(x=75, y=270)

        signup = Button(self.frame, width=6, text="Sign in", border=0, bg='#B31312', cursor='hand2', fg='white', command=self.signup_page)
        signup.place(x=215, y=270)

    def signup_page(self):
        self.root.destroy()
        import signup




    def login(self):
        username = self.user.get()
        password = self.password.get()

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='#22107031#',
                database='estateinsight'
            )
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sell WHERE username = %s AND password = %s', (username, password))
            row = cursor.fetchone()
            if row:
                messagebox.showinfo("Success", "Login Successful")
                self.home(username)
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
            conn.close()
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Database Error", "Failed to connect to database")
    def home(self, username):
        self.root.destroy()
        root = Tk()
        obj = Homepage1(root, username)
        root.mainloop()


root=Tk()
obj = Login(root)
root.mainloop()