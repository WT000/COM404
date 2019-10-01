# Multiple if responses.
print("Towards which direction should I paint? Up, down, left or right?")
direction = input()
if (direction == "up"):
    print("I am painting in the upward direction!")
elif (direction == "down"):
    print("I am painting in the downward direction!")
elif (direction == "left"):
    print("I am painting in the left direction!")
elif (direction == "right"):
    print("I am painting in the right direction!")
else:
    print("That isn't a direction...?")