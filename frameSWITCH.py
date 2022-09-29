try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
# from test2 import container
from important.components import *

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Go to Page Three",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        # a = container(frame)
        # a.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        a = container(self)
        a.pack()

class container(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        frame3 = tk.Frame(parent, bg="black", width=10, height=10)
        frame3.pack(pady=20, padx=20)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()

        button2 = tk.Button(self, text="Go to the page 2",
                           command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

        frameMe = confirMe(self)
        frameMe.pack()

        # #confirm button
        # self.confirm_button = ttk.Button(self, text="אישור", command=self.Confirm)
        # self.confirm_button.pack()

    def Confirm(self):
        messagebox.showerror('OK', 'its ok!')

class confirMe(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.confirm_button = ttk.Button(self, text="אישור", command=self.Confirm)
        self.confirm_button.pack()

    def Confirm(self):
        print("ok")

# class Selector(tk.Frame):
#     #initialize
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.parent = parent
#         self.flag = False
#         self.initialize_user_interface()
#
#     def initialize_user_interface(self):
#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=3)
#
#         self.originalFileComp = FileBrowserContainer("בחר קובץ ישן")
#         self.originalFileComp.pack()
#
#         self.newFileComp = FileBrowserContainer("בחר קובץ חדש")
#         self.newFileComp.pack()
#
#         #confirm button
#         self.confirm_button = ttk.Button(self.controller, text="אישור", command=self.Confirm)
#         self.confirm_button.pack()
#
#     def Confirm(self):
#         if os.path.exists(self.originalFileComp.filePath) and os.path.exists(self.newFileComp.filePath):
#
#             print(self.originalFileComp.filePath + " " + self.newFileComp.filePath)
#             self.flag = True
#             # self.parent.destroy()
#             messagebox.showerror('OK', 'its ok!')
#         else:
#             messagebox.showerror('שגיאה', 'שגיאה: נתיב קובץ אינו תקין')



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()