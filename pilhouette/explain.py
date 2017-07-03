import tkinter as tk
from tkinter import ttk

class Explain(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):
        photo=tk.PhotoImage(file="images/blank.gif").subsample(2,2)
        self.label_gallery = ttk.Label(self, image=photo)
        self.label_gallery.image=photo # prevent garbage collection
        self.label_gallery.grid(row=0,column=1, sticky="news")

        self.button_previous = ttk.Button(self, text="<", command=self.next)
        self.button_previous.grid(row=0, column=0, sticky="news")

        self.button_next = ttk.Button(self, text=">", command=self.next)
        self.button_next.grid(row=0, column=2, sticky="news")

        self.label_history = ttk.Label(self, text="History")
        self.label_history.grid(row=1, column=0, columnspan=3, sticky="news")

        self.label_explanation = ttk.Label(self, text="[DISCLAIMER]\n\n[INSTRUCTIONS]")
        self.label_explanation.grid(row=0, column=3, sticky="news")

        self.button_begin = ttk.Button(self, text="Begin", command=self.controller.begin)
        self.button_begin.grid(row=1, column=3, sticky="news")

        #self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=20)

    def prev(self):
        pass
    def next(self):
        pass
