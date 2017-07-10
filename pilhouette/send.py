import tkinter as tk
from tkinter import ttk

import re
import subprocess

from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

SMTP_SERVER = "smtp.gmail.com:587"
SMTP_USER = "picam@rth.org.uk"
SMTP_PASS = "R4spb3rry"

class Send(tk.Frame):
    def __init__(self, master, controller, image, filename):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.image = image
        self.filename = filename
        self.create_widgets()
    def create_widgets(self):
        self.placeholder_processed = tk.Label(self, image=self.image)
        self.placeholder_processed.grid(row=0, rowspan=5, column=0, sticky="news")

        self.label_message = ttk.Label(self, text="Please make sure you have entered your correct email address before pressing the 'Send' button - we cannot tell if you have entered the incorrect email address.", wraplength=480)
        self.label_message.grid(row=0, column=1, columnspan=2, sticky="news")

        self.label_email = ttk.Label(self, text="Email:")
        self.label_email.grid(row=1, column=1, sticky="news")

        self.entry_email = ttk.Entry(self)
        self.entry_email.grid(row=1, column=2, sticky="news")
        self.entry_email.bind("<FocusIn>", self.keyboard_open)
        self.entry_email.bind("<FocusOut>", self.keyboard_close )
        #TODO: Some kinda event for popping up onscreen keyboard

        self.button_send = ttk.Button(self, text="Send", command=self.send)
        self.button_send.grid(row=2, column=1, columnspan=2, sticky="news")

        self.label_status = ttk.Label(self, text="")
        self.label_status.grid(row=3, column=1, columnspan=2, sticky="news")

        self.placeholder_keyboard = tk.Label(self)
        self.placeholder_keyboard.grid(row=4, column=1, columnspan=2, sticky="news")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
    def keyboard_open(self):
        self.keyboard = subprocess.Popen("matchbox-keyboard")
    def keyboard_close(self):
        self.keyboard.terminate()
    def send(self):
        self.label_status.config(text="Sending...")
        address = self.entry_email.get()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", address): # basic loose regex
            self.label_status.config(text="The entered email is syntactically invalid, try again.")
        else:
            try:
                msg = MIMEMultipart()

                msg["From"] = SMTP_USER
                msg["To"] = address
                msg["Subject"] = "Here's your silhouette!"
                msg.preamble = "Here's your silhouette"

                body = MIMEText('''<h1>Here's your silhouette</h1>
        <p>Thank you for using Pilhouette!</p>
        <p>You can find your silhouette attached to this email.</p>
        <hr />
        <img src="http://brightonfoodfestival.com/wp-content/uploads/2013/07/regency_town_house.jpg"/>''', _subtype='html')
                msg.attach(body)

                with open("temp/processed/"+self.filename, "rb") as f:
                        s_data = f.read()
                s = MIMEImage(s_data)
                s.add_header("Content-Disposition", "attachment", filename="silhouette.png")
                msg.attach(s)

                with smtplib.SMTP(SMTP_SERVER) as s:
                    #s.ehlo()
                    s.starttls()
                    s.login(SMTP_USER, SMTP_PASS)
                    s.send_message(msg)

                self.controller.success(address)
            except:
                self.label_status.config(text="An error occurred, try again.")
