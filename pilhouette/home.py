import tkinter as tk
from tkinter import ttk

class Home(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):
        self.button_home = ttk.Button(self, text="Home", command=self.controller.home)
        self.button_home.grid(row=0, column=0, sticky="nes")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

