from tkinter import *


root = Tk()
root.geometry("835x616")
root.title("Student Information")
name_label = Label(root,text="Name")
name_label.place(relx=0.1,rely=0.2)
name_text = Entry(root,width=20)
name_text.place(relx=0.15,rely=0.2)
gender_label = Label(root,text="Gender")
gender_label.place(relx=0.1,rely=0.25)
gender_text = Entry(root,width=20)
gender_text.place(relx=0.15,rely=0.25)
dob_label = Label(root,text="Date of birth")
dob_label.place(relx=0.2,rely=0.2)
dob_text = Entry(root,width=20)
name_text.place(relx=0.15,rely=0.2)

root.mainloop()