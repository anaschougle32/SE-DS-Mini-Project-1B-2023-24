import tkinter as tk
import qrcode

class QRCodePayment(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("UPI Payment QR Code Generator")

        # Create a label to display the UPI ID
        self.label_upi_id = tk.Label(self, text="Enter UPI ID:")
        self.label_upi_id.grid(row=0, column=0, padx=10, pady=10)

        # Create an entry widget to input UPI ID
        self.entry_upi_id = tk.Entry(self)
        self.entry_upi_id.grid(row=0, column=1, padx=10, pady=10)

        # Create a label to display the amount
        self.label_amount = tk.Label(self, text="Enter Amount:")
        self.label_amount.grid(row=1, column=0, padx=10, pady=10)

        # Create an entry widget to input the amount
        self.entry_amount = tk.Entry(self)
        self.entry_amount.grid(row=1, column=1, padx=10, pady=10)

        # Create a button to generate QR code
        self.button_generate = tk.Button(self, text="Generate QR Code", command=self.generate_qr_code)
        self.button_generate.grid(row=2, columnspan=2, padx=10, pady=10)

        # Create a label to display QR code image
        self.qr_code_label = tk.Label(self)
        self.qr_code_label.grid(row=3, columnspan=2, padx=10, pady=10)

    def generate_qr_code(self):
        # Get UPI ID and amount from entry widgets
        upi_id = self.entry_upi_id.get()
        amount = self.entry_amount.get()

        # Construct the payment URL
        payment_url = f"upi://{upi_id}?amount={amount}"

        # Generate QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(payment_url)
        qr.make(fit=True)

        # Convert QR code to an image and display it
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img_tk = tk.PhotoImage(master=self, data=qr_img.tobytes())
        self.qr_code_label.configure(image=qr_img_tk)
        self.qr_code_label.image = qr_img_tk

if __name__ == "__main__":
    app = QRCodePayment()
    app.geometry("300x400")
    app.mainloop()
