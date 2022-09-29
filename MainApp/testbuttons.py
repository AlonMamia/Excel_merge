import os
import tkinter as tk
from tkinter import ttk, messagebox

from comps import FileReader


class PageTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        label = tk.Label(self, text="test", font=controller.title_font)
        label.grid(row=0, columnspan=3, sticky=tk.W + tk.E)

        self.create_widgets()


        self.originalFileComp = FileReader(self, "בחר קובץ ישן")
        self.originalFileComp.grid(row=1, columnspan=3, sticky=tk.W + tk.E)

        # navigation buttons
        self.nav = ttk.Button(self, text="עמוד ראשי",
                              command=lambda: controller.show_frame("StartPage"))
        self.nav.grid(row=4, columnspan=3, sticky=tk.S, padx=5, pady=5)

    def confirm(self):
        if os.path.exists(self.FileComp.filePath):
            self.script()
        else:
            messagebox.showerror('שגיאה', 'שגיאה: נתיב קובץ אינו תקין')

    def script(self):
        print("ok!")

    def create_buttons(self, parent, a, b, c):
        button1 = ttk.Button(parent, text="do task " + a)
        button1.grid(row=1, column=1)
        button2 = ttk.Button(parent, text="do task " + b)
        button2.grid(row=2, column=1)
        button3 = ttk.Button(parent, text="do task " + c)
        button3.grid(row=3, column=1)

        return (button1, button2, button3)

    def create_widgets(self):

        frame = ttk.LabelFrame(self, text="תפריט", relief=tk.RIDGE)
        frame.grid(row=4, column=1, sticky=tk.N + tk.S, padx=30, pady=4)
        self.create_buttons(frame, "D", "E", "F")
        button4 = ttk.Button(frame, text="do task " + "ok")
        button4.grid(row=4, column=1)