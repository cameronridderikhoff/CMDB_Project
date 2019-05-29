#This is a file that holds the constants for the CMDB Project

#Multi-line vars
TEXT = ["Hostname: ", "Last Known Location: ", "IPv4: ", "IPv6: ", "Operating System: ", "Physical/Virtual Machine: ", "Owner: ", "Administrator: ",
        "U of A Tag Number: ", "Make/Model: ", "Processor: ", "RAM: ", "Storage: ", "GPU: ", "Serial Number: ", 
        "Status: ", "Rack Number: ", "SRIT Access: ", "Power Up: ", "Support Team: ", "Host ID: ", "Department: ", "Comments: "]
FUNCT = {
    "SWAP_WINDOW": 1,
    "EXIT": 2,
    "LOOKUP": 3,
    "SELECTED_CLICKED": 4,
    "EDIT_CLICKED": 5,
    "CHANGE_CLICKED": 6
}

#Single line vars
FILE_NAME = "machines.csv"
#Window info
WINDOW_SIZE = "800x600"
LARGE_TEXT = 32
SPACING = 20

EXIT = "Exit"
OKAY = "Okay"

LOOKUP_TITLE = "Search for a Machine"
LOOKUP_LABEL = "Input search features:"
LOOKUP_BUTTON = "Look Up"
NO_HOSTNAME = "<No Hostname>"

EDIT_BUTTON = "Edit"

MAIN_TITLE = "Science Machines"
EDIT_TITLE = "Editing a Machine's Information"

#Error messages
ERROR = "Error"
coding_error = "\nCoding error: Please report this to rodj@ualberta.ca"

BUTTON_ERROR = "An out-of-bounds error occured when creating a Button." + coding_error
BUTTON_END_ERROR = "A invalid function error occured when creating a Button." + coding_error
TEXTBOX_ERROR = "An out-of-bounds error occured when creating a TextBox." + coding_error
LISTBOX_ERROR = "An out-of-bounds error occured when creating a ListBox." + coding_error
LABEL_ERROR = "An out-of-bounds error occured when creating a Label." + coding_error