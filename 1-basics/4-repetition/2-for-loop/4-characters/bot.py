# Asking what markings the user sees
print("What strange markings do you see?")
markings = input()

# Control variable
loopcount = 0

# Loop
for position in range (0, len(markings), 1):
    print("index " + str(loopcount) + ": " + markings[position])
    loopcount = loopcount + 1

# Finished loop
print("Done!")