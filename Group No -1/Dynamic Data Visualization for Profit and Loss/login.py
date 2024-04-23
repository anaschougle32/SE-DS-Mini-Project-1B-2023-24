from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import subprocess



class loginClass:
    def __init__(self, root):
        self.root = root
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="retailers",
            port=3306
        )

        self.cursor = self.db.cursor()

    def login(self):
        try:
            username = user.get()
            password = code.get()

            if not all([username, password]):
                messagebox.showerror("Error", "Please enter both username and password.")
                return

            query = "SELECT username,password FROM login WHERE username = %s AND password = %s"
            values = (username, password)

            self.cursor.execute(query, values)
            user_data = self.cursor.fetchone()

            if user_data:
                messagebox.showinfo("Success", "Login Successful!")
                username = user_data[0]  # Extract user ID
                self.dashboard()
                self.display_user_profile(username)  # Pass user ID to display_user_profile method
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def display_user_profile(self, username):
        self.root.destroy()  # Close the login window
        root = Tk()  # Create a new window
        obj=UserProfile(root, username)  # Pass user ID to UserProfile class
        root.mainloop()

    def dashboard(self):
        subprocess.run(['python', 'dashboard.py'])

root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

class UserProfile:
	def __init__(self, root, username):
		self.root = root
		self.root.title("User Profile")
		self.root.geometry("600x400")  # Increase frame size

		try:
			# Connect to MySQL database
			self.db = mysql.connector.connect(
				host="localhost",
				user="root",
				password="root",
				database="retailers",
				port=3306
			)

			# Fetch user data from the database
			self.cursor = self.db.cursor()
			query = "SELECT * FROM login WHERE username = %s"
			self.cursor.execute(query, (username,))
			user_data = self.cursor.fetchone()

			# Display user profile information
			if user_data:
				self.display_profile(user_data)
			else:
				messagebox.showerror("Error", "User not found")
				self.root.destroy()
		except mysql.connector.Error as err:
			messagebox.showerror("MySQL Error", f"Error: {err}")
			self.root.destroy()

	def display_profile(self, user_data):
		# User profile frame
		frame = Frame(self.root)
		frame.pack(pady=20)  # Add some padding

		# Load and display image
		img = PhotoImage(file='hyy.png')
		img_label = Label(frame, image=img)
		img_label.image = img  # Keep a reference to the image to prevent garbage collection
		img_label.pack()

		# User profile labels with larger font
		Label(frame, text="User Profile", font=("Helvetica", 24, "bold")).pack(pady=10)  # Larger font
		Label(frame, text=f"Username: {user_data[0]}", font=("Helvetica", 16)).pack()  # Larger font
		Label(frame, text=f"Email: {user_data[1]}", font=("Helvetica", 16)).pack()  # Larger font
		Label(frame, text=f"Mobile: {user_data[2]}", font=("Helvetica", 16)).pack()
		Button(frame, text="Close", command= self.dashboard).pack(side="top", anchor="ne")

	def dashboard(self) :
		self.root.destroy()
		subprocess.run(['python', 'dashboard.py'])

def userprofile(self, username):
        root = Tk()  # Create a new window for user profile
        userprofile(root, username)  # Pass user ID to UserProfile class
        root.mainloop()



img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=100)

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
login_instance = loginClass(root)
Button(frame,width=39,pady=7,text='LOGIN',bg='#57a1f8',fg='white',border=0,command=login_instance.login).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)
def reg():
    root.destroy()
    subprocess.run(['python', 'signup.py'])
sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=reg)
sign_up.place(x=215,y=270)





root.mainloop()