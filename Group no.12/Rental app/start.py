from tkinter import *
from tkinter import messagebox
import mysql.connector as con
from dashboard import RentalApplication
from admin_dashboard import AdminDashboard
from PIL import Image, ImageTk


window = Tk()
window.geometry("1000x550")
window.title("Rental Application")
window.config(background="#212121")

def login():
    db = con.connect(host='localhost', user='root', password='Annsh@10', database='student')
    c = db.cursor()
    un = username_entry.get()
    pw = password_entry.get()

    # Check if the credentials match with student_login table
    c.execute("SELECT * FROM student_login WHERE username='" + un + "' AND password = '" + pw + "'")
    student_result = c.fetchone()

    # Check if the credentials match with admin_login table
    c.execute("SELECT * FROM admin_login WHERE admin_name='" + un + "' AND password = '" + pw + "'")
    admin_result = c.fetchone()

    if student_result:
        messagebox.showinfo("Success", "Student Login Successful")
        login_window.destroy()
        app = RentalApplication(Tk(), un)  # Assuming RentalApplication is for regular users
        app.run()
    elif admin_result:
        messagebox.showinfo("Success", "Admin Login Successful")
        login_window.destroy()
        app = AdminDashboard(Tk(), un)  # Assuming AdminDashboard is for admins
        app.run()
    else:
        messagebox.showerror("Error", "Invalid Login")

def get_started():
    window.destroy()  # Close the current window
    create_login_window()



def create_login_window():
    global login_window
    
    login_window = Tk()
    login_window.geometry("700x550")
    login_window.title("Rental Application")
    login_window.config(background="#212121")


    bg_image = Image.open("bg_image.png")  # Change "background_image.png" to your image file path
    bg_image_resized = bg_image.resize((978, 550), Image.LANCZOS)  # Resize the image to fit the window size

    # Convert the resized image to PhotoImage
    bg_image_tk = ImageTk.PhotoImage(bg_image_resized)

    # Create a label with the resized background image
    bg_label = Label(login_window, image=bg_image_tk)
    bg_label.place(relwidth=1, relheight=1)


    rectangular_frame =Frame(login_window, width=500, height=450, bg="black")
    rectangular_frame.place(x=100,y=40)

    login_label = Label(login_window,text="Login",bg="black",font=('Arial',26,'bold',UNDERLINE),fg="white")
    login_label.place(x=300,y=60)
    # Username label and entry
    username_label = Label(login_window, text="Username:", font=("Arial", 14),bg="black",fg="white")
    username_label.place(x=160,y=150)
    global username_entry
    username_entry = Entry(login_window, font=("Arial", 14),width=20)
    username_entry.place(x=270,y=150)

    # Password label and entry
    password_label = Label(login_window, text="Password:", font=("Arial", 14),bg="black",fg="white")
    password_label.place(x=160,y=200)
    global password_entry
    password_entry =Entry(login_window, show="*", font=("Arial", 14),width=20)
    password_entry.place(x=270,y=200)

    # Login button
    login_button = Button(login_window, text="Login", command=login,font=('Arial',15) ,cursor="hand2",bg="#D44C47", fg="white", width=25, height=1)
    login_button.place(x=200,y=270)

    label = Label(login_window,text="don't have any account -",bg="black",font=('Arial',10),fg="white")
    label.place(x=220,y=325)
    signup_button = Button(login_window, text="Sign up", command=signup,font=('Arial',12,UNDERLINE),borderwidth=0 ,cursor="hand2",bg="black", fg="#BB86FC", width=6, height=1)
    signup_button.place(x=370,y=322)

    login_window.mainloop()


def signup():
    global signup_window
    login_window.destroy()
    signup_window = Tk()
    signup_window.title("Sign Up")
    signup_window.geometry("700x550")
    signup_window.config(background="#212121")

    # Sign Up Form
    # Create a label for "Sign Up"

    bg_image = Image.open("bg_image.png")  # Change "background_image.png" to your image file path
    bg_image_resized = bg_image.resize((978, 550), Image.LANCZOS)  # Resize the image to fit the window size

    # Convert the resized image to PhotoImage
    bg_image_tk = ImageTk.PhotoImage(bg_image_resized)

    # Create a label with the resized background image
    bg_label = Label(signup_window, image=bg_image_tk)
    bg_label.place(relwidth=1, relheight=1)


    rectangular_frame =Frame(signup_window, width=500, height=450, bg="black")
    rectangular_frame.place(x=106,y=40)

    signup_label = Label(signup_window, text="Sign Up", font=("Helvetica", 24,UNDERLINE),bg="black" ,fg="white")
    signup_label.pack(pady=40)

    # Create entry fields for username and password
    username_label = Label(signup_window, text="Username:", font=("Helvetica", 14),bg="black" ,fg="white")
    username_label.place(x=230 ,y=90)
    global new_username_entry
    new_username_entry = Entry(signup_window, font=("Helvetica", 14),width=20)
    new_username_entry.place(x=230,y=120)

    password_label = Label(signup_window, text="Password:", font=("Helvetica", 14),bg="black" ,fg="white")
    password_label.place(x=230 ,y=155)
    global new_password_entry
    new_password_entry = Entry(signup_window, show="*", font=("Helvetica", 14),width=20)
    new_password_entry.place(x=230,y=185)

    phone_label = Label(signup_window, text="Phone no:", font=("Helvetica", 14),bg="black" ,fg="white")
    phone_label.place(x=230,y=220)
    global phone_entry
    phone_entry = Entry(signup_window, font=("Helvetica", 14),width=20)
    phone_entry.place(x=230,y=250)

    email_label = Label(signup_window, text="Email Id:", font=("Helvetica", 14),bg="black" ,fg="white")
    email_label.place(x=230,y=285)
    global email_entry
    email_entry = Entry(signup_window, font=("Helvetica", 14),width=20)
    email_entry.place(x=230,y=315)

    # Sign Up button
    signup_button = Button(signup_window, text="Sign Up",command=complete_signup,font=('Arial',12),cursor="hand2",bg="#D44C47",fg="white", width=20)
    signup_button.place(x=250,y=370)

    signup_window.mainloop()

def complete_signup():
    # Establish connection to the database
    db = con.connect(host='localhost', user='root', password='Annsh@10', database='student')
    c = db.cursor()

    # Retrieve values from entry fields
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    # Insert new user into the database
    try:
        c.execute("INSERT INTO student_login (username, password, phone_no, email_id) VALUES (%s, %s, %s, %s)", (new_username, new_password, phone, email))
        db.commit()
        messagebox.showinfo("Success", "Sign Up Successful! You can now log in.")
        signup_window.destroy()
        create_login_window()
    except Exception as e:
        messagebox.showerror("Error", f"Error signing up: {str(e)}")
        db.rollback()
    finally:
        c.close()
        db.close()

def select():
    global select_window
    select_window = Tk()
    select_window.title("Sign Up")
    select_window.geometry("700x550")
    select_window.config(background="#212121")

    

    bg_image = Image.open("bg_image.png")  # Change "background_image.png" to your image file path
    bg_image_resized = bg_image.resize((978, 550), Image.LANCZOS)  # Resize the image to fit the window size

    # Convert the resized image to PhotoImage
    bg_image_tk = ImageTk.PhotoImage(bg_image_resized)

    # Create a label with the resized background image
    bg_label = Label(select_window, image=bg_image_tk)
    bg_label.place(relwidth=1, relheight=1)


    rectangular_frame =Frame(select_window, width=500, height=450, bg="black")
    rectangular_frame.place(x=106,y=40)

    select_label = Label(select_window, text="Login Through :", font=("Helvetica", 24,UNDERLINE),bg="black" ,fg="white")
    select_label.place(x=250,y=60)

    # Sign Up button
    admin_button = Button(select_window, text="ADMIN",font=('Arial',14,'bold'),cursor="hand2",bg="#D44C47",fg="white", width=20,height=5)
    admin_button.place(x=230,y=130)

    user_button = Button(select_window, text="USER",font=('Arial',14,'bold'),cursor="hand2",bg="#D44C47",fg="white", width=20,height=5)
    user_button.place(x=230,y=310)

    select_window.mainloop()

def admin_login_window():
    global admin_window
    
    admin_window = Tk()
    admin_window.geometry("700x550")
    admin_window.title("Rental Application")
    admin_window.config(background="#212121")


    bg_image = Image.open("bg_image.png")  # Change "background_image.png" to your image file path
    bg_image_resized = bg_image.resize((978, 550), Image.LANCZOS)  # Resize the image to fit the window size

    # Convert the resized image to PhotoImage
    bg_image_tk = ImageTk.PhotoImage(bg_image_resized)

    # Create a label with the resized background image
    bg_label = Label(admin_window, image=bg_image_tk)
    bg_label.place(relwidth=1, relheight=1)


    rectangular_frame =Frame(admin_window, width=500, height=450, bg="black")
    rectangular_frame.place(x=100,y=30)

    login_label = Label(admin_window,text="Admin Login:",bg="black",font=('Arial',26,'bold',UNDERLINE),fg="white")
    login_label.place(x=260,y=60)
    # Username label and entry
    username_label = Label(admin_window, text="Username:", font=("Arial", 14),bg="black",fg="white")
    username_label.place(x=160,y=180)
    global username_entry
    username_entry = Entry(admin_window, font=("Arial", 14),width=20)
    username_entry.place(x=270,y=180)

    # Password label and entry
    password_label = Label(admin_window, text="Password:", font=("Arial", 14),bg="black",fg="white")
    password_label.place(x=160,y=230)
    global password_entry
    password_entry =Entry(admin_window, show="*", font=("Arial", 14),width=20)
    password_entry.place(x=270,y=230)

    # Login button
    login_button = Button(admin_window, text="Login",font=('Arial',15) ,cursor="hand2",bg="#D44C47", fg="white", width=25, height=1)
    login_button.place(x=200,y=320)


    admin_window.mainloop()

# Open and resize the background image
bg_image = Image.open("background_image.png")  # Change "background_image.png" to your image file path
bg_image_resized = bg_image.resize((1000, 550), Image.LANCZOS)  # Resize the image to fit the window size

# Convert the resized image to PhotoImage
bg_image_tk = ImageTk.PhotoImage(bg_image_resized)

# Create a label with the resized background image
bg_label = Label(window, image=bg_image_tk)
bg_label.place(relwidth=1, relheight=1)


button1=Button(window,text="Get Started",command=get_started,font=('Arial',12,'bold'),cursor="hand2",bg="#D44C47",fg="white",width=30,height=2)
button1.place(x=60,y=430)


window.mainloop()