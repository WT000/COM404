# Finding an even or odd number using if.
print("Please enter a whole number")
number = int(input())

# Calculating if the number is even or odd.
if (number % 2 == 0):
    print("The number \"" + str(number) + "\" is an even number.")
else:
    print("The number \"" + str(number) + "\" is an odd number.")