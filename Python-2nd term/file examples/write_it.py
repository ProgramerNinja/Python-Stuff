#Jared M.
#12/18/18

print("Creating a text file with the write() method.")
text_file = open("write_it.txt","w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3")
text_file.close()

print("Creating a text file with the writelines() method.")
text_file = open("write_it.txt","w")
lines = ["scores1\n",
         "scores2\n",
         "scores\n"]
text_file.writelines(lines)
text_file.close()
