import tkinter as tk
from tkinter import ttk

import os

class Explain(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):
        self.gallery = [tk.PhotoImage(file=os.path.join("images/examples", f)) for f in os.listdir("images/examples/")]
        self.gallery_length = len(self.gallery)
        self.gallery_current_pos = 0

        #photo=tk.PhotoImage(file=self.gallery[0])
        self.label_gallery = ttk.Label(self, image=self.gallery[0])
        #self.label_gallery.image=photo # prevent garbage collection
        self.label_gallery.grid(row=0,column=1, sticky="news")

        self.button_previous = ttk.Button(self, text="<", command=self.next)
        self.button_previous.grid(row=0, column=0, sticky="news")

        self.button_next = ttk.Button(self, text=">", command=self.next)
        self.button_next.grid(row=0, column=2, sticky="news")

        self.label_history = ttk.Label(self, text="[HISTORY]")
        self.label_history.grid(row=1, column=0, columnspan=3, sticky="news")

        self.label_explanation = ttk.Label(self, text="By using this service, you are agreeing to the Regency Town House storing your images for an indefinite period of time, and allowing them to use it for artistic purposes.\n\nWe are going to make a silhouette of you in the style of the example images shown in the gallery to the left. You will have the opportunity to give your email ,and have it sent to you. Click the button below to begin.", wraplength=240)
        self.label_explanation.grid(row=0, column=3, sticky="news")

        self.button_begin = ttk.Button(self, text="Begin", command=self.controller.begin)
        self.button_begin.grid(row=1, column=3, sticky="news")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=20)

    def prev(self):
        self.gallery_current_pos = (self.gallery_current_pos - 1) % self.gallery_length
        self.label_gallery.config(image=self.gallery[self.gallery_current_pos])
    def next(self):
        self.gallery_current_pos = (self.gallery_current_pos + 1) % self.gallery_length
        self.label_gallery.config(image=self.gallery[self.gallery_current_pos])
