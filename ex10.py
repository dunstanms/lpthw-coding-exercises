tabby_cat = "{}"
persian_cat = "{}"
backslash_cat = "{}"

fat_cat = '''
I'll do a list:
\v* Cat food
\v* Fishies
\v* Catnip\n\v* Grass
'''

print(tabby_cat.format("\tI'm tabbed in"))
print(persian_cat.format("I'm split\non a line."))
print(backslash_cat.format("I'm \\ a \\ cat"))
print(fat_cat)

