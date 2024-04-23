from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import subprocess
from datetime import *


class customerClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1150x600+220+130")
        self.root.title("RETAIL PRO")
        self.root.config(bg="white")
        self.root.focus_force()

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="retailers",
            port=3306
        )

        self.cursor = self.db.cursor()

        # ====title====
        self.icon_title = PhotoImage(file="logo1.png")
        title = Label(self.root, text="RETAIL PRO", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # All Variables
        self.var_cust_id = StringVar()
        self.var_pname = StringVar()
        self.var_quantity = StringVar()
        self.var_gst = StringVar()
        self.var_amount = StringVar()
        self.var_sale = StringVar()


        # Title
        title = Label(self.root, text="CUSTOMER DETAILS", font=(
            "goudy old style", 15), bg="#0f4d7d", fg="white")
        title.place(x=30, y=100, width=1050)

        # Content
        # Row 1
        lbl_custide = Label(
            self.root, text="Product ID", font=("goudy old style", 15), bg="white")
        lbl_custide.place(x=50, y=150)
        lbl_pname = Label(
            self.root, text="Product Name", font=("goudy old style", 15), bg="white")
        lbl_pname.place(x=350, y=150)
        lbl_quantity = Label(
            self.root, text="Product quantity", font=("goudy old style", 15), bg="white")
        lbl_quantity.place(x=700, y=150)

        txt_custide = Entry(
            self.root, textvariable=self.var_cust_id, font=("goudy old style", 15), bg="lightyellow")
        txt_custide.place(x=150, y=150, width=180)
        txt_pname = Entry(
            self.root, textvariable=self.var_pname, font=("goudy old style", 15), bg="lightyellow")
        txt_pname.place(x=500, y=150, width=180)
        txt_quantity = Entry(
            self.root, textvariable=self.var_quantity, font=("goudy old style", 15), bg="lightyellow")
        txt_quantity.place(x=850, y=150, width=180)

        # Row 2
        lbl_gst = Label(
            self.root, text="GST", font=("goudy old style", 15), bg="white")
        lbl_gst.place(x=50, y=220)
        options = ["0", "5", "12", "18", "28"]  # GST rate
        txt_gst = ttk.Combobox(self.root, textvariable=self.var_gst, values=options, font=("goudy old style", 15),
                               background="lightyellow")
        txt_gst.place(x=150, y=220, width=180)
        lbl_amount = Label(
            self.root, text="Total Amount", font=("goudy old style", 15), bg="white")
        lbl_amount.place(x=350, y=220)
        lbl_sale = Label(
            self.root, text="Sale Price ", font=("goudy old style", 15), bg="white")
        lbl_sale.place(x=700, y=220)


        txt_amount = Entry(
            self.root, textvariable=self.var_amount, font=("goudy old style", 15), bg="lightyellow")
        txt_amount.place(x=500, y=220, width=180)
        txt_sale = Entry(
            self.root, textvariable=self.var_sale, font=("goudy old style", 15), bg="lightyellow")
        txt_sale.place(x=850, y=220, width=180)

        # Buttons
        btn_add = Button(self.root, text="SAVE", font=("goudy old style", 15), bg="#2196f3", fg="white",
                         cursor="hand2", command=self.save_data)
        btn_add.place(x=350, y=305, width=120, height=28)
        btn_clear = Button(self.root, text="CLEAR", font=("goudy old style", 15), bg="#607d8b", fg="white",
                           cursor="hand2", command=self.clear_data)
        btn_clear.place(x=700, y=305, width=120, height=28)
        btn_back = Button(self.root, text="BACK", font=("goudy old style", 10), bg="blue", fg="white",
                          command=self.dashboard, cursor="hand2")
        btn_back.place(x=1050, y=20, width=80, height=25)
        btn_check = Button(self.root, text="check", font=("goudy old style", 10), bg="blue", fg="white",
                           cursor="hand2", command=self.search_data)
        btn_check.place(x=585, y=185, width=80, height=25)
        btn_calculate = Button(self.root, text="CALCULATE", command=self.calculate_total, font=(
            "goudy old style", 15), bg="deep sky blue", fg="white", cursor="hand2")
        btn_calculate.place(x=520, y=305, width=120, height=28)

        # Customer Details
        cust_frame = Frame(self.root, bd=3, relief=RIDGE)
        cust_frame.place(x=0, y=350, relwidth=1, height=250)

        scrolly = Scrollbar(cust_frame, orient=VERTICAL)
        scrollX = Scrollbar(cust_frame, orient=HORIZONTAL)

        self.CustomerTable = ttk.Treeview(cust_frame, column=("Cid", "Pname", "quantity", "gst", "Amount", "Sale"), yscrollcommand=scrolly.set, xscrollcommand=scrollX.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)
        self.CustomerTable.heading("Cid", text="Product ID")
        self.CustomerTable.heading("Pname", text="Product Name")
        self.CustomerTable.heading("quantity", text="Product quantity")
        self.CustomerTable.heading("gst", text="GST")
        self.CustomerTable.heading("Amount", text="Total Amount")
        self.CustomerTable.heading("Sale", text="Sale Price")
        self.CustomerTable["show"] = "headings"

        self.update_treeview()

        self.CustomerTable.pack(fill=BOTH, expand=1)

    def clear_data(self):
        # Clearing text in entry widgets
        self.var_cust_id.set("")
        self.var_pname.set("")
        self.var_quantity.set("")
        self.var_gst.set("")
        self.var_amount.set("")
        self.var_sale.set("")

    def save_data(self) :
        try :
            # Fetching data from entry widgets
            product_id = self.var_cust_id.get()
            product_name = self.var_pname.get()
            quantity = int(self.var_quantity.get())  # Convert quantity to int
            gst = self.var_gst.get()
            total_amount = self.var_amount.get()
            sale_price = self.var_sale.get()
            update_query = "UPDATE inventory SET stock_quantity = stock_quantity - %s WHERE prod_id = %s"
            self.cursor.execute(update_query, (quantity, product_id))
            self.db.commit()

            # Check if stock quantity is below low_stk_alert

            check_query = "SELECT stock_quantity, low_stk_alert FROM inventory WHERE prod_id = %s"
            self.cursor.execute(check_query, (product_id,))
            stock_quantity, low_stk_alert = self.cursor.fetchone()
            # Update inventory table's stock quantity


            if stock_quantity < low_stk_alert:
                messagebox.showwarning("Low Stock Alert", "Stock quantity has gone below the limit!")
            elif stock_quantity==0:
                messagebox.showerror("Not In Stock" , "Product not present in stock! Please Refill!")
                self.clear_data()
            else:
                # Inserting data into the customer table
                query = "INSERT INTO customer (product_id, product_name, product_quantity, GST, total_amount, sale_price, sale_month) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (product_id , product_name , quantity , gst.strip('%') , total_amount , sale_price , datetime.now().month)
                self.cursor.execute(query , values)
                self.db.commit()



            # Check if stock quantity is below low_stk_alert


                messagebox.showinfo("Success" , "Data saved successfully!")
                self.clear_data()
                self.update_treeview()  # Update the Treeview after saving

        except mysql.connector as e:
            messagebox.showerror("Error" , f"Database error: {e}")
        except Exception as e :
            messagebox.showerror("Error" , f"Error: {str(e)}")

    def update_treeview(self):
        # Clear the existing data in the Treeview
        for item in self.CustomerTable.get_children():
            self.CustomerTable.delete(item)

        # Fetch all rows from the database
        query = "SELECT product_id, product_name, product_quantity, GST, total_amount, sale_price, sale_month FROM customer"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        # Insert all rows into the Treeview
        for row in data:
            self.CustomerTable.insert("", "end", values=row)

    def get_month_abbreviation(self, month_number):
        month_abbr = {
            1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
        }
        return month_abbr.get(month_number, '')

    def search_data(self):
        try:
            product_name = self.var_pname.get()

            # Fetching data from the database based on the entered product ID
            query = "SELECT prod_id, sale_per_unit, stock_quantity, GST, low_stk_alert FROM inventory WHERE prd_name = %s"
            self.cursor.execute(query, (product_name,))
            data = self.cursor.fetchone()


            if data:
                messagebox.showinfo(
                    "Found", f"Data found for Product name: {product_name}")
                # Data found for the product ID
                product_id, sale_price, stock_quantity,GST, low_stk_alert= data

                if stock_quantity == 0 :
                    messagebox.showerror("Not In Stock" , "Product not present in stock! Please Refill!")
                    self.clear_data()
                elif stock_quantity < low_stk_alert :
                    messagebox.showwarning("Low Stock Alert" , f"Stock quantity has gone below the limit for Product {product_name}")
                    # Update the corresponding text fields with the retrieved data
                    self.var_cust_id.set(product_id)
                    self.var_sale.set(sale_price)
                    self.var_gst.set(str(GST) + '%')
                else:
                    # Update the corresponding text fields with the retrieved data
                    self.var_cust_id.set(product_id)
                    self.var_sale.set(sale_price)
                    self.var_gst.set(str(GST)+'%')
                return True

            else:
                # No data found for the product ID
                messagebox.showinfo("Not Found", f"No data found for Product name: {product_name}")
                return False

        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def calculate_total(self) :
        # Check if product quantity is not empty
        product_quantity = self.var_quantity.get()
        if product_quantity != "" :
            # Get the sale price from the entry widget
            sale_price = float(self.var_sale.get())
            # Assume GST rate is stored in the GST column of the inventory table
            query = "SELECT GST FROM inventory WHERE prod_id = %s"
            self.cursor.execute(query , (self.var_cust_id.get() ,))
            gst_rate = self.cursor.fetchone()[0]

            # Calculate the total price
            total_price = sale_price * int(product_quantity) * (1 + gst_rate / 100)
            # Update the total amount entry field with the calculated value
            self.var_amount.set(round(total_price , 2))
        else :
            messagebox.showerror("Error" , "Product quantity cannot be empty!")

    def dashboard(self):
        self.root.destroy()
        subprocess.run(['python', 'dashboard.py'])


root = Tk()
obj = customerClass(root)
root.mainloop()