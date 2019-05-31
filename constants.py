#This is a file that holds the constants for the CMDB Project

#Multi-line vars
TEXT = ["Hostname: ", "Last Known Location: ", "IPv4: ", "IPv6: ", "Operating System: ", "Physical/Virtual Machine: ", "Owner: ", "Administrator: ",
        "U of A Tag Number: ", "Make/Model: ", "Processor: ", "RAM (GB): ", "Storage Space (GB): ", "GPU: ", "Serial Number: ", 
        "Status: ", "Rack Number: ", "SRIT Access: ", "Power Up: ", "Support Team: ", "Host ID: ", "Department: ", "Comments: "]
FUNCT = {
    "SWAP_WINDOW": 1,
    "EXIT": 2,
    "LOOKUP": 3,
    "SELECTED_CLICKED": 4,
    "EDIT_CLICKED": 5,
    "CHANGE_CLICKED": 6,
    "EDIT_FILE": 7,
    "NEW_ENTRY_CLICKED": 8,
    "DELETE_FILE": 9,
    "APPEND_FILE": 10,
    "GOTO_HELP": 11
}

#Single line vars
FILE_NAME = "machines.csv"
#Window info
WINDOW_SIZE = "800x600"
LARGE_TEXT = 32
PADDING = 5

EXIT = "Exit"
OKAY = "Confirm"
SAVE = "Save"

LOOKUP_TITLE = "Search for a Machine"
LOOKUP_LABEL = "Input search features:"
LOOKUP_BUTTON = "Look Up"
NO_HOSTNAME = "<No Hostname>"

EDIT_BUTTON = "Edit"
NEW_ENTRY_BUTTON = "Create New Entry"
EDIT_BUTTON_INDEX = len(TEXT)
APPEND_BUTTON_INDEX = len(TEXT) + 1
DELETE_BUTTON = "Delete Entry"

MAIN_TITLE = "Science Machines"
EDIT_TITLE = "Editing a Machine's Information"

HELP_TITLE = "Help"

HELP_BUTTON = "?"
MAIN_HELP = "MAIN_HELP"
EDIT_HELP = "EDIT_HELP"
LOOKUP_HELP = "LOOKUP_HELP"

#File change messages
SUCCESS = "Success"
EDIT_MESSAGE = " has been edited.\nmachines.csv successfully updated."
APPEND_MESSAGE = " has been added.\nmachines.csv successfully updated."
DELETE_MESSAGE = " has been removed.\nmachines.csv successfully updated."
#Error messages
ERROR = "Error"
coding_error = "\nCoding error: Please report this to rodj@ualberta.ca"

BUTTON_ERROR = "An out-of-bounds error occured when creating a Button." + coding_error
BUTTON_END_ERROR = "A invalid function error occured when creating a Button." + coding_error
TEXTBOX_ERROR = "An out-of-bounds error occured when creating a TextBox." + coding_error
LISTBOX_ERROR = "An out-of-bounds error occured when creating a ListBox." + coding_error
LABEL_ERROR = "An out-of-bounds error occured when creating a Label." + coding_error

SWAP_ERROR = "An error occurred when swapping to window_help." + coding_error