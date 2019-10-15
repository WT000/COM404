# Box Function
def word_box(originalword):
    print("*" * (len(originalword) + 2))
    print("*" + originalword + "*")
    print("*" * (len(originalword) + 2))

# Lowercase Function
def lower_case(originalword):
    print(originalword.lower())

# Uppercase Function
def upper_case(originalword):
    print(originalword.upper())

# The two above could also be done with a FOR loop using an ASCII table, go between 32 (plus and minus)

# Mirror Function
def mirror(originalword):
    for position in range(len(originalword) - 1, -1, -1):
        print(originalword[position], end="")

# Repeat Function (going between upper and lower case)
def repeat(originalword):
    print("How many times should it be repeated?")
    repeat_value = int(input())
    for count in range(0, repeat_value, 1):
        print(originalword.lower() + " ", end="")
        print(originalword.upper()+ " ", end="")

# Running Function
def run():
    print("Please enter a word.")
    originalword = input()
    print("What do you want to do with the word? \n1. Display in a Box \n2. Display Lower-case \n3. Display Upper-case \n4. Display Mirrored \n5. Repeat")
    op = int(input())

# Various Function options
    if (op == 1):
        word_box(originalword)

    if (op == 2):
        lower_case(originalword)

    if (op == 3):
        upper_case(originalword)

    if (op == 4):
        mirror(originalword)

    if (op == 5):
        repeat(originalword)

    else:
        print("Please select a number.")

# Function runs on start
run()