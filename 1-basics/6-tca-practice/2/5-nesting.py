# Health Counter
health = 100

# Starting message
print("Your health is 100%. Escape is in progress...")

# For loop (total of 5 times)
for count in range(0, 5, 1):
    print("...Oh dear, who is that?")
    seen_person = input()
    if (seen_person == "Smiler's Bot"):
        health -= 20
        print("Time to jam out of here!\n")
    elif (seen_person == "Hacker"):
        health += 20
        print("Yay! Better follow this one!\n")
    else:
        print("Phew, just another emoji!\n")

# Finished loop
print("Escaped! Health is [" + str(health) + "%]")