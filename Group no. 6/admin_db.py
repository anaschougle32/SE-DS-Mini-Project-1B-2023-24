import sqlite3
import os
import textwrap

def verify_user(email):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("UPDATE users SET user_verified = ? WHERE email = ?", (True, email))
    conn.commit()  # Commit the changes to the database
    print(f"User with email {email} verified")
    conn.close()  # Close database connection

def reload_data(table):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    # Clear the current table
    table.delete(*table.get_children())

    # Fetch data from users table excluding admin emails
    c.execute("SELECT email, name, role FROM users WHERE user_verified = 0 AND role != 'admin'")  
    rows = c.fetchall()

    # Insert data into the table
    for row in rows:
        email, name, role = row
        table.insert("", "end", values=(email, name, role, "Verify"), tags=("unverified",)) 
    conn.close()  # Close database connection



def unverify_user(email):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("UPDATE users SET user_verified = ? WHERE email = ?", (False, email))
    conn.commit()  # Commit the changes to the database
    print(f"User with email {email} unverified")
    conn.close()  # Close database connection


def Re_unverified_user(table):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    # Clear the current table
    table.delete(*table.get_children())

    # Fetch data from users table excluding admin emails
    c.execute("SELECT email, name, role FROM users WHERE user_verified = 1 AND role != 'admin'")  
    rows = c.fetchall()

    # Insert data into the table
    for row in rows:
        email, name, role = row
        table.insert("", "end", values=(email, name, role, "unverified"), tags=("unverified",)) 
    conn.close()
    

def applicant_data(table):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    # Clear the current table
    table.delete(*table.get_children())

    # Fetch data from applicants table
    c.execute("SELECT email, course_name, status FROM applicants")
    rows = c.fetchall()

    # Insert data into the table
    for row in rows:
        email, course_name, status = row
        table.insert("", "end", values=(email, course_name, status, "View"))
    
    conn.close()

    

def verify_cv(email):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()

    # Fetch CV path from applicants table based on email
    c.execute("SELECT cv_path FROM applicants WHERE email = ?", (email,))
    result = c.fetchone()
    
    conn.close()

    if result:
        cv_path = result[0]
        if os.path.exists(cv_path):
            return cv_path
        else:
            print("CV file not found.")
            return None
    else:
        print("No applicant found with the provided email.")
        return None


def applicant_file(table):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    # Clear the current table
    table.delete(*table.get_children())

    # Fetch email from users table where login_status is true
    c.execute("SELECT email FROM users WHERE login_status = 1")
    result = c.fetchone()

    if result:
        email = result[0]
        # Fetch data from applicants table based on email
        c.execute("SELECT Email, Course_Name, Status, cv_path FROM applicants WHERE Email = ?", (email,))
        rows = c.fetchall()

        # Insert data into the table
        for row in rows:
            email, course_name, Status, cv_path = row
            table.insert("", "end", values=(email, course_name,Status, "CV"))
    else:
        print("No user found with login status true.")

    conn.close()

# database_operations.py

def update_status(c, conn, committe_frame, approved_button, disapproved_button, applicant_id, status):
    # Update the status in the database
    c.execute('''UPDATE applicants SET status = ? WHERE email = ?''', (status, email))
    conn.commit()

    # Remove the approval buttons
    approved_button.pack_forget()
    disapproved_button.pack_forget()

    # Add an "Approved" label/button
    approved_label = Label(committe_frame, text="Status: Approved", font=("Arial", 12))
    approved_label.pack(padx=20, pady=10, anchor="w")
    approved_label.bind("<Button-1>", lambda event: approved_label.focus_set())  # Make the label unresponsive

    conn.close()
    

def fetch_courses_admin_db(table):
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()

    c.execute("SELECT id, course_name, description FROM courses")
    courses = c.fetchall()
    
    # Insert data into the table
    for row in courses:
        id, course_name, description = row
        # Wrap the description text
        wrapped_description = "\n".join(textwrap.wrap(description, width=60))  # Adjust the width as needed
        table.insert("", "end", values=(id, course_name, wrapped_description))
    
    conn.close()

    
def insert_course(course_name, course_description):
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()

    # Insert the new course into the database
    c.execute("INSERT INTO courses (course_name, description) VALUES (?, ?)", (course_name, course_description))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    
def fetch_courses_applicant_db():
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()

    c.execute("SELECT id, course_name, description FROM courses")
    courses = c.fetchall()
    
    conn.close()
    
    return courses