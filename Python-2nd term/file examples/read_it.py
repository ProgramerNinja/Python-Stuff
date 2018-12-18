#Jared M.
#12/18/18

print("Opening sand closing the file")
text_file = open("read_it.txt","r")
print(text_file)
text_file.close()

print("\nReading charecters from the file")
text_file = open("read_it.txt")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nReading the eantire file at once.")
text_file = open("read_it.txt","r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("reading characters from a line.")
text_file = open("read_it.txt","r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nReading one line at a time.")
text_file = open("read_it.txt","r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()


print("\nReading the entire file into a list.")
text_file = open("read_it.txt","r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()
