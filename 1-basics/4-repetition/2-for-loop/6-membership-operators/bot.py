# Asking the user what they see
print("What phrase do you see?")
originalphrase = input()

# Preparing the reversephrase variable (leaving it blank)
reversephrase = ""

# Preparing to reverse the phrase (done so the printed message itself isnt looped)
print("Reversing... \nThe phrase is: ", end="")

# Adds the originalphrase letters onto reversephrase
for letters in originalphrase:
    reversephrase = letters + reversephrase

# Result
print(reversephrase)