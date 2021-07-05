print("Let's practice this thing")
print("You\'d need to know 'bout escapes \\ that do:")
print("\n newlines and \t tabs")

poem = """
\tThe lovely world 
with logic so firmly planted 
and cannot decern \n the needs of love
nor comprehend passion from intuition
and requires an explanantion
\n\t\where is none
"""

print("_________")
print(poem)
print("__________")


five = 10 - 2 + 3 - 6 
print(f"This should be {five}")

def secret_formula(started):
    jelly_beans = started * 500 
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars , crates = secret_formula(start_point)

# another way to format a string 
print("With a starting point of: {}".format(start_point))
#it's just like an f"" string
print(f"we have {beans} beans {jars} jars and {crates} crates  ")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to  a format string
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
