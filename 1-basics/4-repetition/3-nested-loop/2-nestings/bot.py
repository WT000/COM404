# Getting the entire sequence
print("Please enter a sequence")
usersequence = input()

# Getting the marker
print("Please enter a character for the marker")
marker = input()

usertotal = len(usersequence)
markertotal = 0
distance = 0

for position in range (0, usertotal, 1):
    currentcharacter = usersequence[position]
    if (currentcharacter == marker):
        markertotal = markertotal + 1
    elif (markertotal == 1):
        distance = distance + 1

print("The distance between the markers is: " + str(distance))