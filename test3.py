import tkinter as tk
from tkinter import ttk, filedialog, END
import pandas as pd

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, tst):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack(side="top", fill="both", expand=True)

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(side="top", fill="both", expand=True)

        button3 = tk.Button(self, text="Visit Page 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(side="top", fill="both", expand=True)

        button4 = tk.Button(self, text="Visit test page",
                            command=lambda: controller.show_frame(tst))
        button4.pack(side="top", fill="both", expand=True)



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.om_variable = tk.StringVar(self)
        self.om_variable.set("בחר גיליון")

        self.entry_label = ttk.Button(self, text="title",width = 17, command=self.SetFileComponents)
        self.entry_label.grid(column=2, row=0, sticky=tk.EW, padx=5, pady=5)

        self.dropDown = ttk.OptionMenu(self, self.om_variable, ())
        self.dropDown.grid(column=1, row=0, sticky=tk.S, padx=5, pady=5)
        self.dropDown.config(width=30)

        self.entry = tk.Entry(self)
        self.entry.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5, ipadx=150)

        button3 = tk.Button(self, text="Visit Page 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)

    def SetFileComponents(self):
        print("ok")

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side="top", fill="both", expand=True)

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack(side="top", fill="both", expand=True)

        button3 = tk.Button(self, text="Visit Page 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(side="top", fill="both", expand=True)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 3", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side="top", fill="both", expand=True)

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack(side="top", fill="both", expand=True)

        button3 = tk.Button(self, text="Visit Page 3",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack(side="top", fill="both", expand=True)



class tst(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="test", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        a = buttontest()
        a.pack()


class buttontest(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        button1 = tk.Button(self, text="Back to Home",command=self.pr)
        button1.pack()

    def pr(self):
        print("ok")

class test(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #file read path
        self.filePath = ''
        self.sheetName = ''
        self.selectedSheet = tk.StringVar(self)
        self.om_variable = tk.StringVar(self)
        self.om_variable.set("בחר גיליון")
        self.df = ''

        self.entry_label = ttk.Button(controller, text="title",width = 17, command=self.SetFileComponents)
        self.entry_label.pack()

        self.dropDown = ttk.OptionMenu(controller, self.om_variable, ())
        self.dropDown.pack()
        self.dropDown.config(width=30)

        self.entry = tk.Entry(controller)
        self.entry.pack()

        self.om_variable.trace('w', self.check)

    def SetFileComponents(self):
        """
        get the path from the file dialog and inserts into the entry field
        :return:
        """
        filename = filedialog.askopenfilename(filetypes=(("Excel קבצי", ".xlsx"), ("All files", ".*")))
        if filename !='':
            self.entry.delete(0, END)
            self.entry.insert(tk.END, filename)
            self.filePath = self.entry.get()
        '''        
        read the excel and set the data frame and the sheet list of the excel
        if an error occurred reset the option menu and clear the sheet list
        '''

        try:
            self.dframe = pd.ExcelFile(self.filePath)
            self.sheetList = self.dframe.sheet_names
            self._reset_option_menu(self.sheetList, 0)
        except:
            self._reset_option_menu(['בחר גיליון'], 0)

    def check(self,*args):
        try:
            self.sheetName = self.om_variable.get()
            self.df = pd.read_excel(self.filePath, sheet_name=self.sheetName)
        except:
            pass

    def _reset_option_menu(self, options, index=None):
        '''reset the values in the option menu

        if index is given, set the value of the menu to
        the option at the given index
        '''
        menu = self.dropDown["menu"]
        menu.delete(0, "end")
        for string in options:
            menu.add_command(label=string,
                             command=lambda value=string:
                                  self.om_variable.set(value))
        if index is not None:
            self.om_variable.set(options[index])


app = SeaofBTCapp()
app.mainloop()