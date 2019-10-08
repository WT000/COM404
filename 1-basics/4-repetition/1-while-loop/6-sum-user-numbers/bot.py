# Numbers to sum up
print("How many numbers should I sum up?")
max_number = int(input())

# Counter
number = 0
add_number = 0

# Calculation
while (number < max_number):
    print("Please enter number", number, "of", max_number)
    add_number = int(input()) + add_number
    number = number + 1

print("The answer is ", add_number, ".")