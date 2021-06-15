formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your","own text here", "Maybe a poem", "Or a song about fear"))


cow = "{} {} {} "

print(cow.format("missy","fresh","bull"))
print(cow.format(1, 2, 3))
print(cow.format(True, False, False))
print(cow.format(cow, cow, cow))