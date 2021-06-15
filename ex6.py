#first variable
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"

do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
#f-strings in print statements
print(f"I said : {x}")
print(f"I also said : '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#use .format string to add hilariuos variable to statement
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side"

#combine the two strings into one
print(w + e)