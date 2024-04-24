import tkinter as tk
from tkinter import simpledialog
import webbrowser
import subprocess
import time



def redirect_to_payment(amount):

    # Define the URL of your Flask payment page
    payment_url = f"http://127.0.0.1:5000/?amount={amount}"
    
    # Open the payment URL in the default web browser
    webbrowser.open(payment_url)
    # Start the Flask server in a subprocess
    flask_process = subprocess.Popen(['python', 'payment.py'])

    # Wait for a short time to ensure the server starts up
    time.sleep(2)

# Create tkinter window
window = tk.Tk()
window.title("Payment Gateway")
window.geometry("500x500")

def get_amount():
    # Prompt the user to enter the amount
    amount = simpledialog.askfloat("Enter Amount", "Enter the amount to pay (INR):")
    if amount:
        redirect_to_payment(amount)

# Create a button to initiate payment
pay_button = tk.Button(window, text="Initiate Payment", command=get_amount)
pay_button.pack(pady=50)

# Run the tkinter event loop
window.mainloop()