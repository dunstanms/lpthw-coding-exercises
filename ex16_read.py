from sys import argv

script, filename = argv 

txt = open(filename)

print(f"Here is your {filename}") 
print(txt.read())