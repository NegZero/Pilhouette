import tkinter as tk
from tkinter import ttk

class Success(tk.Frame):
    def __init__(self, master, controller, address):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.address = address
        self.create_widgets()
    def create_widgets(self):
        self.label_thankyou = ttk.Label(self, text="Thank you for using Pilhouette!")
        self.label_thankyou.grid(row=0,column=0, columnspan=2)

        self.label_success = ttk.Label(self, text="Email sent successfully to {}".format(self.address))
        self.label_success.grid(row=1, column=0)

        self.button_toggle = ttk.Button(self)
        self.button_toggle.grid(row=1,column=1)
        self.address_toggle(False)

        self.label_spam = ttk.Label(self, text="[SPAM MESSAGE]")
        self.label_spam.grid(row=2, column=0, columnspan=2)

        self.label_timer = ttk.Label(self, text="Restarting in 10 seconds...")
        self.label_timer.grid(row=3, column=0, columnspan=2)
        self.countdown(10)
    def address_toggle(self, visible): # boolean, true if currently visible
        if visible: # hide the address
            self.label_success.config(text="Email sent successfully")
            self.button_toggle.config(text="Show address", command=lambda:self.address_toggle(not visible)) # not visible == False
        else: # show the address
            self.label_success.config(text="Email sent successfully to {}".format(self.address))
            self.button_toggle.config(text="Hide address", command=lambda:self.address_toggle(not visible)) # not visible == True
    def countdown(self, seconds):
        if seconds > 0:
            self.label_timer.config(text="Restarting in {} seconds...".format(seconds))
            self.master.after(1000, lambda:self.countdown(seconds-1))
        else:
            self.controller.home()

