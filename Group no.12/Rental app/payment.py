from flask import Flask, render_template, request,jsonify
import razorpay
import socket

app = Flask(__name__)

def notify_payment_success():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 5555))  # IP address and port where Tkinter app is listening
    sock.send(b'payment_success')
    sock.close()

# Set up Razorpay client
razorpay_client = razorpay.Client(auth=("rzp_test_ApufYMBu9p1t2M", "xjyNi2iLXXN3lefeeb6T0UIg"))

@app.route('/')
def index():
    amount = request.args.get('amount', '15')  # Default to 15 if amount is not provided
    
    # Render the index.html template and pass the amount to it
    return render_template('index.html', amount=amount)

@app.route('/payment', methods=['POST'])
def payment():
    # Retrieve amount from form
    amount_str = request.form.get('amount')
    amount_str = amount_str.strip('/')
    if not amount_str:
        return "Amount not provided", 400

    amount = int(float(amount_str) * 100)  # Amount in paisa

    # Create Razorpay order
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'payment_capture': 1  # Auto-capture payment
    }
    order = razorpay_client.order.create(data=order_data)

    # Pass Razorpay order ID and amount to the payment template
    return render_template('payment_form.html', order_id=order['id'], amount=amount)

@app.route('/payment/success',methods=['POST'])
def payment_success():
    # Handle payment success here
    notify_payment_success()
    return render_template('payment_success.html')
if __name__ == '__main__':
    app.run(debug=True)
