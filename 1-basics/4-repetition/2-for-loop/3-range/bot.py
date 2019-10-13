# Asks the user what level of brightness is needed
print("What level of brightness is required?")
brightness = int(input())

# Control variable
brightness_adjustment = 0

# Brightness loop
for count in range (0, brightness, 2):
    brightness_adjustment = brightness_adjustment + 2
    print("Beep's brightness level: " + "*" * brightness_adjustment)
    print("Bop's brightness level: " + "*" * brightness_adjustment)

# Completed adjustment!
print("Adjustments complete!")