from sys import argv 
script, first, second, third, = argv

first = input("enter name")
second = input("surname")
third = input("age")


print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print(f"Your name is {first} {second} and you are {third} years old")