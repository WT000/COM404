# Asking a user for a number
print("Please enter a number:")
factorial = int(input())

# Calculation
number = 0
finalfactorial = 1

while (number < factorial):
    number = number + 1
    finalfactorial = finalfactorial * number

print("The factorial is", finalfactorial)