import sys

if __name__ == "__main":
    num_arguments = len(sys.argv) - 1
    if num_arguments == 0:
        print("No arguments provided.")
    else:
        print(f"Number of arguments provided: {num_arguments}")