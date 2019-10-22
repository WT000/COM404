# Asking the user how many zones must be crossed
print("How many zones must I cross?")

# Zones to cross
zones = int(input())

# For loop countdown
print("Crossing zones...")
for countdown in range(zones, 0, -1):
    print("...crosed zone", countdown)

# Countdown complete
print("Crossed all zones. Jumanji!")