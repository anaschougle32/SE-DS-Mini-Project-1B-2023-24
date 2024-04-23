import subprocess
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from datetime import *

class SalesClass(Tk):
    def __init__(self):
        super().__init__()
        self.list_y_purchase = None
        self.list_x_purchase = None
        self.list_y_sales = None
        self.list_x_sales = None
        self.geometry("1150x600+220+130")
        self.title("RETAIL PRO")
        self.config(bg="white")
        self.focus_force()

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="retailers",
            port=3306
        )
        self.cursor = self.db.cursor()

        self.icon_title = PhotoImage(file="logo1.png")
        title = Label(self, text="RETAIL PRO", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w",
                      padx=20).place(x=0, y=0, relwidth=1, height=70)

        title = Label(self, text="SALES DETAILS", font=("goudy old style", 15), bg="#0f4d7d",
                      fg="white").place(x=0, y=100, width=1150)

        btn_back = Button(self , text = "BACK" , font = ("goudy old style" , 10) , bg = "blue" , fg = "white" ,
                          command = self.dashboard , cursor = "hand2")
        btn_back.place(x = 1050 , y = 20 , width = 80 , height = 25)

        self.figure_purchase = Figure(figsize=(6, 4), dpi=100)
        self.axes_purchase = self.figure_purchase.add_subplot(111)

        self.figure_sales = Figure(figsize=(6, 4), dpi=100)
        self.axes_sales = self.figure_sales.add_subplot(111)

        self.figure_canvas_purchase = FigureCanvasTkAgg(self.figure_purchase, self)
        self.figure_canvas_purchase.get_tk_widget().place(x=20, y=140)

        self.figure_canvas_sales = FigureCanvasTkAgg(self.figure_sales, self)
        self.figure_canvas_sales.get_tk_widget().place(x=590, y=140)

        self.load_data()
        NavigationToolbar2Tk(self.figure_canvas_purchase, self)

    def load_data(self) :
        query_purchase = "SELECT SUM(total_price), `purchase_month` FROM `supplier` GROUP BY `purchase_month`"
        query_sales = "SELECT SUM(`total_amount`), `sale_month` FROM `customer` GROUP BY `sale_month`"

        # Fetch all data and initialize the lists with zeros for all months
        self.list_y_purchase = [0] * 12
        self.list_y_sales = [0] * 12

        self.cursor.execute(query_purchase)
        data_purchase = self.cursor.fetchall()
        for row in data_purchase :
            month_index = row[1] - 1  # Adjust month index to start from 0
            self.list_y_purchase[month_index] = row[0]

        self.cursor.execute(query_sales)
        data_sales = self.cursor.fetchall()
        for row in data_sales :
            month_index = row[1] - 1  # Adjust month index to start from 0
            self.list_y_sales[month_index] = row[0]

        self.plot_data()

    def plot_data(self):
        self.axes_purchase.clear()
        self.axes_sales.clear()

        months_abbr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        self.axes_purchase.bar(months_abbr, self.list_y_purchase, color='b')
        self.axes_purchase.set_title('Purchase Details')
        self.axes_purchase.set_xlabel('Month')
        self.axes_purchase.set_ylabel('Price')

        self.axes_sales.bar(months_abbr, self.list_y_sales, color='g')
        self.axes_sales.set_title('Sales Details')
        self.axes_sales.set_xlabel('Month')
        self.axes_sales.set_ylabel('Price')

        self.figure_canvas_purchase.draw()
        self.figure_canvas_sales.draw()

    def dashboard(self) :
        self.destroy()
        subprocess.run(['python' , 'dashboard.py'])

root = SalesClass()
root.mainloop()
