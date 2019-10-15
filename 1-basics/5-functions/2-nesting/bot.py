# Identify function
def identify():
    print("What lies before us?")
    item = input()
    if (item == "A large boulder") or (item == "a large boulder"):
        print("It's time to run!")
    else:
        print("We will be fine.")

# Calling identify function
identify()