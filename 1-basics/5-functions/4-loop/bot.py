# Crossing the bridge function
def cross_bridge(steps):
    maxsteps = 0
    while (0 < steps):
        print("Crossed step.")
        steps = steps - 1
        maxsteps = maxsteps + 1
    if (maxsteps > 5):
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

# Calling the crossing bridge function
cross_bridge(3)
cross_bridge(6)