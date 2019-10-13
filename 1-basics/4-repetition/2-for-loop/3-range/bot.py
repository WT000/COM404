# Asks the user what level of brightness is needed
print("What level of brightness is required?")
brightness = int(input())

# Brightness loop
for count in range (2, brightness+1, 2):
    print("Beep's brightness level: " + "*" * count)
    print("Bop's brightness level: " + "*" * count)

# Completed adjustment!
print("Adjustments complete!")