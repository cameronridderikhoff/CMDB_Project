#This is a file that holds the constants for the CMDB Project

#Multi-line vars
TEXT = ["Hostname: ", "Last Known Location: ", "IPv4: ", "IPv6: ", "Operating System: ", "Physical/Virtual Machine: ", "Owner: ", "Administrator: ",
        "U of A Tag Number: ", "Make/Model: ", "Processor: ", "RAM (GB): ", "Storage Space (GB): ", "GPU: ", "Serial Number: ", 
        "Status: ", "Rack Number: ", "SRIT Access: ", "Power Up: ", "Support Team: ", "Department: ", "Comments: "]
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
FILE_NAME = "machines.db"
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

HELP_BUTTON = "Help"
LOOKUP_HELP = "Input a keyword for the computer you wish to look up,\nand then click the \"Lookup\" button to fetch the information.\nYou can also click the \"Create New Entry\" button to create a blank entry and append it to the file.\nPress the \"Exit\" button at any time to quit the program."
MAIN_HELP = "Click the \"Edit\" button beside each field you want to change,\nand click the \"Save\" button when you are satisfied with the entry."
EDIT_HELP = "Input the correct format for the field you are editing, please try to fill in as many entries as possible:\n"
EDIT_HELP_LIST = [
"Hostname: Must be a string, the hostname can be found in the computer\'s settings.\nEg. \"bellis\" (bellis.cs)", 
"Last Known Location: Must be a string, this is the building and room the computer resides in.\nEg. Chem W3-15 (Chemistry West, floor 3, room 315)", 
"IPv4: Must be in the correct format, four groups of three decimal digits.\nEg. XXX.XXX.XXX.XXX, where each \"X\" is a digit from 0-9", 
"IPv6: Must be in the correct format, eight groups of four hexadecimal digits.\nAny group of four zeros may be excluded\nEg. XXXX:XXXX:XXXX:XXXX::::, where each \"X\" is a digit from 0-9 or a character from A-F,\nand where two adjesent colons indicate a grouping of four zeros.",
"Operating System: Must be a string, this is the operating system and version number that the machine is using. If dual-boot, provide both.\nEg. Dual boot Windows 10 Education and Ubuntu 18.04",
"Physical/Virtual Machine: Must be a string, either \"Physical\" or \"Virtual\",\nindicating whether this machine is a physical device, or exists only as a virtual desktop.\nEg. Virtual",
"Owner: Must be a string, indicating the name of the professor or group that owns the machine.\nEg. Herb Yang",
"Administrator: Must be a string, indicating the name of the group who owns an administrator account on the PC.\nEg. Vadim Bulitko",
"U of A Tag Number: Must be an integer. This is the six digit number on the label of all U of A machines.\nIt's a white label with \"University of Alberta\" and the U of A Shield on it.\nEg. XXXXXX, where each \"X\" is a digit from 0-9", 
"Make/Model: Must be a string, describing the brand, make, and model of the machine.\nEg. Lenovo Thinkpad T470s",
"Processor: Must be a string, describing the brand and model of the machine's processor.\nEg. Intel i7 4771 @ 3.50GHz",
"RAM (GB): Must be an int, describing the amount of random access memory in gigabytes.\nEg. 8",
"Storage Space (GB): Can be an int or a string, describing the amount of hard drive space in gigabytes.\nIf there are two drives, list them separately.\nEg. 1000HDD, 250SSD",
"GPU: Must be a string, describing the brand and model of the machine's graphics processing unit.\n Eg. NVIDIA GeForce GTX 1080",
"Serial Number: Must be a string, this is the specific serial number for the machine,\ncreated by the manufacturer.\nCan usually be found on the back, or bottom of the machine.\nEg. XXXXXXXXXXXX, where each \"X\" is a digit from 0-9 or a character from A-Z", 
"Status: Must be a string, this is either \"Active\", \"Retired\" or \"Missing\".\nEg. Active",
"Rack Number: Must be an int, can either be the rack number of the server, or \"N/A\" if the machine is not a server.\n Eg. 21", 
"SRIT Access: Must be a yes or no. This means whether or not SRIT has access to the machine.\n Eg. Yes",
"Power Up: Must be an int. This field is the order in which the PC must be booted up in. \nEg 3 (Usually the fileserver must be booted first)",
"Support Team: Must be a string, indicating the person,\nor group who does the sysadmin work on this machine.\nEg. AMII (Is often SRIT)",
"Department: Must be a string. This is the department that the machine is located in. \nEg. Chemistry",
"Comments: Must be a string. Any additional comments and information.\nEg. Was grd123"]


#File change messages
SUCCESS = "Success"
EDIT_MESSAGE = " has been edited.\nmachines.csv successfully updated."
APPEND_MESSAGE = " has been added.\nmachines.csv successfully updated."
DELETE_MESSAGE = " has been removed.\nmachines.csv successfully updated."
#Error messages
ERROR = "Error"
coding_error = "\nCoding error: Please report this to rodj@ualberta.ca"
user_error = "\nUser error: Please try again."

BUTTON_ERROR = "An out-of-bounds error occured when creating a Button." + coding_error
BUTTON_END_ERROR = "A invalid function error occured when creating a Button." + coding_error
TEXTBOX_ERROR = "An out-of-bounds error occured when creating a TextBox." + coding_error
LISTBOX_ERROR = "An out-of-bounds error occured when creating a ListBox." + coding_error
LABEL_ERROR = "An out-of-bounds error occured when creating a Label." + coding_error

SWAP_ERROR = "An error occurred when swapping to window_help." + coding_error

LOOKUP_ERROR = "An error occurred. There is no machine with the search term you are using." + user_error