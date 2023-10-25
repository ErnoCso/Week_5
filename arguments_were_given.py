# Task 2

# Write a program that, when run from the command line, reports how many
# arguments were provided. (Remember that the program name itself is not an
# argument)

import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1
    if num_arguments == 0:
        print("No arguments provided.")
    else:
        print(f"Number of arguments provided: {num_arguments}")

# python arguments_were_given.py argument1 arguments2 argument3
