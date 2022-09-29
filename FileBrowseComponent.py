from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd


# class widg(tk.Frame):
#     def __init__(self):
#         super(widg, self).__init__()
#         self.entry = tk.Entry(self)
#         self.ent1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5, ipadx=150)
#
#         # self.ent1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5, ipadx=150)


class ButtonTest(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        b4_button = Button(self.parent, text="Geeks4", fg="green")
        b4_button.pack(side=BOTTOM)

        b5_button = Button(self.parent, text="Geeks5", fg="green")
        b5_button.pack(side=BOTTOM)

        b6_button = Button(self.parent, text="Geeks6", fg="green")
        b6_button.pack(side=BOTTOM)

class MyButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'red'

    #   def __init__(self, *args, **kwargs):
    #     OptionMenu.__init__(self, *args, **kwargs)
    #     self.selectedSheet = StringVar(self.parent)
    #     self.sheetList = ["בחר גיליון"]
    #     self.pathOriginal = ''
    #     self.pathNew = ''
    #     self.originalXLS = ''
    #     self.newXLS = ''
    #     self.initialize_user_interface()

class FileBrowserComponent():
    def __init__(self, rows, columns):
        self.selectedSheet = StringVar(self.parent)
        self.sheetList = ["בחר גיליון"]
        self.pathOriginal = ''
        self.pathNew = ''
        self.originalXLS = ''
        self.newXLS = ''
        self.initialize_user_interface()



    def initialize_user_interface(self):
        self.entry_label = tk.Button(self.parent, text="בחר קובץ ישן", command=self.SetFilePath)
        self.entry_label.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)
        self.entry = tk.Entry(self.parent)
        self.entry.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5, ipadx=150)
        #sheet Dropdown original
        self.dropDown = ttk.OptionMenu(self.parent, self.selectedSheet, self.sheetList[0], *self.sheetList)
        self.dropDown.grid(column=1, row=0, sticky=tk.S, padx=5, pady=5)

    def SetFilePath(self):
        filename1 = filedialog.askopenfilename(filetypes=(("Excel קבצי", ".xlsx"), ("All files", ".*")))
        self.entry.delete(0, END)
        self.entry.insert(tk.END, filename1)


# root = tk.Tk()
# ui = FileBrowserComponent(root)
# print(ui.selectedSheetOriginal.get())
# root.mainloop()