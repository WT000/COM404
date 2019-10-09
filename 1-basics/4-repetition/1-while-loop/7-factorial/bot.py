# Asking a user for a number
print("Please enter a number:")
factorial = int(input())

# Calculation
loop = 0
finalfactorial = 1

while (loop < factorial):
    loop = loop + 1
    finalfactorial = finalfactorial * loop

print("The factorial is", finalfactorial)
