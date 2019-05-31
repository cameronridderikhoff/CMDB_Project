#Base Code based off of https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
#and https://www.blog.pythonlibrary.org/2012/07/26/tkinter-how-to-show-hide-a-window/
#Edited and built upon by Cameron Ridderikhoff for SRIT at the University of Alberta
#Last edited May 25, 2019
from functools import partial
import fileinput
import tkinter as tk

from tkinter import END,BOTH, LEFT,RIGHT,TOP,BOTTOM, X,Y
from tkinter import messagebox as msgbox
#my files
import constants as const

class Window(tk.Frame):
    def __init__(self, parent, title):
        self.root = parent
        self.root.geometry(const.WINDOW_SIZE)
        self.root.title(title)
        self.frame = tk.Frame(parent)
        self.frame.pack(fill=BOTH)
        
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
    def create_label(self, text, index, side=TOP, text_size=11):
        #failsafe in case trying to add an out of range widget
        if index > len(self.str_vars):
            msgbox.showinfo(const.ERROR, const.LABEL_ERROR)
            return
        strvar = tk.StringVar()
        strvar.set(text)
        self.str_vars.append(strvar)
        lbl = tk.Label(self.frame, textvar=self.str_vars[index], font=("Arial", text_size))
        lbl.pack(side=side, padx=const.PADDING, pady=const.PADDING)

    """
    This function creates a textbox and adds it to the textbox list
    """
    def create_textbox(self, index, side):
        #failsafe in case trying to add an out of range widget
        if index > len(self.textboxes):
            msgbox.showinfo(const.ERROR, const.TEXTBOX_ERROR)
            return

        self.textboxes.append("")
        self.textboxes[index] = tk.Entry(self.frame)
        self.textboxes[index].pack(side=side, padx=const.PADDING, pady=const.PADDING)

    """
    This function creates a button and adds it to the buttons list
    """
    def create_button(self, text, command, index, side=TOP, ignore=False, args=[]):
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
        self.buttons[index].pack(side=side, padx=const.PADDING, pady=const.PADDING)

class WindowLookup(Window):
    def __init__(self, parent, title):
        self.listbox = None
        self.list = [] #the list that holds the full lines that we pull from the file
        self.swap_back = None
        super().__init__(parent, title)

    """
    This function creates a listbox, and since there can only be one listbox, it sets the listbox variable to be that
    """
    def create_listbox(self, side):
        self.listbox = tk.Listbox(self.frame, selectmode = "SINGLE")
        self.listbox.pack(side=side, padx=const.PADDING, pady=const.PADDING)
    
    """
    This function overrides the create_button function in Window, adding special checks for functions specific to LookupWindow
    """
    def create_button(self, text, command, index, side, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return
            
        if command == const.FUNCT["LOOKUP"]: #the term we are searching for is in self.textboxes[0]
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=self.get_info)
            super().create_button(text,command,index,side,True,args)
        elif command == const.FUNCT["SELECTED_CLICKED"]: #we clicked the "Okay" button, and want to go to window_main
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.selected_clicked, args[0])) #args[0] must hold window_main
            super().create_button(text,command,index,side,True,args)
        elif command == const.FUNCT["NEW_ENTRY_CLICKED"]: #we clicked the "Make new entry" button, and want to go to window_main
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.new_entry_clicked, args[0])) #args[0] must hold window_main
            super().create_button(text,command,index,side,True,args)
        else:
            super().create_button(text,command,index,side,False,args)

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
        window_main.buttons[const.EDIT_BUTTON_INDEX].grid()
        window_main.buttons[const.APPEND_BUTTON_INDEX].grid_remove()
        self.swap_window(window_main)

    """
    This function is called when the "Create New Entry" button is clicked. 
    It clears out all string vars in window_main and swaps to window_main
    """
    def new_entry_clicked(self, window_main):
        for i in range(len(const.TEXT)):
            window_main.str_vars[i].set(const.TEXT[i])
            
        window_main.buttons[const.EDIT_BUTTON_INDEX].grid_remove()
        window_main.buttons[const.APPEND_BUTTON_INDEX].grid()
        self.swap_window(window_main)

class WindowMain(Window):
    def __init__(self, parent, title):
        self.currently_editing = None
        self.frame2 = tk.Frame(parent)
        self.frame2.pack(fill=Y, side = LEFT)
        super().__init__(parent, title)

    """
    This function overrides the create_button function in Window, adding special checks for functions specific to WindowMain
    It also sets up a grid for the two rows, utilizing the second frame that was created
    """
    def create_button(self, text, command, index, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return
        self.buttons.append("")
        if command == const.FUNCT["EDIT_CLICKED"]: #args[0] must have the reference to window_edit
            if index < len(const.TEXT)/2: 
                self.buttons[index] = tk.Button(self.frame2, text=text, command=partial(self.edit_clicked, index, args[0]))
            else:
                self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.edit_clicked, index, args[0]))
        elif command == const.FUNCT["EDIT_FILE"]: #args[0] must contain a reference to window_lookup
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.edit_file,args[0]))
        elif command == const.FUNCT["APPEND_FILE"]: #args[0] must contain a reference to window_lookup
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.append_file,args[0]))
        elif command == const.FUNCT["DELETE_FILE"]: #args[0] must contain a reference to window_lookup
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.delete_from_file,args[0]))
        elif command == const.FUNCT["SWAP_WINDOW"]: #args[0] must contain a reference to the window we are swapping to
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.swap_window,args[0]))
        else:
            msgbox.showinfo(const.ERROR, const.BUTTON_END_ERROR)
            return
        self.buttons[index].grid(row=index, column=1)
    
    """
    This function creates overrides the create_label function in Window so that the labels will be in the correct location,
    by utilizing frame2
    """
    def create_label(self, text, index, text_size=11):
        #failsafe in case trying to add an out of range widget
        if index > len(self.str_vars):
            msgbox.showinfo(const.ERROR, const.LABEL_ERROR)
            return
        strvar = tk.StringVar()
        strvar.set(text)
        self.str_vars.append(strvar)
        if index < len(const.TEXT)/2: 
            lbl = tk.Label(self.frame2, textvar=self.str_vars[index], font=("Arial", text_size))
        else:
            lbl = tk.Label(self.frame, textvar=self.str_vars[index], font=("Arial", text_size))
        lbl.grid(row=index, column=0,padx=const.PADDING, pady=const.PADDING)

    """
    This function is called when one of the "Edit" buttons have been pressed
    it sets the text for the label on window_edit, and then switches to window_edit
    """
    def edit_clicked(self, index, window_edit):
        self.currently_editing = index #the index of the button that we are currently editing
        window_edit.str_vars[0].set(self.str_vars[index].get())
        self.swap_window(window_edit)
    
    """
    This function is called when the Okay button is pressed to confirm any changes
    it then saves the data to the file, and then switches to window_lookup
    This function is called when we select "Edit this Entry" on window_lookup
    """
    def edit_file(self, window_lookup):
        search_term = window_lookup.list[window_lookup.listbox.curselection()[0]] #this is the line 

        print_string = ""
        for str_var in self.str_vars:
            words = str_var.get().split(": ")
            print_string = print_string + words[1] + "|" 
        print_string = print_string[0:-1] #remove the extra "|", since each line shouldn't end with a "|"

        for line in fileinput.FileInput(const.FILE_NAME, inplace=1):
            if line == search_term:
                print(print_string, end='')
            else:
                print(line, end='')
        msgbox.showinfo(const.SUCCESS, window_lookup.listbox.curselection()[0] + const.EDIT_MESSAGE)
        self.swap_window(window_lookup)

    """
    This function is called when the Okay button is pressed to confirm any changes
    it then appends the data to the file, and then switches to window_lookup
    This function is called when we select "Create new Entry" on window_lookup
    """
    def append_file(self, window_lookup):
        print_string = ""
        for str_var in self.str_vars:
            words = str_var.get().split(": ")
            print_string = print_string + words[1] + "|" 
        print_string = print_string[0:-1] #remove the extra "|", since each line shouldn't end with a "|"

        text_file = open(const.FILE_NAME, 'a')
        text_file.write(print_string)
        text_file.close()
        msgbox.showinfo(const.SUCCESS, window_lookup.listbox.curselection()[0] + const.EDIT_MESSAGE)
        self.swap_window(window_lookup)

    """
    This function is called when the Okay button is pressed to confirm any changes
    it then removed the line that we selected, and then switches to window_lookup
    """
    def delete_from_file(self, window_lookup):
        search_term = window_lookup.list[window_lookup.listbox.curselection()[0]] #this is the line 

        for line in fileinput.FileInput(const.FILE_NAME, inplace=1):
            if line == search_term:
                print("", end='')
            else:
                print(line, end='')
        msgbox.showinfo(const.SUCCESS, window_lookup.listbox.curselection()[0] + const.EDIT_MESSAGE)
        self.swap_window(window_lookup)


class WindowEdit(Window):
    """
    This function overrides the create_button function in Window, adding special checks for functions specific to WindowEdit
    """
    def create_button(self, text, command, index, side, args=[]):
        #failsafe in case trying to add an out of range widget
        if index > len(self.buttons):
            msgbox.showinfo(const.ERROR, const.BUTTON_ERROR)
            return
            
        if command == const.FUNCT["CHANGE_CLICKED"]: #args[0] must have the reference to window_edit
            self.buttons.append("")
            self.buttons[index] = tk.Button(self.frame, text=text, command=partial(self.change_clicked,args[0]))
            super().create_button(text,command,index,side,True,args)
        else:
            super().create_button(text,command,index,side,False,args)

    """
    This function is called when the "Okay" button is clicked on window_edit.
    It changes the label that we are editing on window_main 
    """
    def change_clicked(self, window_main):
        i = window_main.currently_editing
        window_main.str_vars[i].set(const.TEXT[i] + self.textboxes[0].get())
        self.swap_window(window_main)
