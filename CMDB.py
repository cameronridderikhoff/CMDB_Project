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
window_lookup = classes.LookupWindow(root1, const.LOOKUP_TITLE)
window_main = classes.Window(root2, const.MAIN_TITLE)
window_edit = classes.Window(root3, const.EDIT_TITLE)

#window_lookup widgets
window_lookup.create_label(const.LOOKUP_LABEL, 0)
window_lookup.create_textbox(0)
window_lookup.create_button(const.LOOKUP_BUTTON, const.FUNCT["LOOKUP"], 0)
window_lookup.create_button(const.OKAY, const.FUNCT["SELECTED_CLICKED"], 1)
window_lookup.create_button(const.EXIT, const.FUNCT["EXIT"], 2)
window_lookup.create_listbox()

window_main.hide()
window_edit.hide()
root1.mainloop()