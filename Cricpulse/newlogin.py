from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import subprocess


class loginClass:
    def __init__(self,root):
        self.root = root
        self.db = mysql.connector.connect(host="localhost", user="root", password="Parthavi@1204", database="cricpulse", auth_plugin='mysql_native_password')

        self.cursor = self.db.cursor()

    def login(self):
        try:
            username = user.get()
            password = code.get()

            if not all([username, password]):
                messagebox.showerror("Error", "Please enter both username and password.")
                return

            query = "SELECT * FROM loginad WHERE username = %s AND password = %s"
            values = (username, password)

            self.cursor.execute(query, values)
            result = self.cursor.fetchone()

            if result:
                messagebox.showinfo("Success", "Login Successful!")
                self.dashboard()# Add your code here for successful login
            else:
                messagebox.showerror("Error", "Invalid username or password.")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def dashboard(self):
        self.root.destroy()
        subprocess.run(['python', 'new1.py'])
root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)




frame=Frame(root,width=400,height=400,bg="white")
frame.place(x=450,y=50)

heading=Label(frame,text='SIGN IN',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI',23,'bold'))
heading.place(x=100,y=5)

###########------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#########------------------

def on_enter(e):
    if code.get() == 'Password':
        code.delete(0, 'end')  # Clear the default text when the Entry is focused
        code.config(show='*')


def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')
        code.config(show='')  # Show actual characters when the Entry is not focused




code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

####################------------------------------

buttonl = Button(frame,width=39,pady=7,text='LOGIN',bg='#57a1f8',fg='white',border=0,command=loginClass(root).login).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)
def reg():
    root.destroy()
    subprocess.run(['python', 'reg.py'])
sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=reg)
sign_up.place(x=215,y=270)





root.mainloop()