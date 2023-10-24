import sys

def highestLowest(temperatures):
    if not temperatures:
        print("No temperature values specified.")
    else:
        print(f"Lowest Temperature: {min(temperatures)}°C")
        print(f"Highest Temperature: {max(temperatures)}°C")

def average(temperatures):
    if not temperatures:
        print("No temperature value specified.")
    else:
        avg = sum(temperatures) / len(temperatures)
        print(f"Average temperature: {avg}°C")

if __name__ == "__main":
    arguments = sys.argv[1:]  # We omit the first argument, which is the name of the program

    temperatures = [int(temp) for temp in arguments]  # Convert arguments to integers

    highestLowest(temperatures)
    average(temperatures)