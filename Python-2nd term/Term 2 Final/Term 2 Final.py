##Jared M.
##1/2/2019
##Term 2 Final

import sys

def open_file(file_name,mode):
    """Open File."""
    try:
        file=open(file_name,mode)
    except IOError as e:
        print("unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return file

def next_line(the_file):
    try:
        line = the_file.readline()
    except:
        print("unable to assign the file line of", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
    else:
        """Return next line from the trivia file, formatted."""
        line = line.replace("/","\n")
        return line

file = open_file("test_file.txt","w")
file.write("this/is a/test")
file.close()
file = open_file("test_file.txt","r")
line = next_line(file)
print(line)
