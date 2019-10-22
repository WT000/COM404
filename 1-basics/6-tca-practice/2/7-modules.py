# Line under word function
def under(originalword):
    print(originalword + "*")
    print("*" * len(originalword))

# Line over word function
def over(originalword):
    print("*" * len(originalword))
    print(originalword)

# Line under and over word function
def both(originalword):
    print("*" * len(originalword))
    print(originalword)
    print("*" * len(originalword))

# Word grid function
def grid(originalword):
    print("What grid size do you want?")
    gridsize = int(input())

    # Grid loop
    for count in range(0, gridsize, 1):
        for count in range(0, gridsize, 1):
            print(originalword, end="" + " ")
        print()

# Running function
def run():
    print("Please enter a word")
    originalword = input()
    print("Please choose one of the options: \n1. Under \n2. Over \n3. Both \n4. Grid")
    chosen_option = input()

    # Decides which function to run
    if (chosen_option == "Under"):
        under(originalword)
    elif (chosen_option == "Over"):
        over(originalword)
    elif (chosen_option == "Both"):
        both(originalword)
    elif (chosen_option == "Grid"):
        grid(originalword)
    else:
        print("You didn't pick an option. Please type the word.")

# Starts the program
run()