import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
# import matplotlib.pyplot as plt
import subprocess
import mysql.connector

class ModernTk(tk.Tk):
    def __init__(self):
        super().__init__()
        

    def run(self):
        self.mainloop()

class AdminDashboard():
    def __init__(self, master,username):
        self.master = master
        self.master.title("Admin Dashboard")
        self.master.geometry('950x600')
        self.master.config(bg="#121212") 


        self.create_widgets(username)
        self.username = username

    def run(self):
        self.master.mainloop()

    def create_widgets(self,username):
        # Admin Dashboard Label
        self.options_frame = tk.Frame(self.master, bg='#232323', width=200, height=600)  # Adjusted size
        self.options_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.main_frame = tk.Frame(self.master, highlightbackground='black', highlightthickness=1, width=620, height=550, bg="#121212")  # Darker background
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add user logo
        user_logo = Image.open("profile.png")  # Provide the path to your user logo image
        user_logo = user_logo.resize((100, 100))  # Resize the logo
        user_logo = ImageTk.PhotoImage(user_logo)
        logo_label = tk.Label(self.options_frame, image=user_logo, bg="#232323")
        logo_label.image = user_logo
        logo_label.pack()

        # Add username text
        username_label = tk.Label(self.options_frame, text=username, font=('Arial', 14), fg='white', bg='#232323')
        username_label.pack(pady=(20, 5))

        # Add buttons with icons
        self.pages = {
            " Home": {"icon": "home_icon.png", "command":self.home_page},
            " Profile": {"icon": "profile_icon.png", "command": lambda:self.profile_page(username)},
            " Orders": {"icon": "order_icon.png", "command": self.order_page},
            " User": {"icon": "ad_icon.png", "command": self.user_page},
            " Rentee": { "icon": "cart_icon.png", "command" :self.rentee_page},
            " Payment Detail": { "icon": "hand.png", "command" :self.user_stat_page},
            
        }
        self.current_page = None
        self.buttons = {}
        for text, info in self.pages.items():
            icon = Image.open(info["icon"])
            icon = icon.resize((30, 30))  # Resize the icon
            icon = ImageTk.PhotoImage(icon)
            command=info["command"]
            button = tk.Button(self.options_frame, text=text, image=icon, compound=tk.LEFT,
                   font=('Arial', 14), fg='white', bg='#800080',  # Adjusted font size and button color
                   width=180,cursor="hand2" ,command=lambda cmd=command: self.change_page(cmd)) 
            button.image = icon
            button.pack(side=tk.TOP, fill=tk.X, pady=5)  # Adjust position for buttons
            self.buttons[text] = button

        

        # Add logout button at the bottom with an icon
        logout_icon = Image.open("logout_icon.png")  # Provide the path to your logout icon image
        logout_icon = logout_icon.resize((30, 30))  # Resize the icon
        logout_icon = ImageTk.PhotoImage(logout_icon)
        logout_button = tk.Button(self.options_frame, text="Logout", image=logout_icon, compound=tk.LEFT,
                                  font=('Arial', 14), fg='white', bg='#800080',cursor="hand2" ,width=180, command=self.logout)  # Adjusted font size and button width
        logout_button.image = logout_icon
        logout_button.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        self.change_page(self.home_page)  # Select home page by default
    
    
    def logout(self):
        # Prompt user for confirmation
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            # Destroy the current window
            self.master.destroy()
            # Start the start.py file using subprocess
            subprocess.run(["python", "start.py"])
        
        

    
    def change_page(self, page):
        # Delete existing pages
        self.delete_pages()

    # Check if the page is the profile page
        if page == self.profile_page:
            self.display_profile_data(self.username)

        

    # Create a new frame for the selected page
        if callable(page):
            page()

    # Set the current page attribute to the selected page
        self.current_page = page

    def return_to_home(self, frame):
        # Destroy the current page frame
        frame.destroy()
        # Navigate back to the home page
        self.home_page()



    def home_page(self):
        # Placeholder for home page content
        home_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        home_frame.pack(fill=tk.BOTH, expand=True)

        canvas_height = 70
        canvas = tk.Canvas(home_frame, bg="#800080", highlightthickness=0, height=canvas_height)
        canvas.pack(fill=tk.X)

        canvas.create_rectangle(0, 0, self.master.winfo_screenwidth(), canvas_height, fill="#800080")  # Adjust width as per screen width

        # Add text 'Home' on the left side of the canvas
        canvas.create_text(15, canvas_height // 2, anchor=tk.W, text="Admin Dashboard :", fill="white", font=('Arial', 18, 'bold'))

        # Create three small rectangle frames
        frame1 = tk.Frame(home_frame, bg="#8444FC", width=200, height=50)
        frame1.place(x=50, y=100)
        frame2 = tk.Frame(home_frame, bg="#E23E57", width=200, height=50)
        frame2.place(x=400, y=100)
        frame3 = tk.Frame(home_frame, bg="#05299E", width=200, height=50)
        frame3.place(x=50, y=230)

        # Count number of users
        user_count = self.get_user_count()

        # Count number of ads
        ad_count = self.get_ad_count()

        # Count number of orders placed
        order_count = self.get_order_count()

        # Display counts in the frames
        label1 = tk.Label(frame1, text=f"No of Users: {user_count}", fg="white", bg="#8444FC", font=('Arial', 18))
        label1.pack(padx=50,pady=35)
        label2 = tk.Label(frame2, text=f"No of Ads: {ad_count}", fg="white", bg="#E23E57", font=('Arial', 18))
        label2.pack(padx=50,pady=35)
        label3 = tk.Label(frame3, text=f"No of Orders Placed: \n{order_count}", fg="white", bg="#05299E", font=('Arial', 18))
        label3.pack(padx=10,pady=20)


        # Create a Treeview widget to display user details, number of ads rented, and number of ads published
        tree = ttk.Treeview(home_frame)
        tree["columns"] = ( "Ads Rented", "Ads Published")

        # Define column headings
        tree.heading("#0", text="Username")
        
        tree.heading("Ads Rented", text="Product Uploaded")
        tree.heading("Ads Published", text="Product Rented")

        

        # Fetch user details, number of ads rented, and number of ads published from the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Fetch user details, number of ads rented, and number of ads published
            query = """
                        SELECT sl.username, 
                        COUNT(DISTINCT ad.ad_id) AS ad_count,
                        COUNT(DISTINCT ord.order_id) AS order_count
                    FROM student_login sl
                    LEFT JOIN ad_table ad ON sl.username = ad.username
                    LEFT JOIN order_table ord ON sl.username = ord.username
                    GROUP BY sl.username
                    """
            cursor.execute(query)
            user_data = cursor.fetchall()

            # Populate the Treeview with user details
            for user in user_data:
                tree.insert("", "end", text=user[0], values=( user[1], user[2]))

            # Commit and close
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        # Pack the Treeview
        tree.place(x=50,y=340)


    def get_user_count(self):
        try:
            # Establish a connection to the database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            
            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Define your SQL query to count users
            sql_query = "SELECT COUNT(*) FROM student_login"

            # Execute the SQL query
            cursor.execute(sql_query)

            # Fetch the result of the query
            user_count = cursor.fetchone()[0]

            # Close the cursor and connection
            cursor.close()
            conn.close()

            return user_count

        except mysql.connector.Error as err:
            # Handle any errors
            print("Error:", err)
            return None

    def get_ad_count(self):
        try:
            # Establish a connection to the database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            
            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Define your SQL query to count users
            sql_query = "SELECT COUNT(*) FROM ad_table"

            # Execute the SQL query
            cursor.execute(sql_query)

            # Fetch the result of the query
            user_count = cursor.fetchone()[0]

            # Close the cursor and connection
            cursor.close()
            conn.close()

            return user_count

        except mysql.connector.Error as err:
            # Handle any errors
            print("Error:", err)
            return None

    def get_order_count(self):
        try:
            # Establish a connection to the database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            
            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Define your SQL query to count users
            sql_query = "SELECT COUNT(*) FROM order_table"

            # Execute the SQL query
            cursor.execute(sql_query)

            # Fetch the result of the query
            user_count = cursor.fetchone()[0]

            # Close the cursor and connection
            cursor.close()
            conn.close()

            return user_count

        except mysql.connector.Error as err:
            # Handle any errors
            print("Error:", err)
            return None

    def profile_page(self,username):
        # Delete existing pages
        self.delete_pages()

        # Create a new frame for the profile page
        profile_frame = tk.Frame(self.main_frame, bg="#121212")
        profile_frame.pack(fill=tk.BOTH, expand=True)

        # Add label "Your Profile"
        profile_label = tk.Label(profile_frame, text="Your Profile:", font=('Helvetica', 24), fg="white", bg="#121212")
        profile_label.place(x=20, y=20)

        # Create a canvas for the circular image box
        self.canvas = tk.Canvas(profile_frame, bg="#212121", width=100, height=100, highlightthickness=0)
        self.canvas.place(x=20, y=60)
        
        
        # profile_label1 = tk.Label(profile_frame, bg="blue",width=20,height=5)
        # profile_label1.place(x=20, y=400)
        #Draw a circular box on the canvas
        self.image = Image.open("profile.png").resize((100, 100), Image.LANCZOS)  # Create a blank image
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(50, 50, image=self.photo_image)

        # # Add upload button
        # upload_button = tk.Button(profile_frame, text="Upload", font=('Arial', 12), bg="#800080", fg="white", width=10, height=1, command=self.upload_prof_image)
        # upload_button.place(x=200, y=90)

        # Add username label and entry
        username_label = tk.Label(profile_frame, text="Username:", font=('Arial', 14), fg="white", bg="#121212")
        username_label.place(x=20, y=180)
        self.username_entry = tk.Entry(profile_frame, font=('Arial', 12), bg="#212121", fg="white")
        self.username_entry.place(x=20, y=210)

        # Add password label and entry
        password_label = tk.Label(profile_frame, text="Password:", font=('Arial', 14), fg="white", bg="#121212")
        password_label.place(x=400, y=180)
        self.password_entry = tk.Entry(profile_frame, show="*", font=('Arial', 12), bg="#212121", fg="white")
        self.password_entry.place(x=400, y=210)

        phone_label = tk.Label(profile_frame, text="Phone No.:", font=('Arial', 14), fg="white", bg="#121212")
        phone_label.place(x=20, y=260)
        self.phone_entry = tk.Entry(profile_frame, font=('Arial', 12), bg="#212121", fg="white")
        self.phone_entry.place(x=20, y=290)

        # Add email label and entry
        email_label = tk.Label(profile_frame, text="Email:", font=('Arial', 14), fg="white", bg="#121212")
        email_label.place(x=400, y=260)
        self.email_entry = tk.Entry(profile_frame, font=('Arial', 12), bg="#212121", fg="white")
        self.email_entry.place(x=400, y=290)

        update_button = tk.Button(profile_frame, text="Update", font=('Arial', 12), bg="#800080", fg="white",width=20,height=1,command=self.update_profile)
        update_button.place(x=200, y=480)

        self.display_profile_data(username)
    


    def display_profile_data(self,username):
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )

            # Create a cursor
            cursor = conn.cursor()

            # Prepare the SQL query to fetch profile data
            sql = "SELECT * FROM admin_login WHERE admin_name = %s"
            cursor.execute(sql, (username,))

            # Fetch the data
            profile_data = cursor.fetchone()

            # Check if data is retrieved
            if profile_data:
                # Populate the text boxes/fields with the retrieved data
                self.username_entry.delete(0, tk.END)
                self.username_entry.insert(0, profile_data[1])  # Assuming username is the first column

                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, profile_data[2])  # Assuming password is the second column

                self.phone_entry.delete(0, tk.END)
                self.phone_entry.insert(0, profile_data[3])  # Assuming phone_no is the third column

                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, profile_data[4])  # Assuming email_id is the fourth column


            # Close the cursor and connection
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            # Handle any errors that occur during the database operation
            print("Error:", err)

        

    def update_profile(self):
        # Get the updated profile data from the entry fields and comboboxes
        updated_username = self.username_entry.get()
        updated_password = self.password_entry.get()
        updated_phone = self.phone_entry.get()
        updated_email = self.email_entry.get()
        
       

        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )

            # Create a cursor
            cursor = conn.cursor()

            # Prepare the SQL query to update the profile data
            sql = "UPDATE admin_login SET password = %s, phone_no = %s, email_id = %s WHERE admin_name = %s"
            cursor.execute(sql, (updated_password, updated_phone, updated_email , updated_username))

            # Commit the changes
            conn.commit()

            # Display a success message
            messagebox.showinfo("Success", "Profile updated successfully")

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            # Handle any errors that occur during the database operation
            messagebox.showerror("Error", f"Failed to update profile: {err}")

        

    def order_page(self):
        order_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        lb = tk.Label(order_frame, text='Order Details', font=('Bold', 30), fg="white", bg="#121212")  # Darker text and background
        lb.pack()

        

        # Create a Treeview widget to display orders
        tree = ttk.Treeview(order_frame)
        tree["columns"] = ("Title", "Description", "Publisher Name", "Price", "Start Date", "End Date", "Remaining Days")

        # Define column headings
        tree.heading("#0", text="Order ID")
        # tree.heading("#1","Order ID", text="Order ID")
        tree.heading("Title", text="Title")
        tree.heading("Description", text="Description")
        tree.heading("Publisher Name", text="Buyer Name")
        tree.heading("Price", text="Price")
        tree.heading("Start Date", text="Start Date")
        tree.heading("End Date", text="End Date")
        tree.heading("Remaining Days", text="No of Days")

        tree.column("#0", width=200)  # Adjust the width of the first column (Order ID)
        tree.column("#1", width=150)  # Adjust the width of the "Title" column
        tree.column("#2", width=200)  # Adjust the width of the "Description" column
        tree.column("#3", width=100)  # Adjust the width of the "Publisher Name" column
        tree.column("#4", width=100)  # Adjust the width of the "Price" column
        tree.column("#5", width=100)  # Adjust the width of the "Start Date" column
        tree.column("#6", width=100)  # Adjust the width of the "End Date" column
        tree.column("#7", width=100)

        # Add a horizontal scrollbar
        scrollbar_x = tk.Scrollbar(order_frame, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the Treeview to use the horizontal scrollbar
        tree.configure(xscrollcommand=scrollbar_x.set)

        # Fetch orders from the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Fetch orders made by the logged-in user
            query = """SELECT order_id, title, description, username, price, start_date, end_date, num_of_days 
                       FROM order_table 
                       """
            cursor.execute(query)
            orders = cursor.fetchall()


            # Check if there are no orders
            if not orders:
                # If there are no orders, display an empty table
                tree.insert("", "end", text="No data available")
            else:
                # Populate the Treeview with orders
                for order in orders:
                    tree.insert("", "end", text=order[0], values=(order[1], order[2], order[3], order[4], order[5], order[6], order[7]))

            # Commit and close
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
        # Pack the Treeview
        tree.pack(expand=True, fill=tk.BOTH)


        order_frame.pack(pady=20)
        

    def user_page(self):
        user_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        lb = tk.Label(user_frame, text='User Details', font=('Bold', 30), fg="white", bg="#121212")  # Darker text and background
        lb.pack()

        # Create a Treeview widget to display user data
        user_tree = ttk.Treeview(user_frame)
        user_tree["columns"] = ("Password", "Phone No", "Email ID", "Branch", "Year")

        # Define column headings
        user_tree.heading("#0", text="Username")
        user_tree.heading("Password", text="Password")
        user_tree.heading("Phone No", text="Phone No")
        user_tree.heading("Email ID", text="Email ID")
        user_tree.heading("Branch", text="Branch")
        user_tree.heading("Year", text="Year")

        # Define column widths
        user_tree.column("#0", width=150)  # Adjust the width of the first column (User ID)
        user_tree.column("#1", width=150)  # Adjust the width of the "Username" column
        user_tree.column("#2", width=150)  # Adjust the width of the "Password" column
        user_tree.column("#3", width=150)  # Adjust the width of the "Phone No" column
        user_tree.column("#4", width=150)  # Adjust the width of the "Email ID" column
        user_tree.column("#5", width=150)  # Adjust the width of the "Branch" column
          # Adjust the width of the "Year" column

        # Add a horizontal scrollbar
        scrollbar_x = tk.Scrollbar(user_frame, orient=tk.HORIZONTAL, command=user_tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the Treeview to use the horizontal scrollbar
        user_tree.configure(xscrollcommand=scrollbar_x.set)

        # Fetch user data from the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Fetch user data
            query = """SELECT username, password, phone_no, email_id, branch, year FROM student_login"""
            cursor.execute(query)
            users = cursor.fetchall()

            # Check if there are no users
            if not users:
                # If there are no users, display an empty table
                user_tree.insert("", "end", text="No data available")
            else:
                # Populate the Treeview with user data
                for user in users:
                    user_tree.insert("", "end", text=user[0], values=(user[1], user[2], user[3], user[4], user[5]))

            # Commit and close
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        # Pack the Treeview
        user_tree.pack(expand=True, fill=tk.BOTH)

        user_frame.pack(pady=20)


    def rentee_page(self):
        ad_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        lb = tk.Label(ad_frame, text='Ad Details', font=('Bold', 30), fg="white", bg="#121212")  # Darker text and background
        lb.pack()

        # Create a Treeview widget to display ad data
        ad_tree = ttk.Treeview(ad_frame)
        ad_tree["columns"] = ("Username", "Title", "Description", "Category", "Price")

        # Define column headings
        ad_tree.heading("#0", text="Ad ID")
        ad_tree.heading("Username", text="Rentee name")
        ad_tree.heading("Title", text="Title")
        ad_tree.heading("Description", text="Description")
        ad_tree.heading("Category", text="Category")
        ad_tree.heading("Price", text="Price")

        # Define column widths
        ad_tree.column("#0", width=100)  # Adjust the width of the "Ad ID" column
        ad_tree.column("#1", width=100)  # Adjust the width of the "Username" column
        ad_tree.column("#2", width=150)  # Adjust the width of the "Title" column
        ad_tree.column("#3", width=200)  # Adjust the width of the "Description" column
        ad_tree.column("#4", width=100)  # Adjust the width of the "Category" column
        ad_tree.column("#5", width=100)  # Adjust the width of the "Price" column

        # Add a horizontal scrollbar
        scrollbar_x = tk.Scrollbar(ad_frame, orient=tk.HORIZONTAL, command=ad_tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the Treeview to use the horizontal scrollbar
        ad_tree.configure(xscrollcommand=scrollbar_x.set)

        # Fetch ad data from the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Fetch ad data
            query = """SELECT ad_id, username, title, description, category, price FROM ad_table"""
            cursor.execute(query)
            ads = cursor.fetchall()

            # Check if there are no ads
            if not ads:
                # If there are no ads, display an empty table
                ad_tree.insert("", "end", text="No data available")
            else:
                # Populate the Treeview with ad data
                for ad in ads:
                    ad_tree.insert("", "end", text=ad[0], values=(ad[1], ad[2], ad[3], ad[4], ad[5]))

            # Commit and close
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


        # # Create a label below the Treeview
        # info_label = tk.Label(ad_frame, text="Additional information goes here",font=('Arial',20), fg="white", bg="#121212")
        # info_label.pack()
        # Pack the Treeview
        ad_tree.pack(expand=True, fill=tk.BOTH)

        ad_frame.pack(pady=20)

    def user_stat_page(self):
        global total_amount
        home_frame = tk.Frame(self.main_frame, bg="#121212")  # Darker background
        home_frame.pack(fill=tk.BOTH, expand=True)

        header_label = tk.Label(home_frame, text="User Statistics", font=('Bold', 30), fg="white", bg="#121212")
        header_label.pack(pady=20)

        frame1 = tk.Frame(home_frame, bg="#8444FC", width=200, height=50)
        frame1.place(x=50, y=100)

        # label1 = tk.Label(frame1, text=f"Total Amount: {total_amount} ", fg="white", bg="#8444FC", font=('Arial', 18))
        # label1.pack(padx=50,pady=35)

        # Create a Treeview widget to display user details, number of ads rented, and number of ads published
        tree = ttk.Treeview(home_frame)
        tree["columns"] = ( "Ads Rented", "Total Amount")

        # Define column headings
        tree.heading("#0", text="Username")
        
        tree.heading("Ads Rented", text="Product Rented")
        tree.heading("Total Amount", text="Amount Paid")

        

        # Fetch user details, number of ads rented, and number of ads published from the database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Annsh@10",
                database="student"
            )
            cursor = conn.cursor()

            # Fetch user details, number of ads rented, and number of ads published
            query = """
                        SELECT sl.username, COUNT(DISTINCT ord.order_id) AS ads_purchased, SUM(ord.price) AS total_amount
                FROM student_login sl
                
                LEFT JOIN order_table ord ON sl.username = ord.username
                GROUP BY sl.username
                    """
            cursor.execute(query)
            user_data = cursor.fetchall()

            # Calculate total amount
            total_amount = sum(user[2] for user in user_data)


            label1 = tk.Label(frame1, text=f"Total Amount: ₹{total_amount} ", fg="white", bg="#8444FC", font=('Arial', 18))
            label1.pack(padx=50,pady=35)

            # Populate the Treeview with user details
            for user in user_data:
                tree.insert("", "end", text=user[0], values=( user[1], user[2]))

            # Commit and close
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        # Pack the Treeview
        tree.place(x=50,y=250)

        
    

    def delete_pages(self):
        for child in self.main_frame.winfo_children():
            child.destroy()


# Create the main application window
if __name__ == "__main__":
    root = ModernTk()
    app = AdminDashboard(root,'username')
    root.run()