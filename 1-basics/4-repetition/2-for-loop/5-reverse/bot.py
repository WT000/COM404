# Asking the user what they see
print("What phrase do you see?")
originalphrase = input()

# Preparing to reverse the phrase (done so the printed message itself isnt looped)
print("Reversing... \nThe phrase is: ", end="")

# Reverse loop
for position in range(len(originalphrase) - 1, -1, -1):
    print(originalphrase[position], end="")