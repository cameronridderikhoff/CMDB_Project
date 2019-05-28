#This is a file that holds the constants for the CMDB Project

#Multi-line vars
TEXT = ["Name: ", "Room: ", "IPv4: ", "IPv6: ", "OS: ", "Physical/Virtual Machine: ", "Owner: ", "Administrator: ",
        "U of A Tag Number: ", "Make/Model: ", "Processor: ", "RAM: ", "Storage: ", "GPU: ", "Serial Number: ", 
        "Status: ", "Rack Number: ", "SRIT Access: ", "Power Up: ", "Support Team: ", "Host ID: ", "Comments: "]
FUNCT = {
    "SWAP_WINDOW": 1,
    "EXIT": 2,
    "LOOKUP": 3
}

#Single line vars
FILE_NAME = "machines.csv"
#Window info
WINDOW_SIZE = "800x600"
LARGE_TEXT = 32
EXIT = "Exit"

LOOKUP_TITLE = "Search for a Machine"
LOOKUP_LABEL = "Input search features:"
LOOKUP_BUTTON = "Look Up"
NO_HOSTNAME = "<No Hostname>"

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