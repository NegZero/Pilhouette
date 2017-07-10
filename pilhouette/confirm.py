import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

import os

class Confirm(tk.Frame):
    def __init__(self, master, controller, image):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.image = image
        self.create_widgets()
    def create_widgets(self):
        self.filenames = os.listdir("temp/processed/")
        images = [Image.open(os.path.join("temp/processed", f)) for f in self.filenames]
        self.gallery = [ImageTk.PhotoImage(i.resize((270,360), Image.LANCZOS)) for i in images]
        self.gallery_length = len(self.gallery)
        self.gallery_current_pos = 0

        self.feed = ImageTk.PhotoImage(image=self.image.resize((270,360)))
        #self.processed = tk.PhotoImage(file="images/examples/placeholder3.gif")
        self.placeholder_raw = tk.Label(self, image=self.feed)
        self.placeholder_raw.grid(row=0, column=0, sticky="news")

        self.button_retake = ttk.Button(self, text="Retake", command=self.controller.retake)
        self.button_retake.grid(row=1, column=0, sticky="news")

        self.label_gallery = tk.Label(self, image=self.gallery[self.gallery_current_pos])
        self.label_gallery.grid(row=0, column=2, sticky="news")

        self.button_prev = ttk.Button(self, text="<", command=self.prev)
        self.button_prev.grid(row=0, column=1, sticky="news")

        self.button_next = ttk.Button(self, text=">", command=self.next)
        self.button_next.grid(row=0, column=3, sticky="news")

        self.button_confirm = ttk.Button(self, text="Confirm", command=lambda:self.controller.confirm(self.gallery[self.gallery_current_pos], self.filenames[self.gallery_current_pos]))
        self.button_confirm.grid(row=1, column=1, columnspan=3, sticky="news")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        #self.rowconfigure(2, weight=1)
        #self.rowconfigure(3, weight=2)
        self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
    def prev(self):
        self.gallery_current_pos = (self.gallery_current_pos - 1) % self.gallery_length
        self.label_gallery.config(image=self.gallery[self.gallery_current_pos])
    def next(self):
        self.gallery_current_pos = (self.gallery_current_pos + 1) % self.gallery_length
        self.label_gallery.config(image=self.gallery[self.gallery_current_pos])

