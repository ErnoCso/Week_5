import sys

if len(sys.argv) > 1:  # Check if command line arguments were provided
    print("Command line arguments provided:")

for arg in sys.argv[1:]:  # Iterate through the command line arguments and print each one
    print(arg)
else:
    print("No command line arguments provided.")
