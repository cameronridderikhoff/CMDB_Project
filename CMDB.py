#tkinters classes
import tkinter
from tkinter import Toplevel
from tkinter import LEFT,RIGHT,TOP,BOTTOM #directions to position the widgets
#my files
import classes
import constants as const

"""TODO: clean up all constants that arent in the constants.py file"""

root1 = tkinter.Tk()
root2 = Toplevel(root1)
root3 = Toplevel(root1)
root4 = Toplevel(root1)
window_lookup = classes.WindowLookup(root1, const.LOOKUP_TITLE)
window_main = classes.WindowMain(root2, const.MAIN_TITLE)
window_edit = classes.WindowEdit(root3, const.EDIT_TITLE)
window_help = classes.WindowHelp(root4, const.HELP_TITLE)

#window_lookup widgets
window_lookup.create_label(const.LOOKUP_LABEL, 0, TOP)
window_lookup.create_textbox(0, TOP)
window_lookup.create_button(const.LOOKUP_BUTTON, const.FUNCT["LOOKUP"], 0, TOP)
window_lookup.create_button(const.NEW_ENTRY_BUTTON, const.FUNCT["NEW_ENTRY_CLICKED"], 1, TOP, args=[window_main])
window_lookup.create_button(const.OKAY, const.FUNCT["SELECTED_CLICKED"], 2, RIGHT, args=[window_main])
window_lookup.create_listbox(RIGHT)
window_lookup.create_button(const.EXIT, const.FUNCT["EXIT"], 3, BOTTOM)
window_lookup.create_button(const.HELP_BUTTON, const.FUNCT["GOTO_HELP"], 4, TOP, args=[window_help])

#window_main widgets
for i in range(len(const.TEXT)):
    if i < len(const.TEXT)/2:
        window_main.create_label(const.TEXT[i], i)
        window_main.create_button(const.EDIT_BUTTON, const.FUNCT["EDIT_CLICKED"], i, args=[window_edit])
    else:
        window_main.create_label(const.TEXT[i], i)
        window_main.create_button(const.EDIT_BUTTON, const.FUNCT["EDIT_CLICKED"], i, args=[window_edit])

window_main.create_button(const.SAVE, const.FUNCT["EDIT_FILE"], const.EDIT_BUTTON_INDEX, args=[window_lookup])
window_main.create_button(const.SAVE, const.FUNCT["APPEND_FILE"], const.APPEND_BUTTON_INDEX, args=[window_lookup])
window_main.create_button(const.DELETE_BUTTON, const.FUNCT["DELETE_FILE"], len(const.TEXT)+2, args=[window_lookup])
window_main.create_button(const.EXIT, const.FUNCT["SWAP_WINDOW"], len(const.TEXT)+3, args=[window_lookup])
window_main.create_button(const.HELP_BUTTON, const.FUNCT["GOTO_HELP"], len(const.TEXT) + 4, args=[window_help])

#window_edit widgets
window_edit.create_label("", 0, TOP)
window_edit.create_textbox(0, TOP)
window_edit.create_button(const.OKAY, const.FUNCT["CHANGE_CLICKED"], 0, TOP, args=[window_main])
window_edit.create_button(const.EXIT, const.FUNCT["SWAP_WINDOW"], 1, TOP, args=[window_main])
window_edit.create_button(const.HELP_BUTTON, const.FUNCT["GOTO_HELP"], 2, TOP, args=[window_help])

#window_help widgets
window_help.create_label("", 0, TOP)
window_help.create_button(const.EXIT, const.FUNCT["SWAP_WINDOW"], 0, TOP, args=[window_help])

window_main.hide()
window_edit.hide()
window_help.hide()
root1.mainloop()