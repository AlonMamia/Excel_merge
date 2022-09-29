# from important.FileBrowseComponent import *
from tkinter import filedialog

from funcEX import *
import tkinter as tk


class FileBrowserContainer(tk.Frame):
    def __init__(self,title):
        super(FileBrowserContainer, self).__init__()
        #file read path
        self.filePath = ''
        self.sheetName = ''
        self.selectedSheet = StringVar(self)
        self.om_variable = tk.StringVar(self)
        self.om_variable.set("בחר גיליון")
        self.df = ''
        self.sv = StringVar()


        self.entry_label = ttk.Button(self, text=title,width = 17, command=lambda: self.SetFileComponents(True))
        self.entry_label.grid(column=2, row=0, sticky=tk.EW, padx=5, pady=5)
        self.entry_label.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)


        self.dropDown = ttk.OptionMenu(self, self.om_variable, ())
        self.dropDown.grid(column=1, row=0, sticky=tk.S, padx=5, pady=5)
        self.dropDown.config(width=30)

        self.entry = tk.Entry(self, textvariable=self.sv, exportselection=0)
        self.entry.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5, ipadx=150)

        self.om_variable.trace('w', self.check)

        """
        set file path to entry identify its entry by sending false value to SetFileComponents
        """
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.SetFileComponents(False))


    def SetFileComponents(self,bool):
        """
        get the path from the file dialog and inserts into the entry field
        :return:
        """
        if bool:
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

class hi_hello():
    def __init__(self, parent, frame2):
        there = Button(frame2,text="hi~",command=self.hello)
        there.pack()

    def hello(self):
        print("hello ~ !")