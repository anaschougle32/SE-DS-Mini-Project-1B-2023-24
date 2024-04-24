from tkinter import *
from tkinter import ttk 
from verification import *
import random
import time
from tkinter import messagebox, filedialog
import sqlite3
import os
import subprocess
import admin_db
import tkinter as tk
import shutil
from admin_db import fetch_courses_admin_db


def on_closing(window):
    global global_course_name
    global_course_name = None
    
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        logout()
        window.destroy()
      
    

def create_account():
    login_window.withdraw()  # Hide the login window
    register_window.deiconify()  # Show the register window

def back_to_login():
    register_window.withdraw()  # Hide the register window
    login_window.deiconify()  # Show the login window again

def generate_token():
    return str(random.randint(100000, 999999))
    login_window.after(180000, clear_otp)
    return otp

def clear_otp():
    global otp
    otp = None
    
def register():
    name = name_entry.get()
    role = roles_combobox.get()
    email = email_entry.get()
    password = password_entry_reg.get()
    confirm_password = confirm_entry.get()

    # Check if any input field is empty
    if not all([name, role, email, password, confirm_password]):
        messagebox.showerror("Error", "All fields are required.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Password does not match.")
        return

    global otp
    otp = generate_token()

    result = register_user(name, role, email, password, otp)
    
    if result.startswith("Error"):
        messagebox.showerror("Error", result)
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry_reg.delete(0, END)
        roles_combobox.set('')
        confirm_entry.delete(0, END)
    else:
        # messagebox.showinfo("Success", result)
        # If registration is successful, show the OTP window
        otp_window.deiconify()  # Show the OTP window
    
    print("Register account...")

global login_email

def login():
    # committee_login()
    global login_email  # Declare login_email as a global variable
    email = email_entry_log.get()
    email = email_entry_log.get()
    login_email = email
    login_password = password_entry_log.get()
    
    # Validate user input
    if not all([email, login_password]):
        messagebox.showerror("Error", "Please enter both email and password.")
        return

    authenticated = authenticate_user(email, login_password)

    if authenticated:
        if is_admin(email):
            admin_login()
        elif is_applicant(email):
           applicant_login()
        elif is_committee(email):
           committee_login()
        else:
            # User is neither admin nor applicant
            email_entry_log.delete(0, END)
            password_entry_log.delete(0, END)
            close_login()
    else:
        messagebox.showerror("Error", "Invalid email or password. Please try again.")

def admin_login():
    login_window.withdraw()
    admin_db.Re_unverified_user(table_verified)
    admin_db.applicant_data(table_applicant)
    home_window.deiconify()
    
def applicant_login():
    login_window.withdraw()
    admin_db.applicant_data(table_submission_app)
    load_courses()
    applicant_window.deiconify()
    
    
def committee_login():
    login_window.withdraw()
    admin_db.applicant_data(table_committee)
    view_home_window.deiconify()
    

def close_otp():
    otp_window.withdraw()
    register_window.withdraw()
    login_window.withdraw()
    window_admin.deiconify() 
    
def verify_otp():
    entered_otp = otp_entry.get()
    if entered_otp == str(otp):
        
        # Get user inputs
        name = name_entry.get()
        role = roles_combobox.get()
        email = email_entry.get()
        password = password_entry_reg.get()
        email_token = secrets.token_urlsafe(16)
        
        # Show success message for OTP verification
        messagebox.showinfo("Success", "OTP Verified Successfully!")
        
        # Connect to the database
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        
        # Insert new user into the database
        c.execute("INSERT INTO users (name, role, email, password, email_token) VALUES (?, ?, ?, ?, ?)",
                (name, role, email, password, email_token))
        
        # Update user table to mark email as verified
        c.execute("UPDATE users SET email_verified = ? WHERE email = ?", (True, email))
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry_reg.delete(0, END)
        roles_combobox.set('')
        confirm_entry.delete(0, END)
        otp_entry.delete(0, END)
        
        close_otp()
        login_window.deiconify()
    else:
        messagebox.showerror("Error", "Invalid OTP")

def resend():
    email = email_entry.get()
    global otp  
    otp = generate_token()
    
    result2 = resend_otp(email, otp)
    messagebox.showinfo("Success", result2) 



def forgot_password(event=None):
    forget_window.deiconify()
    

def verify_user_email():
    email = forget_email_entry.get()
    global otp  
    otp = generate_token()
    print(otp)
    send_email_verification(email, otp)
    forget_otp_window.deiconify()
    otp_window.withdraw()
    forget_window.withdraw()

def verify_otp_forget():
    entered_otp = otp_entry_forget.get()
    if entered_otp == str(otp):
        otp_window.withdraw()
        display_set_password_window()
    else:
        messagebox.showerror("Error", "Invalid OTP")
        
def display_set_password_window():
    # Create a new window for setting the new password
    set_password_window = Toplevel()
    set_password_window.title("Set New Password")
    set_password_window.geometry("300x300")
    center_window(set_password_window)
    
    # Add entry fields for new password and confirm password
    new_password_label = tk.Label(set_password_window, text="New Password:")
    new_password_label.pack()
    new_password_entry = tk.Entry(set_password_window, show="*")
    new_password_entry.pack()
    
    confirm_password_label = tk.Label(set_password_window, text="Confirm Password:")
    confirm_password_label.pack()
    confirm_password_entry = tk.Entry(set_password_window, show="*")
    confirm_password_entry.pack()
    
    # Button to submit the new password
    submit_button = tk.Button(set_password_window, text="Submit", command=lambda: update_password(set_password_window, new_password_entry.get(), confirm_password_entry.get()))
    submit_button.pack()

def update_password(window, new_password, confirm_password):
    
    email = forget_email_entry.get()
    
    if new_password == confirm_password:

        update_password_in_database(new_password, email)
        # Close the window after updating the password
        window.destroy()
    else:
        messagebox.showerror("Error", "Passwords do not match")



def update_password_in_database(email, new_password):
    print(email,new_password)
    try:
        # Connect to the database
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()

        # Update the password in the database
        c.execute("UPDATE users SET password = ? WHERE email = ?", (new_password, email))

        # Commit the transaction
        conn.commit()
        
        # Close the database connection
        conn.close()
        
        messagebox.showinfo("Success", "Password updated successfully!")
        return True  # Return True to indicate successful password update
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return False  # Return False to indicate failure

def resend_mail_forget():
    email = forget_email_entry.get()
    global otp  
    otp = generate_token()
    
    result2 = resend_otp(email, otp)
    messagebox.showinfo("Success", result2)






def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x_offset = (window.winfo_screenwidth() - width) // 2
    y_offset = (window.winfo_screenheight() - height) // 2
    window.geometry(f"+{x_offset}+{y_offset - 20}") 

def update_progress(check_vars):
    total_items = len(checklist_items)
    checked_items = sum(var.get() for var in check_vars)
    progress = (checked_items / total_items) * 100
    progressbar["value"] = progress
    progressbar_admin['value'] = progress



# Login window
login_window = Tk()
login_window.title("Login")
login_window.geometry("800x600")
center_window(login_window)

login_label = Label(login_window, text="Sign in to your account", font=("Arial", 18))
login_label.place(relx=0.5, rely=0.2, anchor=CENTER)

email_label = Label(login_window, text="Email", font=("Arial", 12))
email_label.place(relx=0.3, rely=0.35)
email_frame = Frame(login_window)
email_frame.place(relx=0.3, rely=0.4, relwidth=0.4)
email_entry_log = Entry(email_frame, font=("Arial", 12))
email_entry_log.pack(fill=BOTH, ipadx=5, ipady=5)

password_label = Label(login_window, text="Password", font=("Arial", 12))
password_label.place(relx=0.3, rely=0.5)
password_frame = Frame(login_window)
password_frame.place(relx=0.3, rely=0.55, relwidth=0.4)
password_entry_log = Entry(password_frame, show="*", font=("Arial", 12))
password_entry_log.pack(fill=BOTH, ipadx=5, ipady=5)

forget_label = Label(login_window, text="Forgot Password?", font=("Arial", 10), fg="blue", cursor="hand2")
forget_label.place(relx=0.3, rely=0.6)
forget_label.bind("<Button-1>", forgot_password)

login_button = Button(login_window, text="Login", width=10, font=("Arial", 12), bg="blue", fg="white", padx=10, pady=5, command=login)
login_button.place(relx=0.5, rely=0.75, anchor=CENTER, relwidth=0.4)

create_account_label = Label(login_window, text="Not a member? Create account", font=("Arial", 10), fg="blue", cursor="hand2")
create_account_label.place(relx=0.5, rely=0.85, anchor=CENTER)
create_account_label.bind("<Button-1>", lambda event: create_account())

# login_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))

# Register window
register_window = Toplevel()
register_window.title("Register")
register_window.geometry("800x600")
center_window(register_window)
register_window.withdraw()  # Hide the register window initially

arrow_img = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\arrow.png")
arrow_img = arrow_img.subsample(4) 

back_arrow_label = Label(register_window, image=arrow_img)
back_arrow_label.place(relx=0.02, rely=0.02, anchor=NW)
back_arrow_label.bind("<Button-1>", lambda event: back_to_login())

register_label = Label(register_window, text="Register Page", font=("Arial", 18))
register_label.place(relx=0.5, rely=0.1, anchor=CENTER)

name_label = Label(register_window, text="Full name", font=("Arial", 12))
name_label.place(relx=0.3, rely=0.2)
name_frame = Frame(register_window)
name_frame.place(relx=0.3, rely=0.25, relwidth=0.4)
name_entry = Entry(name_frame, font=("Arial", 12))
name_entry.pack(fill=BOTH, ipadx=5, ipady=5)

roles_label = Label(register_window, text="Select Role", font=("Arial", 12))
roles_label.place(relx=0.3, rely=0.33)
roles_frame = Frame(register_window)
roles_frame.place(relx=0.45, rely=0.32, relwidth=0.25)
roles_combobox = ttk.Combobox(roles_frame, values=["Applicant", "Staff", "Committee Member","Instructor","admin"], font=("Arial", 12), state="readonly")
roles_combobox.pack(fill=BOTH, ipadx=5, ipady=5)

email_label = Label(register_window, text="Email", font=("Arial", 12))
email_label.place(relx=0.3, rely=0.39)
email_frame = Frame(register_window)
email_frame.place(relx=0.3, rely=0.44, relwidth=0.4)
email_entry = Entry(email_frame, font=("Arial", 12))
email_entry.pack(fill=BOTH, ipadx=5, ipady=5)

password_label = Label(register_window, text="Password", font=("Arial", 12))
password_label.place(relx=0.3, rely=0.5)
password_frame = Frame(register_window)
password_frame.place(relx=0.3, rely=0.55, relwidth=0.4)
password_entry_reg = Entry(password_frame, show="*", font=("Arial", 12))
password_entry_reg.pack(fill=BOTH, ipadx=5, ipady=5)

confirm_label = Label(register_window, text="Confirm password", font=("Arial", 12))
confirm_label.place(relx=0.3, rely=0.6)
confirm_frame = Frame(register_window)
confirm_frame.place(relx=0.3, rely=0.65, relwidth=0.4)
confirm_entry = Entry(confirm_frame, show="*", font=("Arial", 12))
confirm_entry.pack(fill=BOTH, ipadx=5, ipady=5)

register_button = Button(register_window, text="Register", width=10, font=("Arial", 12), bg="blue", fg="white", padx=10, pady=5, command=register)
register_button.place(relx=0.5, rely=0.8, anchor=CENTER)

login_account_label = Label(register_window, text="Already have an account? Log in", font=("Arial", 10), fg="blue", cursor="hand2")
login_account_label.place(relx=0.5, rely=0.9, anchor=CENTER)
login_account_label.bind("<Button-1>", lambda event: back_to_login())

# register_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))


# OTP verification window
otp_window = Toplevel()
otp_window.title("OTP Verification")
otp_window.geometry("400x200")
center_window(otp_window)
otp_window.withdraw()

otp_label = Label(otp_window, text="", font=("Arial", 12))
otp_label.pack()

otp_entry = Entry(otp_window, font=("Arial", 12))
otp_entry.pack()

verify_button = Button(otp_window, text="Verify OTP", command=verify_otp)
verify_button.pack()

resend_otp_label = Label(otp_window, text="Resend OTP", font=("Arial", 10), fg="blue", cursor="hand2")
resend_otp_label.place(relx=0.27, rely=0.6, anchor=W)
resend_otp_label.bind("<Button-1>", lambda event: resend())


 
    
    
forget_window = Toplevel()
forget_window.title("OTP Verification")
forget_window.geometry("400x200")
center_window(forget_window)
forget_window.withdraw()

email_label = Label(forget_window, text="Enter Email", font=("Arial", 12))
email_label.pack()

forget_email_entry = Entry(forget_window, font=("Arial", 12))
forget_email_entry.pack()

verify_button = Button(forget_window, text="Check Email", command=verify_user_email)
verify_button.pack()



forget_otp_window = Toplevel()
forget_otp_window.title("OTP Verification")
forget_otp_window.geometry("400x200")
center_window(forget_otp_window)
forget_otp_window.withdraw()

otp_label = Label(forget_otp_window, text="", font=("Arial", 12))
otp_label.pack()

otp_entry_forget = Entry(forget_otp_window, font=("Arial", 12))
otp_entry_forget.pack()

verify_button = Button(forget_otp_window, text="Verify OTP", command=verify_otp_forget)
verify_button.pack()

resend_otp_label = Label(forget_otp_window, text="Resend OTP", font=("Arial", 10), fg="blue", cursor="hand2")
resend_otp_label.place(relx=0.27, rely=0.6, anchor=W)
resend_otp_label.bind("<Button-1>", lambda event: resend())


def on_double_click_verified(event):
    print("call")
    selection = table_verified.selection()
    if selection:
        item = selection[0]
        email = table_verified.item(item, "values")[0]
        admin_db.unverify_user(email)
        admin_db.Re_unverified_user(table_verified)
        

def on_double_click_unverified(event):
    print("call")
    selection = table_unverified.selection()
    if selection:
        item = selection[0]
        email = table_unverified.item(item, "values")[0]
        admin_db.verify_user(email)
        admin_db.reload_data(table_unverified)
        


def course_page():
    home_window.withdraw()
    verified_window.withdraw()
    course_home.withdraw()
    unverified_window.withdraw()
    course_home.deiconify()


def show_unverified_frame():
    home_window.withdraw()
    verified_window.withdraw()
    course_home.withdraw()
    admin_db.reload_data(table_unverified)
    unverified_window.deiconify()
   

def show_home_frame():
    verified_window.withdraw()
    course_home.withdraw()
    unverified_window.withdraw()
    home_window.deiconify()

def show_verified_frame():
    unverified_window.withdraw()
    home_window.withdraw()
    course_home.withdraw()
    admin_db.Re_unverified_user(table_verified)
    verified_window.deiconify()




def logout():
    global login_email  # Declare login_email as a global variable
    login_mail_result = logout_user(login_email)
    login_email = None  # Reset login_email after logout
    print("Logged out successfully")
    admin_applicant_chart_window.withdraw()
    view_home_window.withdraw
    otp_window.withdraw()
    register_window.withdraw()
    applicant_window.withdraw()
    home_window.withdraw()
    course_submission_window.withdraw()
    submission_window.withdraw()
    verified_window.withdraw()
    course_home.withdraw()
    committee_course_home.withdraw()
    login_window.deiconify()



check_vars=[]

def on_click_applicant(event):
    
    print("select")
    
    admin_applicant_chart_window.deiconify()
    home_window.withdraw()
    
    
    # Fetch the selected applicant's email and course name
    selection = table_applicant.selection()
    if selection:
        item = selection[0]
        # global email
        email, course_name = [table_applicant.item(item, "values")[i] for i in [0, 1]]
        
        print("Email:", email)
        print("Course Name:", course_name)

        # Fetch details of the applicant using their email and course name from the database
        applicant_details = fetch_applicant_details(email, course_name)
        
        load_checklist_admin(email,course_name)
        # load_approval_buttons(email)
        
        print(applicant_details)
        
        if applicant_details:
            name = applicant_details['name']
            course = applicant_details['course']
            cv_path = applicant_details['cv_path']
        
            # Populate fields in the application_chart_committee window
            name_label_admin.config(text=f"Name: {name}")
            email_label_admin.config(text=f"Email: {email}")
            course_label_admin.config(text=f"Course: {course}")
        
            # Function to open CV when view button is clicked
            def view_cv():
                if cv_path:
                    if os.path.exists(cv_path):
                        try:
                            os.startfile(cv_path)
                        except Exception as e:
                            print("Error opening CV file:", e)
                    else:
                        print("CV file does not exist:", cv_path)
                else:
                    print("No CV path found for the provided email.")
                pass
        
            # Bind view_cv function to View CV button
            view_cv_button_admin.config(command=view_cv)
        else:
            print("Applicant details not found in the database.")
    
    # Open the application_chart_committee window
  
    
    
home_window = Toplevel()
home_window.title("Home")
home_window.geometry("800x600")
center_window(home_window)
home_window.withdraw() 

frame_home = Frame(home_window)
frame_home.pack(fill=BOTH, expand=True)

# Create a navigation bar frame

navbar_frame_home = Frame(frame_home,bg="light blue", height=50)
navbar_frame_home.pack(fill=X)

# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_home, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)

home_frame_logo = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
home_frame_logo = home_frame_logo.subsample(4)
home_logo_label = Label(navbar_frame_home, image=home_frame_logo)
home_logo_label.pack(side="left", padx=10, pady=10)

# Add navigation buttons to the navbar frame
logout_button = Button(navbar_frame_home, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

verified_button = Button(navbar_frame_home, text="Verified",  command=show_verified_frame)
verified_button.pack(side=RIGHT, padx=5, pady=10)

unverifed_button = Button(navbar_frame_home, text="Unverifed", command=show_unverified_frame)
unverifed_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(navbar_frame_home, text="Courses", command=course_page)
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(navbar_frame_home, text="Application", command=show_home_frame)
application_button.pack(side=RIGHT, padx=5, pady=10)

# From

def on_enter_applicant(event):
    applicant_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave_applicant(event):
    applicant_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves
    
applicant_label = Label(frame_home, text="Applicant", font=("Arial", 18),relief=SOLID, borderwidth=1)
applicant_label.pack(padx=1, pady=10)

# Bind events for hover effect
applicant_label.bind("<Enter>", on_enter_applicant)
applicant_label.bind("<Leave>", on_leave_applicant)


# Define columns
columns_applicant = ("Email", "Course Name", "Status", "cv")

# Create the treeview with columns for unverified users
table_applicant = ttk.Treeview(frame_home, columns=columns_applicant, show="headings")

# Define column headings for unverified users
for col in columns_applicant:
    table_applicant.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_applicant:
    table_applicant.column(col, stretch=True)

# Define tag configuration for unverified users
table_applicant.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
table_applicant.bind("<Double-1>", on_click_applicant)

# Pack the table to fill both width and height of the window for unverified users
table_applicant.pack(fill="both", expand=True)

admin_db.applicant_data(table_applicant)


home_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))
# till




# course page 


def on_mousewheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


course_home = tk.Toplevel()
course_home.title("Course")
course_home.geometry("800x600")
center_window(course_home)
course_home.withdraw()

frame_course = Frame(course_home)
frame_course.pack(fill=BOTH, expand=True)


course_nav_bar = Frame(frame_course, bg="light blue", height=50)
course_nav_bar.pack(fill="x")

course_logo_image = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
course_logo_image = course_logo_image.subsample(4)
course_logo_label = Label(course_nav_bar, image=course_logo_image)
course_logo_label.pack(side="left", padx=10, pady=10)


# Add navigation buttons to the navbar frame
logout_button = Button(course_nav_bar, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

verified_button = Button(course_nav_bar, text="Verified",  command=show_verified_frame)
verified_button.pack(side=RIGHT, padx=5, pady=10)

unverifed_button = Button(course_nav_bar, text="Unverifed", command=show_unverified_frame)
unverifed_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(course_nav_bar, text="Courses", command=course_page)
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(course_nav_bar, text="Application", command=show_home_frame)
application_button.pack(side=RIGHT, padx=5, pady=10)

# From

def on_enter_applicant(event):
    applicant_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave_applicant(event):
    applicant_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves
    
applicant_label = Label(frame_course, text="Course", font=("Arial", 18),relief=SOLID, borderwidth=1)
applicant_label.pack(padx=1, pady=10)

# Bind events for hover effect
applicant_label.bind("<Enter>", on_enter_applicant)
applicant_label.bind("<Leave>", on_leave_applicant)


def add_course():
    def save_course():
        # Get the values entered by the user
        course_name = course_name_entry.get()
        course_description = course_description_entry.get()

        # Insert the new course into the database
        admin_db.insert_course(course_name, course_description)

        for item in table_course.get_children():
            table_course.delete(item)
        
        admin_db.fetch_courses_admin_db(table_course)
    
        
        add_course_window.destroy()

    # Create a new window for adding a course
    add_course_window = Toplevel()
    add_course_window.title("Add Course")
    add_course_window.geometry("400x200")
    center_window(add_course_window)

    # Labels and entry fields for course name and description
    course_name_label = Label(add_course_window, text="Course Name:", font=("Arial", 12))
    course_name_label.pack()
    course_name_entry = Entry(add_course_window, font=("Arial", 12))
    course_name_entry.pack()

    course_description_label = Label(add_course_window, text="Description:", font=("Arial", 12))
    course_description_label.pack()
    course_description_entry = Entry(add_course_window, font=("Arial", 12))
    course_description_entry.pack()

    # Button to save the course
    save_button = Button(add_course_window, text="Save", command=save_course)
    save_button.pack()


add_course_button = tk.Button(frame_course, text="Add Course", command=add_course, font=("Arial", 14))
add_course_button.pack(side="bottom", padx=10, pady=10, anchor="e")

# Define columns
columns_applicant = ("Id", "Course name", "Description")

# Create the treeview with columns for unverified users
table_course = ttk.Treeview(frame_course, columns=columns_applicant, show="headings")

# Define column headings for unverified users
for col in columns_applicant:
    table_course.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_applicant:
    table_course.column(col, stretch=True)

# Define tag configuration for unverified users
table_course.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
# table_course.bind("<Double-1>", on_click_applicant)

# Pack the table to fill both width and height of the window for unverified users
table_course.pack(fill="both", expand=True)

# Fetch and display courses
admin_db.fetch_courses_admin_db(table_course)

# Set padding for rows and columns
style = ttk.Style()
style.configure("Treeview", rowheight=50, padding=10)

# Set column width for ID column
table_course.column("Id", width=50)  # Adjust the width as needed


table_course.column("Description", width=300) 



course_home.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))


# course page end


# Unverified Window
unverified_window = Toplevel()
unverified_window.title("Unverified")
unverified_window.geometry("800x600")
center_window(unverified_window)
unverified_window.withdraw()

frame_unverified = Frame(unverified_window)
frame_unverified.pack(fill=BOTH, expand=True)

navbar_frame_unverified = Frame(frame_unverified, bg="light blue", height=50)
navbar_frame_unverified.pack(fill=X)


# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_unverified, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)

logo_image_unverified = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
logo_image_unverified = logo_image_unverified.subsample(4)
logo_label = Label(navbar_frame_unverified, image=logo_image_unverified)
logo_label.pack(side="left", padx=10, pady=10)

logout_button = Button(navbar_frame_unverified, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

verified_button = Button(navbar_frame_unverified, text="Verified",  command=show_verified_frame)
verified_button.pack(side=RIGHT, padx=5, pady=10)

unverifed_button = Button(navbar_frame_unverified, text="Unverifed", command=show_unverified_frame)
unverifed_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(navbar_frame_unverified, text="Courses",command=course_page)
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(navbar_frame_unverified, text="Application", command=show_home_frame)
application_button.pack(side=RIGHT, padx=5, pady=10)


def on_enter(event):
    unverified_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave(event):
    unverified_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves



# Create the submission label with initial border
unverified_label = Label(frame_unverified, text="Unverified account", font=("Arial", 18),relief=SOLID, borderwidth=1)
unverified_label.pack(padx=1, pady=10)

# Bind events for hover effect
unverified_label.bind("<Enter>", on_enter)
unverified_label.bind("<Leave>", on_leave)


# Define columns
columns_unverified = ("Email", "Name", "Role", "Action")

# Create the treeview with columns for unverified users
table_unverified = ttk.Treeview(frame_unverified, columns=columns_unverified, show="headings")

# Define column headings for unverified users
for col in columns_unverified:
    table_unverified.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_unverified:
    table_unverified.column(col, stretch=True)

# Define tag configuration for unverified users
table_unverified.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
table_unverified.bind("<Double-1>", on_double_click_unverified)

# Pack the table to fill both width and height of the window for unverified users
table_unverified.pack(fill="both", expand=True)

admin_db.reload_data(table_unverified)


unverified_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))




# Verified Window
verified_window = Toplevel()
verified_window.title("Verified")
verified_window.geometry("800x600")
center_window(verified_window)
verified_window.withdraw()

verified_frame = Frame(verified_window)
verified_frame.pack(fill=BOTH, expand=True)

navbar_frame_verified = Frame(verified_frame, bg="light blue", height=50)
navbar_frame_verified.pack(fill=X)

# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_verified, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)


logo_image_verified = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
logo_image_verified = logo_image_verified.subsample(4)
logo_label_verified = Label(navbar_frame_verified, image=logo_image_verified)
logo_label_verified.pack(side="left", padx=10, pady=10)


logout_button = Button(navbar_frame_verified, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

verified_button = Button(navbar_frame_verified, text="Verified",  command=show_verified_frame)
verified_button.pack(side=RIGHT, padx=5, pady=10)

unverifed_button = Button(navbar_frame_verified, text="Unverifed", command=show_unverified_frame)
unverifed_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(navbar_frame_verified, text="Courses", command=course_page)
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(navbar_frame_verified, text="Application", command=show_home_frame)
application_button.pack(side=RIGHT, padx=5, pady=10)


def on_enter(event):
    submission_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave(event):
    submission_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves



# Create the submission label with initial border
submission_label = Label(verified_frame, text="Verified Account", font=("Arial", 18),relief=SOLID, borderwidth=1)
submission_label.pack(padx=1, pady=10)

# Bind events for hover effect
submission_label.bind("<Enter>", on_enter)
submission_label.bind("<Leave>", on_leave)


# Define columns for verified users
columns_verified = ("Email", "Name", "Role", "Action")
table_verified = ttk.Treeview(verified_frame, columns=columns_verified, show="headings")

# Define column headings for verified users
for col in columns_verified:
    table_verified.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for verified users
for col in columns_verified:
    table_verified.column(col, stretch=True)

# Define action for verifying user for verified users
table_verified.bind("<Double-1>", on_double_click_verified)

# Pack the table to fill both width and height of the window for verified users
table_verified.pack(fill="both", expand=True)

# Load data initially for verified users
admin_db.Re_unverified_user(table_verified)

verified_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))






# applicant_chart_window



def fetch_applicant_details(email, course_name):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, course_name, cv_path FROM applicants WHERE email=? AND course_name=?", (email, course_name))
    applicant_details = cursor.fetchone()
    conn.close()
    if applicant_details:
        return {'name': applicant_details[0], 'course': applicant_details[1], 'cv_path': applicant_details[2]}
    else:
        return None

    
  
def open_application(event=None):
    admin_db.applicant_data(table_applicant)
    home_window.deiconify()
    admin_applicant_chart_window.withdraw()
    
# def send_mail_client():
#     email_text = email_label_admin.cget("text")
#     course_text = course_label_admin.cget("text")
#     print("Email:", email_text)
#     print("Course:", course_text)
#     response = sendEmailToClient(email_text, course_text)
    
admin_applicant_chart_window = Toplevel()
admin_applicant_chart_window.title("View Window")
admin_applicant_chart_window.geometry("800x600")
center_window(admin_applicant_chart_window)
admin_applicant_chart_window.withdraw()


# Navigation bar
view_admin_nav_bar = Frame(admin_applicant_chart_window, bg="light blue", height=50)
view_admin_nav_bar.pack(fill=X)

view_page_logo = Label(view_admin_nav_bar, text="Logo")
view_page_logo.pack(side=LEFT, padx=10, pady=10)

logout_button = Button(view_admin_nav_bar, text="Logout", font=("Arial", 12), command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

career_button = Button(view_admin_nav_bar, text="Career", font=("Arial", 12))
career_button.pack(side=RIGHT, padx=5, pady=10)

applicant_button = Button(view_admin_nav_bar, text="Application", font=("Arial", 12), command=open_application)
applicant_button.pack(side=RIGHT, padx=5, pady=10)

# Scrollbar and Canvas
scrollbar_admin = Scrollbar(admin_applicant_chart_window, orient=VERTICAL)
scrollbar_admin.pack(side=RIGHT, fill=Y)

chart_canvas = Canvas(admin_applicant_chart_window, yscrollcommand=scrollbar_admin.set)
chart_canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar_admin.config(command=chart_canvas.yview)

# Frame inside the canvas
views_frame = Frame(chart_canvas)
chart_canvas.create_window((0, 0), window=views_frame, anchor="nw")

# Heading
heading_label = Label(views_frame, text="Details", font=("Arial", 16))
heading_label.pack(pady=(20, 10), anchor="w", padx=20)

# Name input field
name_label_admin = Label(views_frame, text="Name : Name of the user", font=("Arial", 12))
name_label_admin.pack(anchor="w", padx=20, pady=5)

# Email input field
email_label_admin = Label(views_frame, text="Email", font=("Arial", 12))
email_label_admin.pack(anchor="w", padx=20, pady=5)

# Course input field
course_label_admin = Label(views_frame, text="Course", font=("Arial", 12))
course_label_admin.pack(anchor="w", padx=20, pady=5)

# CV heading
cv_heading_label_admin = Label(views_frame, text="CV", font=("Arial", 14))
cv_heading_label_admin.pack(pady=(20, 10), anchor="w", padx=20)

# View CV button
view_cv_button_admin = Button(views_frame, text="View", font=("Arial", 12))
view_cv_button_admin.pack(anchor="w", padx=20)

# Checklist
checklist_label = Label(views_frame, text="Checklist", font=("Arial", 16))
checklist_label.pack(pady=(20, 10), anchor="w", padx=20)

progressbar_admin = ttk.Progressbar(views_frame, orient=HORIZONTAL, length=200, mode='determinate')
progressbar_admin.pack(pady=20, padx=20, anchor="w")


checklist_items = [
    "Bachelor's degree in a relevant field",
    "Prior teaching experience",
    "Ability to work collaboratively",
    "Organizational skills",
    "Certifications and Training",
    "Additional Qualifications"
]



def load_checklist_admin(email, course_name):
    # Check if the checklist has already been created
    if not check_vars:
        # Checklist has not been created, so create it
        for item in checklist_items:
            var = IntVar()
            check_vars.append(var)
            # checkbutton_admin = Checkbutton(views_frame, text=item, font=("Arial", 12), variable=var)

            checkbutton_admin = Checkbutton(views_frame, text=item, font=("Arial", 12), variable=var, command=lambda: update_progress(check_vars))
            checkbutton_admin.pack(anchor="w", padx=20)
    else:
        # Clear existing check_vars
        for var in check_vars:
            var.set(0)  # Reset all variables to 0

    # Check if the "Send Email" button has already been created
    # if not hasattr(load_checklist_admin, 'send_mail_button'):
    #     # "Send Email" button has not been created, so create it
    #     send_mail_button = Button(views_frame, text="Send Email", font=("Arial", 12), command=send_mail_client)
    #     send_mail_button.pack(padx=5, pady=10)
    #     # Store the button reference as an attribute of the function
    #     load_checklist_admin.send_mail_button = send_mail_button

    # Update progress bar
    update_progress(check_vars)

    # Check if the checklist exists and needs to be updated
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT checklist FROM applicants WHERE email=? AND course_name=?", (email, course_name))
    checklist_str = c.fetchone()
    conn.close()

    # Update check_vars with new checklist items
    if checklist_str is not None and checklist_str[0] is not None:
        selected_items = checklist_str[0].split("\n")
        for i, item in enumerate(checklist_items):
            var = IntVar(value=1 if item in selected_items else 0)
            check_vars[i].set(var.get())  # Update existing variables with new values

    update_progress(check_vars)





# Configure scrollregion
chart_canvas.update_idletasks()
chart_canvas.config(scrollregion=chart_canvas.bbox("all"))

# Linking scrollbar to canvas
scrollbar_admin.config(command=chart_canvas.yview)

# Make scrollbar visible only when needed
chart_canvas.bind("<Configure>", lambda e: chart_canvas.configure(scrollregion=chart_canvas.bbox("all")))

# Adjusting scrollbar as per canvas size
chart_canvas.bind("<Configure>", lambda e: scrollbar_admin.pack_forget() if chart_canvas.winfo_height() >= chart_canvas.bbox("all")[3] else scrollbar_admin.pack(side=RIGHT, fill=Y))

# Function to update scroll region when the content changes
def update_scrollregion(event):
    chart_canvas.configure(scrollregion=chart_canvas.bbox("all"))

# Bind the update_scrollregion function to the frame's children and size changes
views_frame.bind("<Configure>", update_scrollregion)


admin_applicant_chart_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))

# close




# applicant_window


def on_frame_enter(event):
    frame = event.widget
    frame.config(bg="light blue")
    if hasattr(frame, 'label'):
        frame.label.config(bg="light blue")
    if hasattr(frame, 'definition_label'):
        frame.definition_label.config(bg="light blue")

def on_frame_leave(event):
    frame = event.widget
    frame.config(bg="white")
    if hasattr(frame, 'label'):
        frame.label.config(bg="white")
    if hasattr(frame, 'definition_label'):
        frame.definition_label.config(bg="white")

def create_border_frame(parent, pady):
    frame = tk.Frame(parent, highlightbackground="light blue", highlightthickness=1, padx=10, pady=10, bg="white")
    frame.pack(fill=tk.BOTH, padx=10, pady=pady)
    return frame

def on_button_enter(event):
    event.widget.config(bg="light blue")

def on_button_leave(event):
    event.widget.config(bg="white")



def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    sub_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
def deep_on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    deep_canvas.yview_scroll(int(-1*(event.delta/120)), "units")



# Function to handle "Submission" button click
def submission_button_click():
    submission_window.deiconify()
    admin_db.applicant_file(table_submission_app)
    admin_db.applicant_data(table_applicant)
    applicant_window.withdraw()
    course_submission_window.withdraw()

def career_button_click():
    applicant_window.deiconify()
    submission_window.withdraw() 
    course_submission_window.withdraw()



def create_frame(frame, frame_number, label_text, definition_text):
    label = Label(frame, text=label_text, font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    frame.label = label  

    definition = Label(frame, text=definition_text, font=("Arial", 12), wraplength=500, justify="left")
    definition.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
    frame.definition_label = definition

    button = Button(frame, text="Apply Now →", font=("Arial", 12))
    button.grid(row=2, column=0, sticky="w", padx=10, pady=10)
    button.bind("<Enter>", on_button_enter)
    button.bind("<Leave>", on_button_leave)
    button.bind("<Button-1>", lambda event, name=course_name: on_button_click(event, name))




def adjust_text_position(event):
    screen_width = applicant_window.winfo_width()
    rel_x = 0.2
    rel_y = 0.2
        
    if text_label.winfo_exists():
        text_width = text_label.winfo_reqwidth()
        x_offset = 0.5 * (1 + rel_x) * screen_width - 0.48 * text_width
        y_offset = 0

        text_label.place(relx=rel_x, rely=rel_y, anchor=tk.CENTER, x=x_offset, y=y_offset)
        
        
        
    
applicant_window = Toplevel()
applicant_window.title("Applicant")
applicant_window.geometry("800x600")
center_window(applicant_window)
applicant_window.withdraw()

nav_bar = Frame(applicant_window, bg="light blue", height=50)
nav_bar.pack(fill=X)

logo_image = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
logo_image = logo_image.subsample(4)
logo_label = Label(nav_bar, image=logo_image)
logo_label.pack(side=LEFT, padx=10, pady=10)

logout_button = Button(nav_bar, text="Logout", font=("Arial", 12), command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

submission_button = Button(nav_bar, text="Submission", font=("Arial", 12), command=submission_button_click)
submission_button.pack(side=RIGHT, padx=5, pady=10)

career_button = Button(nav_bar, text="Career", font=("Arial", 12), command=career_button_click)
career_button.pack(side=RIGHT, padx=5, pady=10)

frame_home = Frame(applicant_window)
frame_home.pack(fill=BOTH, expand=True)

scrollbar =Scrollbar(frame_home, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

canvas = Canvas(frame_home, yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=canvas.yview)

inner_frame = Frame(canvas)

image_path = r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\bg_img.png"
img = PhotoImage(file=image_path)
img_label = Label(inner_frame, image=img)
img_label.pack()

text = "Join Our Team as a Teaching Assistant at A P Shah Institute of Technology\nExplore exciting opportunities to contribute to academic excellence! We're seeking\n dedicated individuals passionate about education to join us as Teaching Assistants\n at APSIT. Shape the future of learning and inspire students on their\n educational journey. Apply now to be a part of our dynamic team!"
text_label = Label(inner_frame, text=text, bg="white", font=("Arial", 14, "bold"))
text_label.pack()

applicant_window.bind("<Configure>", adjust_text_position)

heading_frame = Frame(inner_frame)
heading_frame.pack(side=TOP, fill=BOTH, padx=15, pady=25)

heading_border_frame = Frame(heading_frame, highlightbackground="black", highlightthickness=1, padx=5, pady=5)
heading_border_frame.pack(side=LEFT)

heading_label = Label(heading_border_frame, text="Open Positions", font=("Arial", 18))
heading_label.pack(padx=15, pady=(10, 5)) 

button_frame = Frame(inner_frame)
button_frame.pack(side=BOTTOM, fill=BOTH, padx=10, pady=10, anchor=E, expand=True)


def load_courses():
    global courses
    courses = None
    courses = admin_db.fetch_courses_applicant_db()
    
load_courses()

frame_functions = {}

global_course_name = None

def on_button_click(event, course_name):
    global global_course_name
    global_course_name = course_name
    
    applicant_window.withdraw()
    course_submission_window.deiconify()
        
for id, course_name, description in courses:
    frame = create_border_frame(button_frame, pady=20)
    frame.bind("<Enter>", on_frame_enter)
    frame.bind("<Leave>", on_frame_leave)
    create_frame(frame, id, course_name, description)
    frame_functions[id] = lambda num=id, name=course_name: on_button_click(num, name)


canvas.create_window((0, 0), window=inner_frame, anchor="nw")
canvas.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))
canvas.bind_all("<MouseWheel>", on_mousewheel)


applicant_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))


# from here





submission_window = Toplevel()
submission_window.title("Submission Window")
submission_window.geometry("800x600")
center_window(submission_window)
submission_window.withdraw()  # Hide the Home window

frame_submission = Frame(submission_window)
frame_submission.pack(fill=BOTH, expand=True)

# Create a navigation bar frame
navbar_frame_sub = Frame(frame_submission, bd=1, relief=SUNKEN)
navbar_frame_sub.pack(side=TOP, fill=X)

# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_sub, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)

logo_image_home = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
logo_image_home = logo_image_home.subsample(4)
logo_label = Label(navbar_frame_sub, image=logo_image_home)
logo_label.pack(side=LEFT)

# Add navigation buttons to the navbar frame
logout_button = Button(navbar_frame_sub, text="Logout", font=("Arial", 12), command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

submission_button = Button(navbar_frame_sub, text="Submission", font=("Arial", 12), command=submission_button_click)
submission_button.pack(side=RIGHT, padx=5, pady=10)

career_button = Button(navbar_frame_sub, text="Career", font=("Arial", 12), command=career_button_click)
career_button.pack(side=RIGHT, padx=5, pady=10)



def on_enter_sub(event):
    applicant_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave_sub(event):
    applicant_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves
    
applicant_label = Label(frame_submission, text="Applicant", font=("Arial", 18),relief=SOLID, borderwidth=1)
applicant_label.pack(padx=1, pady=10)

# Bind events for hover effect
applicant_label.bind("<Enter>", on_enter_sub)
applicant_label.bind("<Leave>", on_leave_sub)


# Define columns
columns_applicant = ("Email", "Course Name", "Status", "cv")

# Create the treeview with columns for unverified users
table_submission_app = ttk.Treeview(frame_submission, columns=columns_applicant, show="headings")

# Define column headings for unverified users
for col in columns_applicant:
    table_submission_app.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_applicant:
    table_submission_app.column(col, stretch=True)

# Define tag configuration for unverified users
table_submission_app.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
table_submission_app.bind()

# Pack the table to fill both width and height of the window for unverified users
table_submission_app.pack(fill="both", expand=True)

admin_db.applicant_file(table_submission_app)


submission_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))



# till



# course_submission_window

cv_path = None

def browse_cv():
    global cv_path
    cv_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if cv_file:
        cv_path = cv_file 
        
def check_duplicate(email, course_name):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM applicants WHERE email = ? AND course_name = ?''', (email, course_name))
    result = c.fetchone()
    conn.close()
    return result

def submit_form():
    global cv_path
    global login_email  # Declare login_email as a global variable
    global global_course_name
    
    cv_path_value = cv_path
    if cv_path_value:
        # Create the cv_folder if it doesn't exist
        if not os.path.exists("cv_folder"):
            os.makedirs("cv_folder")

        # Fetch name from users table based on login_email
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE email = ?", (login_email,))
        result = c.fetchone()
        conn.close()

        
        
        if result:
            
            name = result[0]  # Extracting name from the result
            experience = ta_var.get()

            existing_record = check_duplicate(login_email, global_course_name)
            
            if not existing_record:
                
                 # Move the CV file to the cv_folder
                cv_filename = os.path.basename(cv_path_value)
                target_path = os.path.join("cv_folder", cv_filename)
                shutil.copy(cv_path_value, target_path)
                
                # Insert applicant information into the applicants table
                conn = sqlite3.connect('user_database.db')
                c = conn.cursor()
                c.execute('''INSERT INTO applicants (name, email, cv_path, experience, course_name, status) VALUES (?, ?, ?, ?, ?, ?)''', (name, login_email, target_path, experience, global_course_name, "Recommended"))
                
                global_course_name = None
                
                conn.commit()
                conn.close()

            
                messagebox.showinfo("Success", "Form submitted successfully!")
            else:
                messagebox.showerror("Error", "A user with the same email and course name already exists.")
        else:
            messagebox.showerror("Error", "User not found for the given email.")
    else:
        messagebox.showerror("Error", "Please select a CV file.")
        


# Create the course_submission window

course_submission_window = Toplevel()
course_submission_window.title("Deep Learning")
course_submission_window.geometry("800x600")
center_window(course_submission_window)
course_submission_window.withdraw()


deep_nav_bar = Frame(course_submission_window, bg="light blue", height=50)
deep_nav_bar.pack(fill=X)

deep_logo_image = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
deep_logo_image = deep_logo_image.subsample(4)
deep_logo_label = Label(deep_nav_bar, image=deep_logo_image)
deep_logo_label.pack(side=LEFT, padx=10, pady=10)

logout_button = Button(deep_nav_bar, text="Logout", font=("Arial", 12), command= logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

submission_button = Button(deep_nav_bar, text="Submission", font=("Arial", 12), command=submission_button_click)
submission_button.pack(side=RIGHT, padx=5, pady=10)

career_button = Button(deep_nav_bar, text="Career", font=("Arial", 12), command=career_button_click)
career_button.pack(side=RIGHT, padx=5, pady=10)

# Deep Learning Frame
deeplearning_frame = Frame(course_submission_window)
deeplearning_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Scrollbar for the Deep Learning Frame
deep_scrollbar = Scrollbar(deeplearning_frame, orient=VERTICAL)
deep_scrollbar.pack(side=RIGHT, fill=Y)

# Canvas for Deep Learning Frame
deep_canvas = Canvas(deeplearning_frame, yscrollcommand=deep_scrollbar.set)
deep_canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Configure Scrollbar
deep_scrollbar.config(command=deep_canvas.yview)

# Frame for Scrollable Content
deep_inner_frame = Frame(deep_canvas)
deep_canvas.create_window((0, 0), window=deep_inner_frame, anchor="nw")

# Bind Mousewheel Event
deep_canvas.bind_all("<MouseWheel>", deep_on_mousewheel)

# Form Labels and Entry Widgets
label1 = Label(deep_inner_frame, text="Are you a passionate deep learning enthusiast?", font=("Arial", 14, "bold"), anchor="w")
label1.pack(pady=(20, 10), anchor="w")

label2_text = "Unlock the next level of your career by becoming a vital part of our cutting-edge Deep Learning team at North University. We're on the lookout for skilled individuals well-versed in frameworks like TensorFlow and PyTorch, with a strong background in neural networks and machine learning algorithms."
label2 = Label(deep_inner_frame, text=label2_text, font=("Arial", 12), wraplength=600, justify=LEFT, anchor="w")
label2.pack(pady=(0, 10), anchor="w")

label3 = Label(deep_inner_frame, text="Requirements", font=("Arial", 12, "bold"), anchor="w")
label3.pack(anchor="w")

requirements = [
    "Proficiency in Python programming",
    "Extensive knowledge of deep learning frameworks (TensorFlow, PyTorch)",
    "Hands-on experience with neural networks and machine learning algorithms",
    "Strong problem-solving skills in the realm of AI",
    "Ability to collaborate effectively with a multidisciplinary team"
]

for req in requirements:
    label = Label(deep_inner_frame, text=f"• {req}", font=("Arial", 12), wraplength=600, justify=LEFT, anchor="w")
    label.pack(anchor="w")

# Attach CV
attach_label = Label(deep_inner_frame, text="Attach your CV", font=("Arial", 14), anchor="w")
attach_label.pack(anchor="w", pady=(20, 10))

cv_frame = Frame(deep_inner_frame)
cv_frame.pack(anchor="w")

cv_button = Button(cv_frame, text="Browse", font=("Arial", 10),  command=browse_cv)
cv_button.pack(side=LEFT, padx=(5, 0))

# TA Experience
ta_experience_label = Label(deep_inner_frame, text="Do you have experience working as a TA?", font=("Arial", 12), anchor="w")
ta_experience_label.pack(anchor="w")

ta_var = IntVar()
ta_yes = Radiobutton(deep_inner_frame, text="Yes", variable=ta_var, value=1, font=("Arial", 12), anchor="w")
ta_no = Radiobutton(deep_inner_frame, text="No", variable=ta_var, value=0, font=("Arial", 12), anchor="w")
ta_yes.pack(anchor="w")
ta_no.pack(anchor="w")

# Form Buttons
# submit_button = Button(deep_inner_frame, text="Submit", font=("Arial", 12), command=submit_form)
submit_button = Button(deep_inner_frame, text="Submit", command=submit_form)

submit_button.pack(pady=20, anchor="w")


# Set Scrollregion
deep_inner_frame.update_idletasks()
deep_canvas.config(scrollregion=deep_canvas.bbox("all"))

course_submission_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))




# View window


def committee_course_window():
    committee_course_home.deiconify()
    course_home.withdraw()
    application_chart_committee.withdraw()
    unverified_window.withdraw()

global usercourse
usercourse = None


def fetch_applicant_details(email, course_name):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, course_name, cv_path FROM applicants WHERE email=? AND course_name=?", (email, course_name))
    applicant_details = cursor.fetchone()
    conn.close()
    if applicant_details:
        return {'name': applicant_details[0], 'course': applicant_details[1], 'cv_path': applicant_details[2]}
    else:
        return None


def on_click_applicant_committee(event):
    
    print("select")
    
    application_chart_committee.deiconify()
    view_home_window.withdraw()
    
    # Fetch the selected applicant's email and course name
    selection = table_committee.selection()
    if selection:
        item = selection[0]
        global email
        email, course_name = [table_committee.item(item, "values")[i] for i in [0, 1]]
        
        print("Email:", email)
        print("Course Name:", course_name)

        # Fetch details of the applicant using their email and course name from the database
        applicant_details = fetch_applicant_details(email, course_name)
        
        load_checklist(email, course_name)
        load_approval_buttons(email, course_name)
        
        print(applicant_details)
        
        if applicant_details:
            name = applicant_details['name']
            course = applicant_details['course']
            cv_path = applicant_details['cv_path']
            
            global usercourse
            
            usercourse = course
        
            # Populate fields in the application_chart_committee window
            name_label.config(text=f"Name: {name}")
            email_label.config(text=f"Email: {email}")
            course_label.config(text=f"Course: {course}")
        
            # Function to open CV when view button is clicked
            def view_cv():
                if cv_path:
                    if os.path.exists(cv_path):
                        try:
                            os.startfile(cv_path)
                        except Exception as e:
                            print("Error opening CV file:", e)
                    else:
                        print("CV file does not exist:", cv_path)
                else:
                    print("No CV path found for the provided email.")
                pass
        
            # Bind view_cv function to View CV button
            view_cv_button.config(command=view_cv)
        else:
            print("Applicant details not found in the database.")
    
    # Open the application_chart_committee window
    
        
def view_home_window_click(event=None):
    admin_db.applicant_data(table_committee)
    view_home_window.deiconify()
    application_chart_committee.withdraw()

    
view_home_window = Toplevel()
view_home_window.title("View Home")
view_home_window.geometry("800x600")
center_window(view_home_window)
view_home_window.withdraw()  # Hide the Home window

view_home = Frame(view_home_window)
view_home.pack(fill=BOTH, expand=True)

# Create a navigation bar frame
navbar_frame_view = Frame(view_home, bd=1, relief=SUNKEN)
navbar_frame_view.pack(side=TOP, fill=X)

# Create a bottom border for the navbar
bottom_border = Frame(navbar_frame_view, height=1, bg="black")
bottom_border.pack(side=BOTTOM, fill=X)

logo_image_home = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
logo_image_home = logo_image_home.subsample(4)
logo_label = Label(navbar_frame_view, image=logo_image_home)
logo_label.pack(side=LEFT)

# Add navigation buttons to the navbar frame
logout_button = Button(navbar_frame_view, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(navbar_frame_view, text="Courses", command=committee_course_window)
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(navbar_frame_view, text="Application")
application_button.pack(side=RIGHT, padx=5, pady=10)

# From

def on_enter_applicant(event):
    applicant_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave_applicant(event):
    applicant_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves

    
applicant_label = Label(view_home, text="Applicant", font=("Arial", 18),relief=SOLID, borderwidth=1)
applicant_label.pack(padx=1, pady=10)

# Bind events for hover effect
applicant_label.bind("<Enter>", on_enter_applicant)
applicant_label.bind("<Leave>", on_leave_applicant)


# Define columns
columns_committee = ("Email", "Course Name", "Status", "cv")

# Create the treeview with columns for unverified users
table_committee = ttk.Treeview(view_home, columns=columns_committee, show="headings")

# Define column headings for unverified users
for col in columns_committee:
    table_committee.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_committee:
    table_committee.column(col, stretch=True)

# Define tag configuration for unverified users
table_committee.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
table_committee.bind("<Double-1>", on_click_applicant_committee)

# Pack the table to fill both width and height of the window for unverified users
table_committee.pack(fill="both", expand=True)

admin_db.applicant_data(table_committee)


view_home_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))

















# application_chart_committee

check_vars_committee=[]

checklist_items = [
    "Bachelor's degree in a relevant field",
    "Prior teaching experience",
    "Ability to work collaboratively",
    "Organizational skills",
    "Certifications and Training",
    "Additional Qualifications"
]


def update_database(status, email, usercourse):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''UPDATE applicants SET status = ? WHERE email = ? AND course_name = ?''', (status, email, usercourse))
    conn.commit()
    conn.close()


def add_checklist(email, usercourse, checklist_items, check_vars_committee):
    selected_items = [item for item, var in zip(checklist_items, check_vars_committee) if var.get() == 1]
    checklist_str = "\n".join(selected_items)  # Convert the list of selected items to a string
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''UPDATE applicants SET checklist = ? WHERE email = ? AND course_name = ?''', (checklist_str, email, usercourse))
    conn.commit()
    conn.close()



    
def approve_action():
    update_database("Approved", email, usercourse)
    add_checklist(email, usercourse, checklist_items, check_vars_committee)
    messagebox.showinfo("Approval Status", "Application approved successfully!")
    load_approval_buttons(email, usercourse)

def disapprove_action():
    update_database("Disapproved", email, usercourse)
    add_checklist(email, usercourse, checklist_items)
    messagebox.showinfo("Approval Status", "Application disapproved successfully!")
    load_approval_buttons(email, usercourse)


def approve():
    update_status(c, conn, committe_frame, approved_button, disapproved_button, email, "Approved")
    load_approval_buttons(email, usercourse)

def disapprove():
    update_status(c, conn, committe_frame, approved_button, disapproved_button, email, "Disapproved")
    load_approval_buttons(email, usercourse)



application_chart_committee = Toplevel()
application_chart_committee.title("Committee View Window")
application_chart_committee.geometry("800x600")
center_window(application_chart_committee)
application_chart_committee.withdraw()


# Navigation bar
committee_nav_bar = Frame(application_chart_committee, bg="light blue", height=50)
committee_nav_bar.pack(fill=X)



committee_logo = Label(committee_nav_bar, text="Logo")
committee_logo.pack(side=LEFT, padx=10, pady=10)

logout_button = Button(committee_nav_bar, text="Logout", font=("Arial", 12), command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

career_button = Button(committee_nav_bar, text="Career", font=("Arial", 12), command=committee_course_window)
career_button.pack(side=RIGHT, padx=5, pady=10)

applicant_button = Button(committee_nav_bar, text="Application", font=("Arial", 12), command=view_home_window_click)
applicant_button.pack(side=RIGHT, padx=5, pady=10)

# Scrollbar and Canvas
scrollbar_committee = Scrollbar(application_chart_committee, orient=VERTICAL)
scrollbar_committee.pack(side=RIGHT, fill=Y)

committee_canvas = Canvas(application_chart_committee, yscrollcommand=scrollbar_committee.set)
committee_canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar_committee.config(command=committee_canvas.yview)

# Frame inside the canvas
committe_frame = Frame(committee_canvas)
committee_canvas.create_window((0, 0), window=committe_frame, anchor="nw")

# Heading
heading_label = Label(committe_frame, text="Details", font=("Arial", 16))
heading_label.pack(pady=(20, 10), anchor="w", padx=20)

# Name input field
name_label = Label(committe_frame, text="Name : Name of the user", font=("Arial", 12))
name_label.pack(anchor="w", padx=20, pady=5)

# Email input field
email_label = Label(committe_frame, text="Email", font=("Arial", 12))
email_label.pack(anchor="w", padx=20, pady=5)

# Course input field
course_label = Label(committe_frame, text="Course", font=("Arial", 12))
course_label.pack(anchor="w", padx=20, pady=5)

# CV heading
cv_heading_label = Label(committe_frame, text="CV", font=("Arial", 14))
cv_heading_label.pack(pady=(20, 10), anchor="w", padx=20)

# View CV button
view_cv_button = Button(committe_frame, text="View", font=("Arial", 12), command=on_click_applicant)
view_cv_button.pack(anchor="w", padx=20)

# Checklist
checklist_label = Label(committe_frame, text="Checklist", font=("Arial", 16))
checklist_label.pack(pady=(20, 10), anchor="w", padx=20)

progressbar = ttk.Progressbar(committe_frame, orient=HORIZONTAL, length=200, mode='determinate')
progressbar.pack(pady=20, padx=20, anchor="w")

def load_checklist(email, course_name):
    # Check if the checklist has already been created
    if not check_vars_committee:
        # Checklist has not been created, so create it
        for item in checklist_items:
            var = IntVar()
            check_vars_committee.append(var)
            checkbutton = Checkbutton(committe_frame, text=item, font=("Arial", 12), variable=var, command=lambda: update_progress(check_vars_committee))
            checkbutton.pack(anchor="w", padx=20)
    else:
        # Clear existing check_vars_committee
        for var in check_vars_committee:
            var.set(0)  # Reset all variables to 0

        
        update_progress(check_vars_committee)

    # # Update progress bar
    # update_progress()

    # Check if the checklist exists and needs to be updated
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT checklist FROM applicants WHERE email=? AND course_name=?", (email, course_name))
    checklist_str = c.fetchone()
    conn.close()

    # Update check_vars_committee with new checklist items
    if checklist_str is not None and checklist_str[0] is not None:
        selected_items = checklist_str[0].split("\n")
        for i, item in enumerate(checklist_items):
            var = IntVar(value=1 if item in selected_items else 0)
            check_vars_committee[i].set(var.get())  # Update existing variables with new values

    # Update progress bar again after updating the checklist
    update_progress(check_vars_committee)


# Buttons
approved_button = None
disapproved_button = None

def load_approval_buttons(email, usercourse):
    global approved_button
    global disapproved_button
    
    print("Loading approval buttons...")
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT status FROM applicants WHERE email=? AND course_name=?", (email, usercourse))
    status = c.fetchone()

    if status and status[0] == "Approved":
        print("Status: Approved")
        # If status is Approved, don't show the buttons
        if approved_button:
            approved_button.pack_forget()
            approved_button = None
        if disapproved_button:
            disapproved_button.pack_forget()
            disapproved_button = None
    else:
        print("Status: Not Approved")
        # Create approval buttons if not already created
        if not approved_button:
            approved_button = Button(committe_frame, text="Approved", font=("Arial", 12), command=approve_action)
            approved_button.pack(padx=20, pady=10, anchor="w")
        if not disapproved_button:
            disapproved_button = Button(committe_frame, text="Disapproved", font=("Arial", 12), command=disapprove_action)
            disapproved_button.pack(padx=20, pady=(10, 20), anchor="w")


# Configure scrollregion
committee_canvas.update_idletasks()
committee_canvas.config(scrollregion=committee_canvas.bbox("all"))



scrollbar_committee.config(command=committee_canvas.yview)

# Make scrollbar visible only when needed
committee_canvas.bind("<Configure>", lambda e: committee_canvas.configure(scrollregion=committee_canvas.bbox("all")))

# Adjusting scrollbar as per canvas size
committee_canvas.bind("<Configure>", lambda e: scrollbar_committee.pack_forget() if committee_canvas.winfo_height() >= committee_canvas.bbox("all")[3] else scrollbar_committee.pack(side=RIGHT, fill=Y))

# Function to update scroll region when the content changes
def update_scrollregion(event):
    committee_canvas.configure(scrollregion=committee_canvas.bbox("all"))

# Bind the update_scrollregion function to the frame's children and size changes
committe_frame.bind("<Configure>", update_scrollregion)
                

application_chart_committee.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))







# committee_course

def on_mousewheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


committee_course_home = tk.Toplevel()
committee_course_home.title("Course")
committee_course_home.geometry("800x600")
center_window(committee_course_home)
committee_course_home.withdraw()

frame_committee_course = Frame(committee_course_home)
frame_committee_course.pack(fill=BOTH, expand=True)


committee_course_nav_bar = Frame(frame_committee_course, bg="light blue", height=50)
committee_course_nav_bar.pack(fill="x")

committee_course_logo_image = PhotoImage(file=r"C:\Users\choug\Downloads\Project file Tkinter - Copy\Project file Tkinter - Copy\Project file Tkinter - Copy\img\logo.png")
committee_course_logo_image = committee_course_logo_image.subsample(4)
committee_course_logo_label = Label(committee_course_nav_bar, image=committee_course_logo_image)
committee_course_logo_label.pack(side="left", padx=10, pady=10)


# Add navigation buttons to the navbar frame
logout_button = Button(committee_course_nav_bar, text="Logout",  command=logout)
logout_button.pack(side=RIGHT, padx=5, pady=10)

courses_button = Button(committee_course_nav_bar, text="Courses", command=committee_course_window)
courses_button.pack(side=RIGHT, padx=5, pady=10)

application_button = Button(committee_course_nav_bar, text="Application", command=view_home_window_click)
application_button.pack(side=RIGHT, padx=5, pady=10)

# From

def on_enter_applicant(event):
    applicant_label.config(relief=FLAT)  # Remove border when mouse enters

def on_leave_applicant(event):
    applicant_label.config(relief=SOLID, borderwidth=1)  # Add border when mouse leaves
    
applicant_label = Label(frame_committee_course, text="Course", font=("Arial", 18),relief=SOLID, borderwidth=1)
applicant_label.pack(padx=1, pady=10)

# Bind events for hover effect
applicant_label.bind("<Enter>", on_enter_applicant)
applicant_label.bind("<Leave>", on_leave_applicant)


def add_committee_course():
    def save_course():
        # Get the values entered by the user
        course_name = course_name_entry.get()
        course_description = course_description_entry.get()

        # Insert the new course into the database
        admin_db.insert_course(course_name, course_description)

        for item in table_course.get_children():
            table_course.delete(item)
        
        admin_db.fetch_courses_admin_db(table_committee_course)
    
        
        committee_add_course_window.destroy()

    # Create a new window for adding a course
    committee_add_course_window = Toplevel()
    committee_add_course_window.title("Add Course")
    committee_add_course_window.geometry("400x200")
    center_window(committee_add_course_window)

    # Labels and entry fields for course name and description
    course_name_label = Label(committee_add_course_window, text="Course Name:", font=("Arial", 12))
    course_name_label.pack()
    course_name_entry = Entry(committee_add_course_window, font=("Arial", 12))
    course_name_entry.pack()

    course_description_label = Label(committee_add_course_window, text="Description:", font=("Arial", 12))
    course_description_label.pack()
    course_description_entry = Entry(committee_add_course_window, font=("Arial", 12))
    course_description_entry.pack()

    # Button to save the course
    save_button = Button(committee_add_course_window, text="Save", command=save_course)
    save_button.pack()


add_course_button = tk.Button(frame_committee_course, text="Add Course", command=add_committee_course, font=("Arial", 14))
add_course_button.pack(side="bottom", padx=10, pady=10, anchor="e")

# Define columns
columns_committee_course = ("Id", "Course name", "Description")

# Create the treeview with columns for unverified users
table_committee_course = ttk.Treeview(frame_committee_course, columns=columns_committee_course, show="headings")

# Define column headings for unverified users
for col in columns_committee_course:
    table_committee_course.heading(col, text=col)

# Configure the treeview to stretch columns and fill the whole width for unverified users
for col in columns_committee_course:
    table_committee_course.column(col, stretch=True)

# Define tag configuration for unverified users
table_committee_course.tag_configure("unverified", background="light gray")

# Define action for verifying user for unverified users
# table_course.bind("<Double-1>", on_click_applicant)

# Pack the table to fill both width and height of the window for unverified users
table_committee_course.pack(fill="both", expand=True)

# Fetch and display courses
admin_db.fetch_courses_admin_db(table_committee_course)

# Set padding for rows and columns
style = ttk.Style()
style.configure("Treeview", rowheight=50, padding=10)

# Set column width for ID column
table_committee_course.column("Id", width=50)  # Adjust the width as needed


table_committee_course.column("Description", width=300) 



committee_course_home.protocol("WM_DELETE_WINDOW", lambda: on_closing(login_window))

# committee_course end



login_window.mainloop()