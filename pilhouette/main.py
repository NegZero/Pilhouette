#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk

import welcome
import explain
import capture
import confirm
import send
import success
import home

class AppController(ttk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.current_frame = self.frame_welcome = welcome.Welcome(self.master, self)
        #self.frame_welcome.pack(fill=tk.BOTH, expand=True)
        self.frame_welcome.grid(row=0, column=0, sticky="news")
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=0)

    def set_lang(self, lang):
        self.lang = lang
        print("lang set to {}".format(self.lang))
        self.frame_welcome.destroy()

        self.frame_home = home.Home(self.master, self)
        self.frame_home.grid(row=1, column=0, sticky="news")

        self.current_frame = self.frame_explain = explain.Explain(self.master, self)
        #self.frame_explain.pack(fill=tk.BOTH, expand=True)
        self.frame_explain.grid(row=0,column=0, sticky="news")

        self.master.grid_rowconfigure(0, weight=7)
        self.master.grid_rowconfigure(1, weight=1)

    def home(self):
        self.current_frame.destroy()
        self.frame_home.destroy()
        self.create_widgets()
        #print("home pressed")

    def begin(self):
        self.frame_explain.destroy()
        self.current_frame = self.frame_capture = capture.Capture(self.master, self)
        #self.frame_capture.pack(fill=tk.BOTH, expand=True)
        self.frame_capture.grid(row=0, column=0, sticky="news")

    def capture(self, image):
        self.frame_capture.destroy()
        self.current_frame = self.frame_confirm = confirm.Confirm(self.master, self, image)
        #self.frame_confirm.pack(fill=tk.BOTH, expand=True)
        self.frame_confirm.grid(row=0, column=0, sticky="news")

    def retake(self):
        self.frame_confirm.destroy()
        self.current_frame = self.frame_capture = capture.Capture(self.master, self)
        #self.frame_capture.pack(fill=tk.BOTH, expand=True)
        self.frame_capture.grid(row=0, column=0, sticky="news")

    def confirm(self, image, filename):
        self.frame_confirm.destroy()
        self.current_frame = self.frame_send = send.Send(self.master, self, image, filename)
        #self.frame_email.pack(fill=tk.BOTH, expand=True)
        self.frame_send.grid(row=0, column=0, sticky="news")

    def success(self, address):
        self.frame_send.destroy()
        self.current_frame = self.frame_success = success.Success(self.master, self, address)
        #self.frame_success.pack(fill=tk.BOTH, expand=True)
        self.frame_success.grid(row=0, column=0, sticky="news")

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.geometry("800x480")
    App = AppController(root)
    App.mainloop()
