import tkinter as tk
from tkinter import ttk

import smtplib
#import email

class Send(tk.Frame):
    def __init__(self, master, controller, processed):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):
        self.processed = tk.PhotoImage(file="images/examples/placeholder3.gif")

        self.placeholder_processed = tk.Label(self, image=self.processed)
        self.placeholder_processed.grid(row=0, rowspan=3, column=0, sticky="news")

        self.label_email = ttk.Label(self, text="Email:")
        self.label_email.grid(row=0, column=1, sticky="news")

        self.entry_email = ttk.Entry(self)
        self.entry_email.grid(row=0, column=2, sticky="news")
        #TODO: Some kinda event for popping up onscreen keyboard

        self.button_send = ttk.Button(self, text="Send", command=self.send)
        self.button_send.grid(row=1, column=1, columnspan=2, sticky="news")

        self.label_status = ttk.Label(self, text="")
        self.label_status.grid(row=2, column=1, columnspan=2, sticky="news")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
    def send(self):
        self.label_status.config(text="Sending...")
        address = self.entry_email.get()
        self.master.after(1000, lambda:self.controller.success(address))
