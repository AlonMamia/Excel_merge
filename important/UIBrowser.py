import os

from components import *
from tkinter import messagebox


class FileSelect(tk.Frame):
    #initialize
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.flag = False
        self.initialize_user_interface()

    def initialize_user_interface(self):
        # self.parent.geometry("630x110")
        self.parent.title('מניעות חוב 1.1')
        self.parent.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.originalFileComp = FileBrowserContainer("בחר קובץ ישן")
        self.originalFileComp.grid(column=0, row=0, sticky=tk.W+tk.E)

        self.newFileComp = FileBrowserContainer("בחר קובץ חדש")
        self.newFileComp.grid(column=0, row=1, sticky=tk.EW)

        #confirm button
        self.confirm_button = ttk.Button(self.parent, text="אישור", command=self.Confirm)
        self.confirm_button.grid(row=3, columnspan=3, sticky=tk.S, padx=5, pady=5)

    def Confirm(self):
        if os.path.exists(self.originalFileComp.filePath) and os.path.exists(self.newFileComp.filePath):

            # print(self.originalFileComp.filePath + " " + self.newFileComp.filePath)
            self.flag = True
            self.parent.destroy()
        else:
            messagebox.showerror('שגיאה', 'שגיאה: נתיב קובץ אינו תקין')


class Process(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.parent.title('מניעות חוב')
        self.labelConfirm = Label(self.parent, text="התהליך הושלם בהצלחה")
        self.labelConfirm.pack()
        #confirm button
        self.ButtonConfirm = ttk.Button(self.parent, text="אישור", command=self.Confirm)
        self.ButtonConfirm.pack()

    def Confirm(self):
        self.parent.destroy()
