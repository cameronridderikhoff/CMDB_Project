#tkinters classes
import tkinter
from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Listbox
from tkinter import Toplevel

#my classes
from classes import Window

root1 = tkinter.Tk()
root2 = Toplevel(root1)
root3 = Toplevel(root1)
window_lookup = Window(master=root1)
window_main = Window(master=root2)
window_edit = Window(master=root3)



root1.mainloop()