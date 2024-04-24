import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Display Image")

# Load the image file
image = Image.open("bg_image.jpg")

# Resize the image if needed
# image = image.resize((width, height), Image.ANTIALIAS)

# Convert the image for Tkinter
tk_image = ImageTk.PhotoImage(image)

# Create a label widget to display the image
label = tk.Label(window, image=tk_image)
label.pack()

# Run the Tkinter event loop
window.mainloop()
