import sys
from statistics import mean

if len(sys.argv)<=1:    # Check if there is at least one argument
    print("No argument specified.")
else:
    total = 0   #Initially, the total variable is set to 0
    num1 =[]    #We collect the numbers in this list

count = len(sys.argv)
while count > 1:
    count -= 1
    num2 = float(sys.argv[count])
    total += num2
    num1.append(num2)

if num1:        # Check if there are numbers to calculate the average
    avg = mean(num1)
    print("Total is", total)
    print(f"Total is, {avg}")
else: 
    print("No numbers found to calculate average. ")
    



