import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

import os

class Explain(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):
        filenames = os.listdir("images/examples/")
        images = [Image.open(os.path.join("images/examples/", f)) for f in filenames]
        self.gallery = [ImageTk.PhotoImage(i) for i in images]
        self.gallery_length = len(self.gallery)
        self.gallery_current_pos = 0

        #photo=tk.PhotoImage(file=self.gallery[0])
        self.label_gallery = ttk.Label(self, image=self.gallery[self.gallery_current_pos])
        #self.label_gallery.image=photo # prevent garbage collection
        self.label_gallery.grid(row=0,column=1, sticky="news")

        self.button_prev = ttk.Button(self, text="<", command=self.prev)
        self.button_prev.grid(row=0, column=0, sticky="news")

        self.button_next = ttk.Button(self, text=">", command=self.next)
        self.button_next.grid(row=0, column=2, sticky="news")

        self.label_disclaimer = ttk.Label(self, text="By using this you are agreeing to permit us to store your email address and include your silhouette portrait within the Profiles of the Past project.", wraplength=420)
        self.label_disclaimer.grid(row=1, column=0, columnspan=3, sticky="news")

        self.label_explanation = ttk.Label(self, text="Artists making silhouette portraits in the 18th and 19th centuries used a variety of silhouette machines. Our 21st century version uses a digital camera and the Raspberry Pi processor.\n\nUsing this machine you can take a silhouette 'selfie' like the ones on the screen and then email it to yourself. Click 'Begin' to get started.", wraplength=360)
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
