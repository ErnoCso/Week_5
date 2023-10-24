import sys

if __name__ == "__main":
    arguments = sys.argv[1:]  # We omit the first argument, which is the name of the program

    if not arguments:
        print("There are no command line arguments.")
    else:
        short_argument = min(arguments, key=len)
        print("The shortest argument is:", short_argument)
		
#python shortest_argu.py argument1 argument2 argument3 