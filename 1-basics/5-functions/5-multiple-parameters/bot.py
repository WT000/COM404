# Climbing ladder parameter
def climb_ladder(done, togo):
    if (togo > done):
        print("Still some way to go!")
    else:
        print("We made it!")

# Calling the climb ladder parameter
climb_ladder(2, 5)
climb_ladder(5, 5)