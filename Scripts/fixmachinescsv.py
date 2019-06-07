import constants as const

old = open("CS machines.csv", 'r')
new = open("machines.csv", 'r')

old_lines = old.readlines()
new_lines = new.readlines()

print_file = open("new_machines.csv", 'w')
print_words = []
for word in const.TEXT:
    print_words.append("")

for i in range(len(old_lines)):
    old_words = old_lines[i].split("|")
    new_words = new_lines[i].split("|")

    print_words[0] = old_words[0]
    print_words[1] = old_words[1]
    print_words[2] = old_words[2]
    print_words[3] = "" #IPv6
    print_words[4] = old_words[3] + " " + old_words[4]
    print_words[5] = old_words[5]
    print_words[6] = old_words[6]
    print_words[7] = old_words[7]
    print_words[8] = old_words[8]
    print_words[9] = new_words[13]
    print_words[10] = new_words[14]
    print_words[11] = new_words[15]
    print_words[12] = new_words[16]
    print_words[13] = "" #only one machine has a gpu description that i can find. line 6 - gtx1080
    print_words[14] = old_words[11]
    print_words[15] = old_words[14]
    print_words[16] = old_words[17]
    print_words[17] = "" #Access
    print_words[18] = old_words[18]
    print_words[19] = old_words[19]
    print_words[20] = "Computer Science"
    print_words[21] = old_words[20]
    
    #print the edited line to the new file
    print_line = ""
    for word in print_words:
        print_line = print_line + word + "|"
    print_line = print_line[0:-2] #remove the extra "|", since each line shouldn't end with a "|"
    print_file.write(print_line)

print_file.close()