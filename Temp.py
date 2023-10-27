# Task5

# Last week you wrote a program that processed a collection of temperature readings
# entered by the user and displayed the maximum, minimum, and mean. Create a
# version of that program that takes the values from the command-line instead. Be
# sure to handle the case where no arguments are provided

import sys

def highestlowest(temps):
    if not temps:
        print("No temperature values specified.")
    else:
        print(f"Lowest Temperature: {min(temps)}°C")
        print(f"Highest Temperature: {max(temps)}°C")


def average(temps):
    if not temps:
        print("No temperature value specified.")
    else:
        avg = sum(temps) / len(temps)
        print(f"Average temperature: {avg}°C")


arguments = sys.argv[1:]  # We omit the first argument, which is the name of the program

temps = [float(temp) for temp in arguments]  # Convert arguments to floats

highestlowest(temps)
average(temps)


# python Test.py 12.5 21.3 23.0 25 26.4 30 34.4 29.1 20.7
