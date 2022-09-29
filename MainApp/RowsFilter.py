import os
import tkinter as tk
from tkinter import ttk, messagebox

from comps import FileReader


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        label = tk.Label(self, text="סינון הקצאות", font=controller.title_font)
        label.grid(row=0, columnspan=3, sticky=tk.W + tk.E)

        self.FileComp = FileReader(self, "בחר קובץ")
        self.FileComp.grid(row=1, columnspan=3, sticky=tk.W + tk.E)

        self.confirm_button = ttk.Button(self, text="אישור", command=self.confirm)
        self.confirm_button.grid(row=3, columnspan=3, sticky=tk.S, padx=5, pady=5)

        # navigation buttons
        self.nav = ttk.Button(self, text="עמוד ראשי",
                              command=lambda: controller.show_frame("StartPage"))
        self.nav.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

    def confirm(self):
        if os.path.exists(self.FileComp.filePath):
            self.script()
        else:
            messagebox.showerror('שגיאה', 'שגיאה: נתיב קובץ אינו תקין')

    def script(self):
        print("ok!")