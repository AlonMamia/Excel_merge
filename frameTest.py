# Import Module
import tkinter
from tkinter import *
import tkinter as tk
# Create Tkinter Object
root = Tk()

# Set Geometry
root.geometry("400x400")

# Frame 1
frame1 = Frame(root, bg="black", width=500, height=300)
frame1.pack()

# Frame 2
frame2 = Frame(frame1, bg="white", width=100, height=100)
frame2.pack(pady=20, padx=20)

class container(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        frame3 = Frame(parent, bg="black", width=10, height=10)
        frame3.pack(pady=20, padx=20)

a = container(frame2)
a.pack()
# frame3 = Frame(frame2, bg="black", width=10, height=10)
# frame3.pack(pady=20, padx=20)

# Execute Tkinter
root.mainloop()