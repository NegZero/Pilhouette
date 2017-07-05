import tkinter as tk
from tkinter import ttk

class Confirm(tk.Frame):
    def __init__(self, master, controller, image):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):
        self.feed = tk.PhotoImage(file="images/examples/placeholder2.gif")
        self.processed = tk.PhotoImage(file="images/examples/placeholder3.gif")
        self.placeholder_raw = tk.Label(self, image=self.feed)
        self.placeholder_raw.grid(row=0, rowspan=3, column=0, sticky="news")

        self.button_retake = ttk.Button(self, text="Retake", command=self.controller.retake)
        self.button_retake.grid(row=3, column=0, sticky="news")

        self.placeholder_processed = tk.Label(self, image=self.processed)
        self.placeholder_processed.grid(row=1, column=1, sticky="news")

        self.button_prev = ttk.Button(self, text="Previous")
        self.button_prev.grid(row=0, column=1, sticky="news")

        self.button_next = ttk.Button(self, text="Next")
        self.button_next.grid(row=2, column=1, sticky="news")

        self.button_confirm = ttk.Button(self, text="Confirm", command=self.controller.confirm)
        self.button_confirm.grid(row=3, column=1, sticky="news")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
