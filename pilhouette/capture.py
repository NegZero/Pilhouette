import tkinter as tk
from tkinter import ttk

import cv2
import numpy as np

class Capture(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.create_widgets()
        self.process()
    def create_widgets(self):
        self.feed = tk.PhotoImage(file="images/examples/placeholder2.gif")
        self.placeholder_feed = tk.Label(self, image=self.feed)
        self.placeholder_feed.grid(row=0, column=0, sticky="news")

        self.button_capture = ttk.Button(self, text="Capture", command=self.capture)
        self.button_capture.grid(row=1, column=0, sticky="news")

        self.label_tips = ttk.Label(self, text="When you are ready to take a picture, press the 'Capture' button.\n\nRemember that only your outline will be seen in the final silhouette, so try and pose in a way that makes for an interesting result.\n\nDon't be afraid to experiment, you can retake your picture as many times as you want!", wraplength=450)
        self.label_tips.grid(row=0, column=1, sticky="news")

        self.label_status = ttk.Label(self)
        self.label_status.grid(row=1, column=1, sticky="news")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
    def capture(self):
        self.label_status.config(text="Generating...")
        self.process()
        self.controller.capture()
    def process(self):
        # Read in grayscale
        grayscale = cv2.imread("temp/raw.png", cv2.IMREAD_GRAYSCALE)
        # Add a 1px border so findContours correctly detects edges at the border
        bgrayscale = cv2.copyMakeBorder(grayscale, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=[255,255,255])

        # Inverted threshold with pixels whiter than 210, going to black, rest white
        r, thresh = cv2.threshold(bgrayscale, 210, 255, cv2.THRESH_BINARY_INV)

        #  Finds only external contours
        cont = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

        # Fills in the foreground
        cv2.drawContours(thresh, cont, -1, [255, 255, 255], cv2.FILLED)

        # Remove the 1px border we created earlier
        thresh = thresh[1:-1, 1:-1]

        # Write the files as lossless PNG for good quality edges
        cv2.imwrite("temp/processed/wb.png", thresh)
        cv2.imwrite("temp/processed/bw.png", cv2.bitwise_not(thresh))
