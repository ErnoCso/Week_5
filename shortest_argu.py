# Task 3

# Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.

import sys

argu = sys.argv[1:]  # We omit the first argument, which is the name of the program

if not argu:
    print("There are no command line arguments.")
else:
    short_argu = len(min(argu, key=len))
    shortests = []
    for f in argu:
        if len(f) == short_argu:
            shortests.append(f)
    print(f"The shortest argument is:")
    print(*shortests, sep=", ")

# python shortest_argu.py argument1 argument2 argument3
