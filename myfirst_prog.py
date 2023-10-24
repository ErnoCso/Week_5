number = input("Enter a number: ") #The user specifies the value of namber variable

number = int(number)	#Defines the "number" value type and accepts only integers.

print("The numbered entered was", number) # The text entered in quotation marks appears on
										# the display together with the number entered by the user
if (number % 10) == 0:
	print("This number is divisible by 10")

if (number % 2) == 0:	#Check whether the entered number can be divided by two without a remainder
						# if there is no remainder, it is an even number
	print("That is an even number") #If the number is even, the text will appear on the display

else:

	print("That is an odd number")#If the number is odd, it displays the text on the display
