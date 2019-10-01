# Asking the user where they should look
print("Where should I look (in the bedroom / bathroom / lab)?")
look = input()

#Bedroom
if (look == "in the bedroom" or "bedroom"):
    print("Where in the bedroom should I look?")
    look_bedroom = input()
    if (look_bedroom == "under the bed"):
        print("Found some shoes but no battery.")
    else:
        print("Found some mess but no battery.")

#Bathroom
elif (look == "in the bathroom" or "bathroom"):
    print("Where in the bathroom should I look?")
    look_bathroom = input()
    if (look_bathroom == "in the bathtub"):
        print("Found a rubber duck but no battery.")
    else:
        print("It is wet but I found no battery.")

#Lab
elif (look == "in the lab" or "lab"):
    print("Where in the lab should I look?")
    look_lab = input()
    if (look_lab == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

#Other
else:
    print("I do not know where that is but I will keep looking.")