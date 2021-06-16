from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want this, hit CTRL-C (^C)")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now I'm going to write these to the file")

target.write(f" {line1} \n{line2} \n{line3}")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")


txt = open(filename)

print(f"Here is your {filename}")
print(txt.read())

print("And finally, we close it")
target.close()