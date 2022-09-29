from tkinter import *
import tkinter as tk
from tkinter import ttk

root =Tk()
root.title('code')

frame = LabelFrame(root,text='this is a frame!',padx=5,pady=5)
frame.pack(padx=10,pady=10)

frame2 = LabelFrame(root,text='this is a frame!',padx=5,pady=5)
frame2.pack(padx=10,pady=10)



k = Button(frame, text="Click ok")
k.pack()

"""
    frame is parent
"""

class container(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.filePath = ''
        self.sheetName = ''
        self.selectedSheet = StringVar(self)
        self.om_variable = tk.StringVar(self)
        self.om_variable.set("בחר גיליון")
        self.df = ''

        self.dropDown = ttk.OptionMenu(self, self.om_variable, ())
        self.dropDown.grid(column=1, row=0, sticky=tk.S, padx=5, pady=5)
        self.dropDown.config(width=30)

        self.entry = tk.Entry(self)
        self.entry.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5, ipadx=150)


a = container(frame)
a.pack()

b = container(frame)
b.pack()

root.mainloop()