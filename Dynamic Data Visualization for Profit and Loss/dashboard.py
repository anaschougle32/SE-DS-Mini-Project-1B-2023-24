from tkinter import *
from PIL import Image, ImageTk
import subprocess


class Expentory:
	def __init__(self, root):
		self.root = root

		self.root.geometry("1350x700+0+0")
		self.root.title("RETAIL PRO")
		self.root.config(bg="white")
		# ====title====
		self.icon_title = PhotoImage(file="logo1.png")
		title = Label(self.root, text="RETAIL PRO", image=self.icon_title, compound=LEFT,
		              font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,
		                                                                                                         y=0,
		                                                                                                         relwidth=1,
		                                                                                                         height=70)

		# ======left Menu===
		self.MenuLogo = Image.open("menu_im.png")
		self.MenuLogo = self.MenuLogo.resize((1200, 700))
		self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

		Menu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
		Menu.place(x=5, y=70, width=1500, height=660)

		lbl_menuLogo = Label(Menu, image=self.MenuLogo)
		lbl_menuLogo.pack(side=TOP, fill=X)

		self.icon_side = PhotoImage(file="side.png")
		lbl_menu = Label(Menu, text="MENU", font=("times new roman", 40, 'bold')).place(x=50, y=40)

		Menu = Frame(self.root, bd=2, relief=RIDGE, bg="gray")
		Menu.place(x=30, y=180, width=220, height=490)

		btn_customer = Button(
			Menu,
			text="Customer",
			command=self.customer,
			image=self.icon_side,
			compound=LEFT,
			padx=3,
			anchor="w",
			font=("times new roman", 20, "bold"),
			bg="light gray",
			bd=5,
			cursor="hand1"
		).place(x=20, y=30)
		Button(width=7, pady=0, text='Profile',command=self.reg, bg='light blue', fg='black', border=3,
		       font=("times new roman", 15, "bold"),
		       ).place(x=1240, y=20)



		btn_supplier = Button(
			Menu,
			text="Supplier",
			command=self.supplier,
			image=self.icon_side,
			compound=LEFT,
			padx=3,
			anchor="w",
			font=("times new roman", 20, "bold"),
			bg="light gray",
			bd=5,
			cursor="hand1"
		).place(x=25, y=110)

		btn_inventory = Button(
			Menu,
			text="Inventory",
			command=self.inventory,
			image=self.icon_side,
			compound=LEFT,
			padx=3,
			anchor="w",
			font=("times new roman", 20, "bold"),
			bg="light gray",
			bd=5,
			cursor="hand2"
		).place(x=20, y=190)



		btn_sales = Button(
			Menu,
			text="Sales",
			image=self.icon_side,
			compound=LEFT,
			command = self.sales,
			padx=3,
			anchor="w",
			font=("times new roman", 20, "bold"),
			bg="light gray",
			bd=3,
			cursor="hand2"
		).place(x=45, y=270)

		btn_exit = Button(
			Menu,
			text="Exit",
			image=self.icon_side,
			compound=LEFT,
			command=self.exit,
			padx=3,
			anchor="w",
			font=("times new roman", 20, "bold"),
			bg="light gray",
			bd=5,
			cursor="hand2"
		).place(x=45, y=350)

		Button(width=7, pady=0, text='About Us', bg='light blue', fg='black', border=3,command=self.dashboardcopy,
		       font=("times new roman", 15, "bold"),
		       ).place(x=1135, y=20)


	def exit(self):
		self.root.destroy()
	# =====================================================================

	def customer(self):
		self.root.destroy()
		subprocess.run(['python', 'customer.py'])

	def supplier(self):
		self.root.destroy()
		subprocess.run(['python', 'supplier.py'])

	def inventory(self):
		self.root.destroy()
		subprocess.run(['python', 'inventory.py'])

	def sales(self):
		self.root.destroy()
		subprocess.run(['python', 'sales.py'])

	def reg(self):
		self.root.destroy()
		subprocess.run(['python', 'reg.py'])

	def dashboardcopy(self):
		self.root.destroy()
		subprocess.run(['python', 'dashboard.py'])
root = Tk()
obj = Expentory(root)
root.mainloop()