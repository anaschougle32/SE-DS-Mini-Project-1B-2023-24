from tkinter import Tk, Frame, Scrollbar, Label, Entry, Text, Button, messagebox  # Tkinter Python Module for GUI
import socket  # Sockets for network connection
import threading  # for multiple processes


class GUI:
    client_socket = None
    last_received_message = None

    def __init__(self, master):
        self.root = master
        self.initialize_socket()
        self.initialize_gui()
        self.listen_for_incoming_messages_in_a_thread()

    def initialize_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initializing socket with TCP and IPv4
        remote_ip = '127.0.0.1'  # IP address
        remote_port = 10319  # TCP port
        self.client_socket.connect((remote_ip, remote_port))  # Connect to the remote server

    def initialize_gui(self):  # GUI initializer
        self.root.title("Socket Chat")
        self.root.resizable(0, 0)

        # Chat box section
        chat_box_frame = Frame(self.root)
        chat_box_frame.pack(padx=10, pady=10, fill='both', expand=True)

        Label(chat_box_frame, text='Chat Box:', font=("Serif", 12)).pack(side='top', anchor='w')

        self.chat_transcript_area = Text(chat_box_frame, width=60, height=10, font=("Serif", 12))
        self.chat_transcript_area.pack(side='left', padx=10, fill='both', expand=True)

        scrollbar = Scrollbar(chat_box_frame, command=self.chat_transcript_area.yview, orient='vertical')
        scrollbar.pack(side='right', fill='y')

        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)
        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')

        # Name section
        name_frame = Frame(self.root)
        name_frame.pack(padx=10, pady=(0, 5), fill='x')

        Label(name_frame, text='Enter your name:', font=("Helvetica", 12)).pack(side='left')

        self.name_widget = Entry(name_frame, width=40, borderwidth=2)
        self.name_widget.pack(side='left')

        self.join_button = Button(name_frame, text="Join", width=10, command=self.on_join)
        self.join_button.pack(side='left')

        # Entry section
        entry_frame = Frame(self.root)
        entry_frame.pack(padx=10, pady=(5, 10), fill='x')

        Label(entry_frame, text='Enter message:', font=("Serif", 12)).pack(side='left')

        self.enter_text_widget = Text(entry_frame, width=40, height=3, font=("Serif", 12))
        self.enter_text_widget.pack(side='left')

        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)

    def listen_for_incoming_messages_in_a_thread(self):
        thread = threading.Thread(target=self.receive_message_from_server, args=(self.client_socket,))
        thread.start()

    def receive_message_from_server(self, so):
        while True:
            buffer = so.recv(256)
            if not buffer:
                break
            message = buffer.decode('utf-8')

            if "joined" in message:
                user = message.split(":")[1]
                message = user + " has joined"
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview('end')
            else:
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview('end')

        so.close()

    def on_join(self):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter your name", "Enter your name to send a message")
            return
        self.name_widget.config(state='disabled')
        self.client_socket.send(("joined:" + self.name_widget.get()).encode('utf-8'))

    def on_enter_key_pressed(self, event):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter your name", "Enter your name to send a message")
            return
        self.send_chat()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')

    def send_chat(self):
        senders_name = self.name_widget.get().strip() + ": "
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview('end')
        self.client_socket.send(message)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'


root = Tk()
gui = GUI(root)
root.mainloop()

