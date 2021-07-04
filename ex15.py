from sys import argv
# argument variables for argv
script, filename = argv

#variable name for the txt file to be opened
txt = open(filename)
#print out file and use the read funtion to read the file
print(f"Here's your file {filename}:")
print(txt.read())
#type file name again
print("Type the filename again:")
file_again = input("> ")
#open function to read file again
txt_again = open(file_again)
#display file contents
print(txt_again.read()) 

print(txt.close())
print(txt_again.close())