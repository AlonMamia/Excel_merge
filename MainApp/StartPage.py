import tkinter as tk
from tkinter import ttk
from tkinter import *


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ממשק רפאל", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="מניעות חוב",
                             command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        button2 = ttk.Button(self, text="סינון הקצאות",
                             command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

        button3 = ttk.Button(self, text="סינון הקצאות",
                             command=lambda: controller.show_frame("PageTest"))
        button3.pack()

        # buttonContainer = ttk.LabelFrame(self, text="תפריט", relief=tk.RIDGE)
        # buttonContainer.pack()
        # button4 = ttk.Button(buttonContainer, text="do task " + "ok",
        #                      command=lambda: controller.show_frame("PageTest"))
        # button4.pack()