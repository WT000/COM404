# Counter.
even_number = 0
odd_number = 0

# First Number
print("Please enter the first whole number.")
first_number = int(input())
if (first_number % 2 == 0):
    even_number += 1
else:
    odd_number += 1

# Second Number
print("Please enter the second whole number.")
second_number = int(input())
if (second_number % 2 == 0):
    even_number += 1
else:
    odd_number += 1

# Third Number
print("Please enter the third whole number.")
third_number = int(input())
if (third_number % 2 == 0):
    even_number += 1
else:
    odd_number += 1

print("There were " + str(even_number) + " even and " + str(odd_number) + " odd numbers.")