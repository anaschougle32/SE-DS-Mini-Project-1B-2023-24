import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import simpledialog

class TravelChecklistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Checklist")

        # Connect to MySQL database
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1927__sid",
                database="test"
            )
            self.cur = self.conn.cursor()

            self.create_widgets()
            self.load_checklist()
        except mysql.connector.Error as err:
            messagebox.showerror("MySQL Error", f"Failed to connect to MySQL database: {err}")

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="Travel Checklist")
        self.label.pack(pady=10)

        # Checklist Listbox
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(self.root, text="Remove Item", command=self.remove_item)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.modify_button = tk.Button(self.root, text="Modify Item", command=self.modify_item)
        self.modify_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_checklist)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.root, text="Clear List", command=self.clear_list)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.update_listbox()

    def add_item(self):
        item = simpledialog.askstring("Add Item", "Enter item to add:")
        if item:
            self.cur.execute("INSERT INTO checklist (item) VALUES (%s)", (item,))
            self.conn.commit()
            self.update_listbox()

    def remove_item(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            item_id = self.listbox.get(index).split(".")[0]
            self.cur.execute("DELETE FROM checklist WHERE id=%s", (item_id,))
            self.conn.commit()
            self.update_listbox()

    def modify_item(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            item_id = self.listbox.get(index).split(".")[0]
            current_item = self.listbox.get(index).split(".")[1].strip()
            new_item = simpledialog.askstring("Modify Item", "Enter new item:", initialvalue=current_item)
            if new_item:
                self.cur.execute("UPDATE checklist SET item=%s WHERE id=%s", (new_item, item_id))
                self.conn.commit()
                self.update_listbox()

    def save_checklist(self):
        items = self.listbox.get(0, tk.END)
        self.cur.execute("DELETE FROM checklist")
        for item in items:
            item_text = item.split(".")[1].strip()
            self.cur.execute("INSERT INTO checklist (item) VALUES (%s)", (item_text,))
        self.conn.commit()
        messagebox.showinfo("Saved", "Checklist saved successfully.")

    def clear_list(self):
        self.cur.execute("DELETE FROM checklist")
        self.conn.commit()
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        self.cur.execute("SELECT * FROM checklist")
        rows = self.cur.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, f"{row[0]}. {row[1]}")

    def load_checklist(self):
        self.update_listbox()

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelChecklistApp(root)
    root.mainloop()
