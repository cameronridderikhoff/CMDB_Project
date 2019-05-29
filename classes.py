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
    def create_button(self, text, command, index, ignore=False, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return

        self.buttons.append("")
        if command == const.FUNCT["SWAP_WINDOW"]: #args[0] must contain a reference to the window we are swapping to
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.swap_window,args[0]))
        elif command == const.FUNCT["EXIT"]:
            self.buttons[index] = tk.Button(self.frame, text=text, command=self.root.destroy)
        elif ignore: #this is taken care of in another class, and is here so as to not give an error
            pass
        else:
            msgbox.showinfo(const.ERROR, const.BUTTON_END_ERROR)
            return

        if ignore: #buttons on window_lookup and window_edit
            self.buttons[index].pack(side=tk.LEFT)
        else:
            self.buttons[index].pack()

class WindowLookup(Window):
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
    
    """
    This function overrides the create_button function in Window, adding special checks for functions specific to LookupWindow
    """
    def create_button(self, text, command, index, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return
            
        if command == const.FUNCT["LOOKUP"]: #the term we are searching for is in self.textboxes[0]
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=self.get_info)
            super().create_button(text,command,index,True,args)
        elif command == const.FUNCT["SELECTED_CLICKED"]: #we clicked the "Okay" button, and want to go to window_main
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.selected_clicked, args[0])) #args[0] must hold window_main
            super().create_button(text,command,index,True,args)
        else:
            super().create_button(text,command,index,False,args)

    """
    This function opens the "machines.csv" file, reads the lines, 
    and adds each line containing what the user requested to the listbox, and list variables
    """
    def get_info(self):
        #clear the previous entries
        self.list = []
        self.listbox.delete(0,END)
        search_term = self.textboxes[0].get()

        text_file = open(const.FILE_NAME, 'r')
        lines = text_file.readlines()
        text_file.close()

        for line in lines:
            if search_term.lower() in line.lower():
                self.list.append(line)
                words = line.split("|")
                if words[0] != "": #If the hostname is not blank
                    self.listbox.insert(END, words[0])
                else: #hostname is blank
                    self.listbox.insert(END, const.NO_HOSTNAME)

    """
    This function is called when the "Okay" button is pressed, and sets up window_main with the selected machine
    Eg.(For the "Hostname" field) "Hostname: " + "grd123"  -> "Hostname: grd123"
    """
    def selected_clicked(self, window_main):
        line = self.list[self.listbox.curselection()[0]]
        words = line.split("|")
        
        for i in range(len(const.TEXT)):
            window_main.str_vars[i].set(const.TEXT[i] + words[i])
        self.swap_window(window_main)


class WindowMain(Window):
    def __init__(self, parent, title):
        self.currently_editing = None
        super().__init__(parent, title)

    """
    This function overrides the create_button function in Window, adding special checks for functions specific to WindowMain
    """
    def create_button(self, text, command, index, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return
            
        if command == const.FUNCT["EDIT_CLICKED"]: #args[0] must have the reference to window_edit
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.edit_clicked, index, args[0]))
            super().create_button(text,command,index,True,args)
        else:
            super().create_button(text,command,index,False,args)
    
    """
    This function is called when one of the "Edit" buttons have been pressed
    it sets the text for the label on window_edit, and then switches to window_edit
    """
    def edit_clicked(self, index, window_edit):
        self.currently_editing = index #the index of the button that we are currently editing
        window_edit.str_vars[0].set(self.str_vars[index].get())
        self.swap_window(window_edit)

class WindowEdit(Window):
    """
    This function overrides the create_button function in Window, adding special checks for functions specific to WindowEdit
    """
    def create_button(self, text, command, index, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return
            
        if command == const.FUNCT["CHANGE_CLICKED"]: #args[0] must have the reference to window_edit
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.change_clicked,args[0]))
            super().create_button(text,command,index,True,args)
        else:
            super().create_button(text,command,index,False,args)

    """
    This function is called when the "Okay" button is clicked on window_edit.
    It changes the label that we are editing on window_main 
    """
    def change_clicked(self, window_main):
        i = window_main.currently_editing
        window_main.str_vars[i].set(const.TEXT[i] + self.textboxes[0].get())
        self.swap_window(window_main)
