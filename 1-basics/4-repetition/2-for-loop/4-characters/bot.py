# Asking what markings the user sees
print("What strange markings do you see?")
markings = input()

# Loop
for position in range (0, len(markings), 1):
    print("index " + str(position) + ": " + markings[position])

# Finished loop
print("Done!")