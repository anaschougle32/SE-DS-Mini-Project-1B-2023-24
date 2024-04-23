from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import subprocess

class InventoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1150x600+220+130")
        self.root.title("RETAIL PRO")
        self.root.config(bg="white")
        self.root.focus_force()

        # ====db connection=====
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="retailers",
            port=3306
        )
        self.cursor = self.db.cursor()

        # ====All Variables====
        self.var_prd_id = StringVar()
        self.var_prd_name = StringVar()
        self.var_stk_quantity = StringVar()

        # ====title====
        self.icon_title = PhotoImage(file="logo1.png")
        title = Label(self.root, text="RETAIL PRO", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        btn_back = Button(self.root, text="BACK", font=("goudy old style", 10), bg="blue", fg="white", command=self.dashboard, cursor="hand2").place(x=1050, y=20, width=80, height=25)

        # ====inventory====
        inventory_label = Label(self.root, text="INVENTORY DETAILS", font=("times new roman", 15), bg="#0f4d7d", fg="white").place(x=50, y=100, width=1000)

        # InventoryStatus label=====
        status_frame = LabelFrame(self.root, bg="peach puff", relief="ridge")
        status_frame.place(x=0, y=160, width=1150, relheight=0.1)
        empty_label = Label(status_frame, bg="peach puff")
        empty_label.grid_configure(sticky="news", padx=230)
        inventorystatus_label = Label(status_frame, text="Inventory Status : ", font=("Time New Roman", 13), bg="lemon chiffon")
        inventorystatus_label.grid_configure(column=1, row=1, sticky="news")
        invtstatus_label = Label(status_frame, text=f"{self.statusquery()}", font=("Time New Roman", 13), bg="lemon chiffon")
        invtstatus_label.grid_configure(row=1, column=2, sticky="news", padx=5)

        # showing products in inventory
        inventory_frame = Frame(self.root, bd=3, relief=RIDGE)
        inventory_frame.place(x=0, y=250, relwidth=1, height=400)

        scrolly = Scrollbar(inventory_frame, orient=VERTICAL)
        scrollX = Scrollbar(inventory_frame, orient=HORIZONTAL)

        self.InventoryTable = ttk.Treeview(inventory_frame, columns=("prd_id", "prd_name", "stk_quantity","low_stk_alert"))
        scrollX.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.InventoryTable.xview)
        scrolly.config(command=self.InventoryTable.yview)

        self.InventoryTable.heading("prd_id", text="Product Id")
        self.InventoryTable.heading("prd_name", text="Product Name")
        self.InventoryTable.heading("stk_quantity", text="Stock Quantity")
        self.InventoryTable.heading("low_stk_alert", text="Low Stock ")

        self.InventoryTable["show"] = "headings"
        self.InventoryTable.pack(fill="both", expand=1)

        self.showdata()

        # Bind double-click event to show details
        self.InventoryTable.bind("<Double-1>", self.prd_status)

    def showdata(self):
        # fetch data from db
        query = "SELECT `prod_id`, `prd_name`,`stock_quantity`, `low_stk_alert` FROM inventory"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        # Insert into treeview
        for row in data:
            self.InventoryTable.insert(parent="", index="end", values=row)

    def statusquery(self):
        self.cursor.execute("SELECT count(prod_id) FROM inventory")
        result = self.cursor.fetchone()
        count = result[0] if result else "0"
        return count

    def dashboard(self):
        self.root.destroy()
        subprocess.run(['python', 'dashboard.py'])

    def prd_status(self, event):
        item = self.InventoryTable.focus()
        if item:
            values = self.InventoryTable.item(item, "values")
            product_id = values[0]  # Assuming product ID is the first column in the table
            prd_status_window = Toplevel(self.root)
            obj = PrdStatusClass(prd_status_window, product_id)
    # Passing the product ID as a string to the PrdStatusClass constructor

class PrdStatusClass:
    def __init__(self, root, product_id):
        self.root = root
        self.root.geometry("1150x600+220+130")
        self.root.title("RETAIL PRO")
        self.root.config(bg="#ADD8E6")
        self.root.focus_force()

        # ====db connection=====
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="retailers",
            port=3306
        )
        self.cursor = self.db.cursor()

        # ====variable====
        self.icon_title = PhotoImage(file="logo1.png")
        title = Label(self.root, text="RETAIL PRO", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        self.var_prd_id = StringVar()
        self.var_prd_name = StringVar()
        self.var_sale_price = StringVar()
        self.var_pur_price = StringVar()
        self.var_stk_price = StringVar()
        self.var_stk_quantity = StringVar()
        self.var_low_stk_alert = StringVar()
        self.var_gst = StringVar()

        self.var_prd_id.set(product_id)

        # ====title====
        title = Label(self.root, text="PRODUCT STATUS", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(x=50, y=100, width=1000)

        # ====labels&entry====
        lbl_productid = Label(self.root, text="Product ID", font=("goudy old style", 15), bg="#ADD8E6").place(x=50, y=150)
        val_productid = Label(self.root, textvariable = self.var_prd_id, font=("goudy old style", 15), bg="lightyellow").place(x=190, y=150, width=200)

        lbl_pname = Label(self.root, text="Product Name", font=("goudy old style", 15), bg="#ADD8E6").place(x=50, y=220)
        val_pname = Label(self.root, textvariable = self.var_prd_name, font=("goudy old style", 15), bg="lightyellow").place_configure(x=190, y=220, width=200,relwidth = 0.1)


        lbl_price = Label(self.root, text="Sales Price", font=("goudy old style", 15), bg="#ADD8E6").place(x=50, y=290)
        val_price = Label(self.root, textvariable = self.var_sale_price, font=("goudy old style", 15), bg="lightyellow").place(x=190, y=290, width=200)

        lbl_pprice = Label(self.root, text="Purchase Price", font=("goudy old style", 15), bg="#ADD8E6").place(x=50, y=370)
        val_pprice = Label(self.root, textvariable = self.var_pur_price, font=("goudy old style", 15), bg="lightyellow").place(x=190, y=370, width=200)

        lbl_stkvalue = Label(self.root, text="Stock value", font=("goudy old style", 15), bg="#ADD8E6").place(x=600, y=150)
        val_stkvalue = Label(self.root, textvariable = self.var_stk_price, font=("goudy old style", 15), bg="lightyellow").place(x=750, y=150, width=200)

        lbl_qnty = Label(self.root, text="Stock Quantity", font=("goudy old style", 15), bg="#ADD8E6").place(x=600, y=220)
        val_qnty = Label(self.root, textvariable = self.var_stk_quantity, font=("goudy old style", 15), bg="lightyellow").place(x=750, y=220, width=200)

        lbl_alert = Label(self.root, text="Low Stock Alert", font=("goudy old style", 15), bg="#ADD8E6").place(x=600, y=290)
        val_alert = Label(self.root, textvariable = self.var_low_stk_alert, font=("goudy old style", 15), bg="lightyellow").place(x=750, y=290, width=100)

        # ====buttons====
        btn_back = Button(self.root, text="BACK", font=("goudy old style", 10), bg="blue", fg="white", command=self.inventory, cursor="hand2").place(x=1050, y=20, width=80, height=25)

        self.show_data(product_id)  # To show data of a particular product based on its id

    def show_data(self, product_id):
        query = f"SELECT `prod_id`, `prd_name`, `purchase_per_unit`, `sale_per_unit`, `stock_quantity`, `stock_price`, `GST`, `low_stk_alert` FROM `inventory` WHERE prod_id='{product_id}'"
        self.cursor.execute(query)
        data = self.cursor.fetchone()

        if data:
            self.var_prd_name.set(data[1])
            self.var_pur_price.set(data[2])
            self.var_sale_price.set(data[3])
            self.var_stk_quantity.set(data[4])
            self.var_stk_price.set(data[5])
            self.var_gst.set(data[6])
            self.var_low_stk_alert.set(data[7])


    def inventory(self):
        self.root.destroy()

root = Tk()
obj = InventoryClass(root)
root.mainloop()
