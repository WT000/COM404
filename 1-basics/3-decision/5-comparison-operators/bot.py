# Asking the user for two numbers.
print("Please enter the first number.")
first_number = int(input())
print("Please enter the second number.")
second_number = int(input())

# Calculating which number is the smallest
if (first_number < second_number):
    print("The first number is the smallest!")
elif (first_number > second_number):
    print("The second number is the smallest!")
else:
    print("Both numbers are equal!")