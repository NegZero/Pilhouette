import tkinter as tk
from tkinter import ttk

class Capture(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):
        self.placeholder_feed = tk.Label(self, bg="red")
        self.placeholder_feed.grid(row=0, column=0, sticky="news")

        self.button_capture = ttk.Button(self, text="Capture", command=self.capture)
        self.button_capture.grid(row=1, column=0, sticky="news")

        self.label_tips = ttk.Label(self, text="[TIPS]")
        self.label_tips.grid(row=0, column=1, sticky="news")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
    def capture(self):
        self.controller.capture()
