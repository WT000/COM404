# Display ladder function
def display_ladder(steps):
    while (0 < steps):
        steps = steps - 1
        print("| | \n***")
    print("| |")

# Display ladder creation function
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

# Calling the ladder creation function
create_ladder()