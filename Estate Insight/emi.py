
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_EMI(principal, annual_interest_rate, tenure_years):
    # Convert annual interest rate to monthly and calculate the number of installments
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_of_installments = tenure_years * 12

    # Calculating EMI using the formula
    EMI = (principal * monthly_interest_rate) * ((1 + monthly_interest_rate) ** number_of_installments) / \
          (((1 + monthly_interest_rate) ** number_of_installments) - 1)

    return EMI

def show_results():
    try:
        loan_amount = float(principal_entry.get())
        interest_rate = float(interest_entry.get())
        loan_tenure = int(loan_tenure_entry.get())

        EMI_result = calculate_EMI(loan_amount, interest_rate, loan_tenure)
        result_label.config(text=f"The Equated Monthly Installment (EMI) is: {EMI_result:.2f}")

        # Calculating total amount after repayment of loan, total interest, and total principal
        total_repayment = EMI_result * loan_tenure * 12
        total_interest = total_repayment - loan_amount
        total_principal = loan_amount
        total_loan_amount = total_repayment

        total_loan_label.config(text=f"Total Loan Amount After Repayment: {total_loan_amount:.2f}")

        # Visualizing the data in pie chart
        labels = ['Principal Amount', 'Total Interest Amount']
        sizes = [total_principal, total_interest]
        colors = ['#ff9999', '#66b3ff']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=60, colors=colors)
        ax.axis('equal')

        # Display the pie chart in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=6, column=0, columnspan=2, pady=10)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Creating the main window
root = tk.Tk()
root.title("Estateinsight - By Devesh")

principal_label = ttk.Label(root, text="Loan Amount:")
principal_label.grid(row=0, column=0, padx=10, pady=10)

principal_entry = ttk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

interest_label = ttk.Label(root, text="Annual Interest Rate (%):")
interest_label.grid(row=1, column=0, padx=10, pady=10)

interest_entry = ttk.Entry(root)
interest_entry.grid(row=1, column=1, padx=10, pady=10)

loan_tenure_label = ttk.Label(root, text="Loan Tenure (years):")
loan_tenure_label.grid(row=2, column=0, padx=10, pady=10)

loan_tenure_entry = ttk.Entry(root)
loan_tenure_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Calculate EMI", command=show_results)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

total_loan_label = ttk.Label(root, text="")
total_loan_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()