import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Welcome(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
        self.selection = ""
    def create_widgets(self):

        self.splash = ImageTk.PhotoImage(Image.open("images/welcome.png"))

        self.label_splash = tk.Label(self, image=self.splash)
        self.label_splash.grid(row=0, rowspan=5, column=0, sticky="news")

        self.label_langsel = ttk.Label(self, text="Select a language to begin")
        self.label_langsel.grid(row=0, column=1)

        self.button_en = ttk.Button(self, text="English",
                command=lambda:self.controller.set_lang("en"))
        self.button_fr = ttk.Button(self, text="Français",
                command=lambda:self.controller.set_lang("fr"))
        self.button_de = ttk.Button(self, text="Deutsch",
                command=lambda:self.controller.set_lang("de"))
        self.button_es = ttk.Button(self, text="Español",
                command=lambda:self.controller.set_lang("es"))

        # sticky parameter lets the widget fill the cell
        self.button_en.grid(row=1, column=1, sticky="news")
        self.button_fr.grid(row=2, column=1, sticky="news")
        self.button_de.grid(row=3, column=1, sticky="news")
        self.button_es.grid(row=4, column=1, sticky="news")

        # weights allow rows/cols to stretch as necessary
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=7)
        self.rowconfigure(2, weight=7)
        self.rowconfigure(3, weight=7)
        self.rowconfigure(4, weight=7)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
