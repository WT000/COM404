# How many rows? (repeat value)
print("How many rows should I have?")
rows = int(input())

# How many colums? (amount)
print("\nHow many colums should I have?")
colums = int(input())
print("\nHere I go: \n")

# Face loop
for count in range (0, rows, 1):
    for count in range (0, colums, 1):
        print(":-)", end="")
    print()

# Completed
print("\nDone!")