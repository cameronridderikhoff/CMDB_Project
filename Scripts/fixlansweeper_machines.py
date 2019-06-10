import constants as const

read_file = open("lansweeper_machines.csv", 'r')

read_lines = read_file.readlines()
read_file.close()
print_file = open("lansweeper_fixed.csv", 'w')
print_words = []
for word in const.TEXT:
    print_words.append("")

for i in range(len(read_lines)):
    read_words = read_lines[i].split("|")
    
    print_words[0] = read_words[0].split(".")[0] #the first portion of this will be the hostname, or the best guess at a hostname that we have since the format is: hostname.faculty.ualberta.ca
    print_words[1] = read_words[7] #location
    print_words[2] = read_words[1] #Ipv4
    print_words[3] = "" #IPv6
    print_words[4] = read_words[2] #OS (type in lansweeper)
    print_words[5] = "Physical"#phys/virt
    print_words[6] = read_words[3] #owner (domain in lansweeper)
    print_words[7] = "" #admin
    print_words[8] = "" #tag number
    print_words[9] = read_words[5] + " " + read_words[6] #make/model (manufacturer and model in lansweeper)
    print_words[10] = "" #processor
    print_words[11] = "" #RAM
    print_words[12] = "" #Storage space
    print_words[13] = "" #gpu
    print_words[14] = "" #serial #
    print_words[15] = "Active" #Status
    print_words[16] = "" #rack num
    print_words[17] = "" #Access
    print_words[18] = "" #power up
    print_words[19] = "" #support team
    print_words[20] = read_words[8].split(" - ")[1] #department
    print_words[21] = read_words[4] #comments (description in lansweeper)
    
    #print the edited line to the new file
    print_line = ""
    for word in print_words:
        print_line = print_line + word + "|"
    print_line = print_line[0:-2] #remove the extra "|", since each line shouldn't end with a "|"
    print_file.write(print_line + "\n")

print_file.close()