#tkinters classes
import tkinter
from tkinter import Toplevel
#my files
import classes
import constants as const

"""TODO: clean up all constants that arent in the constants.py file"""

root1 = tkinter.Tk()
root2 = Toplevel(root1)
root3 = Toplevel(root1)
window_lookup = classes.WindowLookup(root1, const.LOOKUP_TITLE)
window_main = classes.WindowMain(root2, const.MAIN_TITLE)
window_edit = classes.WindowEdit(root3, const.EDIT_TITLE)

#window_lookup widgets
window_lookup.create_label(const.LOOKUP_LABEL, 0)
window_lookup.create_textbox(0)
window_lookup.create_button(const.LOOKUP_BUTTON, const.FUNCT["LOOKUP"], 0)
window_lookup.create_button(const.OKAY, const.FUNCT["SELECTED_CLICKED"], 1, args=[window_main])
window_lookup.create_button(const.EXIT, const.FUNCT["EXIT"], 2)
window_lookup.create_listbox()

#window_main widgets
for i in range(len(const.TEXT)):
    window_main.create_label(const.TEXT[i], i)
    window_main.create_button(const.EDIT_BUTTON, const.FUNCT["EDIT_CLICKED"], i, args=[window_edit])

#window_edit widget
window_edit.create_label("", 0)
window_edit.create_textbox(0)
window_edit.create_button(const.OKAY, const.FUNCT["CHANGE_CLICKED"], 0, args=[window_main])
window_edit.create_button(const.EXIT, const.FUNCT["SWAP_WINDOW"], 1, args=[window_main])

window_main.hide()
window_edit.hide()
root1.mainloop()