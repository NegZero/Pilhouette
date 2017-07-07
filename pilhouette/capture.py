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
    def create_widgets(self):
        self.feed = tk.PhotoImage(file="images/examples/placeholder2.gif")
        self.placeholder_feed = tk.Label(self, image=self.feed)
        self.placeholder_feed.grid(row=0, column=0, sticky="news")

        self.button_capture = ttk.Button(self, text="Capture", command=self.capture)
        self.button_capture.grid(row=1, column=0, sticky="news")

        self.label_tips = ttk.Label(self, text="[TIPS]")
        self.label_tips.grid(row=0, column=1, sticky="news")

        self.label_status = ttk.Label(self)
        self.label_status.grid(row=0, column=1, sticky="news")

        #self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        #self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
    def capture(self):
        self.label_status.config(text="Generating...")
        self.process()
        self.controller.capture()
    def process(self):
        grayscale = cv2.imread("temp/raw.jpg", cv2.IMREAD_GRAYSCALE)
        bgrayscale = cv2.copyMakeBorder(grayscale, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=[255,255,255])

        r, thresh = cv2.threshold(bgrayscale, 210, 255, cv2.THRESH_BINARY_INV)
        cont = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

        cv2.drawContours(thresh, cont, -1, [255, 255, 255], cv2.FILLED)
        """
        # Every pixel above 210 will be white
        ret, thresh = cv2.threshold(grayscale, 210, 255, cv2.THRESH_BINARY)
        h, w = thresh.shape[:2] # discards last element in tuple (# of channels)
        cv2.copyMakeBorder(thresh, 2, 2, 2, 2, cv2.BORDER_CONSTANT)
        slate = np.zeros((h, w), np.uint8)i
        outline = cv2.findContours(thresh, cv2.RETR_EXiTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        cv2.drawContours(slate, outline, -1, (255,0,255), cv2.FILLED)"""
        cv2.imwrite("temp/processed/wb.png", thresh)
        cv2.imwrite("temp/processed/bw.png", cv2.bitwise_not(thresh))
        """
        filled = thresh.copy()

        cv2.floodFill(filled, mask, (0,0), 255)

        inv_filled = cv2.bitwise_not(filled)

        wb = thresh | inv_filled
        bw = cv2.bitwise_not(wb)

        cv2.imwrite("temp/processed/wb.png", wb)
        cv2.imwrite("temp/processed/bw.png", bw)
        """

