#Base Code based off of https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
#and https://www.blog.pythonlibrary.org/2012/07/26/tkinter-how-to-show-hide-a-window/
#Edited and built upon by Cameron Ridderikhoff for SRIT at the University of Alberta
#Last edited May 25, 2019
from functools import partial
import tkinter as tk

from tkinter import END, font
from tkinter import messagebox as msgbox
#my files
import constants as const

class Window(tk.Frame):
    def __init__(self, parent, title):
        self.root = parent
        self.root.geometry(const.WINDOW_SIZE)
        self.root.title(title)
        self.frame = tk.Frame(parent)
        self.frame.pack()
        
        self.str_vars = []
        self.buttons = [] 
        self.textboxes = []

    def hide(self):
        self.root.withdraw()
    
    def show(self):
        self.root.update()
        self.root.deiconify()
    """
    This function hides the window that it's called on, and shows the other window
    """
    def swap_window(self, other):
        self.hide()
        other.show()

    """
    This function creates a label with stringvariable linked to text "text"
    """
    def create_label(self, text, index, text_size=11):
        #failsafe in case trying to add an out of range widget
        if index > len(self.str_vars):
            msgbox.showinfo(const.ERROR, const.LABEL_ERROR)
            return
        strvar = tk.StringVar()
        strvar.set(text)
        self.str_vars.append(strvar)
        lbl = tk.Label(self.frame, textvar=self.str_vars[index], font=("Arial", text_size))
        lbl.pack()

    """
    This function creates a textbox and adds it to the textbox list
    """
    def create_textbox(self, index):
        #failsafe in case trying to add an out of range widget
        if index > len(self.textboxes):
            msgbox.showinfo(const.ERROR, const.TEXTBOX_ERROR)
            return

        self.textboxes.append("")
        self.textboxes[index] = tk.Entry(self.frame)
        self.textboxes[index].pack()

    """
    This function creates a button and adds it to the buttons list
    """
    def create_button(self, text, command, index, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return

        self.buttons.append("")
        if command == const.FUNCT["SWAP_WINDOW"]: #there must be at least one argument in args
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.swap_window,args[0]))
        elif command == const.FUNCT["EXIT"]:
            self.buttons[index] = tk.Button(self.frame, text=text, command=self.root.destroy)
        else:
            if command == const.FUNCT["LOOKUP"]:
                pass #this is taken care of in another class, and is here so as to not give an error
            else:
                msgbox.showinfo(const.ERROR, const.BUTTON_END_ERROR)
        self.buttons[index].pack()

class LookupWindow(Window):
    def __init__(self, parent, title):
        self.listbox = None
        self.list = [] #the list that holds the full lines that we pull from the file
        self.swap_back = None
        super().__init__(parent, title)

    """
    This function creates a listbox, and since there can only be one listbox, it sets the listbox variable to be that
    """
    def create_listbox(self):
        self.listbox = tk.Listbox(self.frame, selectmode = "SINGLE")
        self.listbox.pack()
    

    def create_button(self, text, command, index, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return
            
        if command == const.FUNCT["LOOKUP"]: #args[0] is the term we are searching for
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.get_info))

        super().create_button(text,command,index,args)

    def get_info(self):
        #clear the previous entries
        self.list = []
        self.listbox.delete(0,END)
        search_term = self.textboxes[0].get()

        lines = open(const.FILE_NAME, 'r').readlines()

        for line in lines:
            if search_term.lower() in line.lower():
                self.list.append(line)
                words = line.split("|")
                if words[0] != "": #If the hostname is not blank
                    self.listbox.insert(END, words[0])
                else: #hostname is blank
                    self.listbox.insert(END, const.NO_HOSTNAME)


        
    """
    This function may not be nessesary
    """
   # def swap_window(self, other):
   #    self.swap_back = other