# Importing a time feature for dramatic effect, importing sys for end.
import time
import sys

# Health
health = 10
maskedhealth = 5

# Meeting the enemy
print("Beep is continuing to walk through the forest, despite seeing the two red eyes.")
time.sleep(3)
print("\"Are you here to die?\"")
decision1 = input("Yes or No: ")
time.sleep(1)

# First decision
if (decision1 == "yes") or (decision1 == "Yes"):
    print("\"Well, I'll make this simple for you.\"")
    time.sleep(1)
    print("The masked man attacks!")
    time.sleep(1)
    print("Beep died.")
    sys.exit()
elif (decision1 == "no") or (decision1 == "No"):
    print("\"No? Then why did you come?\"")
else:
    print("\"Seriously.\"")
    time.sleep(5)
    print("\"You just had to say \"Yes\" or \"No\" to my question.\"")
    time.sleep(10)
    print("\"Did you spell it wrong? Or were you just trying to act cool?")
    input("Spelt wrong(1) \nActing cool(2) \nDon't even try anything else()")
    time.sleep(10)
    print("\"Sorry for wasting 10 seconds of your time, I don't even have a response for that!\"")
    time.sleep(10)
    print("\"There's another 10 seconds. You won't be able to play again if I keep you here. Probably.\"")
    time.sleep(20)
    print("\"Ha. Ha. Ha.\"")
    time.sleep(5)
    print("\"...\"")
    time.sleep(3)
    print("The masked man attacks!")
    time.sleep(1)
    print("Beep died.")
    sys.exit()

# Second core decision
time.sleep(1)
decision2 = input("I'm lost. (enter 1) \nI'm on an adventure! (enter 2): ")
if (decision2 == "1"):
    time.sleep(1)
    print("\"You're lost? Do you know what this place is?\"")
    decision3 = input("Yes or No?: ")
    time.sleep(1)
    if (decision3 == "yes") or (decision3 == "Yes"):
        print("\"Ah, I see. You think you're really clever, huh?")
        time.sleep(1)
        print("The masked man attacks!")
        time.sleep(1)
        print("Beep died.")
        sys.exit()
    elif (decision3 == "no") or (decision3 == "No"):
        print("\"You don't...? How sad...\"")
        time.sleep(1)
        print("The masked man attacks!")
        time.sleep(1)
        print("Beep died.")
        sys.exit()
    else:
        print("\"Answer my questions!\"")
        time.sleep(1)
        print("The masked man attacks!")
        time.sleep(1)
        print("Beep dies!")
        sys.exit()

# Third core Decision
elif (decision2 == "2"):
    time.sleep(1)
    print("\"You're on an adventure...\"")
    time.sleep(1)
    print("\"Then you know what this place is...\"")
    time.sleep(1)
    print("\"I've been waiting so long for a challenge! Thank you for not turning back!\"")
    time.sleep(1)
    print("The masked man goes into a defensive stance! \nBeep has entered combat!\n")
    time.sleep(1)
    decision4 = input("Beep's Health = " + "♥" * health + "\nMasked Man's Health = " + "♦" * maskedhealth + "\nWhat should Beep do? \nFight(1) \nDefend(2) \nFlee(3)")

# Combat begins!
    if (decision4 == "1"):
        print("Beep attacks!")
        time.sleep(1)
        maskedhealth -= 3
        print("Masked Man's health is " + "♦" * maskedhealth + "!")
        time.sleep(1)
        print("Masked Man attacks!")
        time.sleep(1)
        health -= 4
        print("Beep's health is " + "♥" * health + "!")
    elif (decision4 == "2"):
        print("\"Defending, huh? Well, that won't work against me!\"")
        time.sleep(1)
        print("Masked Man attacks! Colossal damage!")
        time.sleep(1)
        health -= 8
        print("Beep's health is " + "♥" * health + "!")
    elif (decision4 == "3"):
        print("\"Running, huh? Well, that won't work against me!\"")
        time.sleep(1)
        print("Masked Man attacks! Colossal damage!")
        time.sleep(1)
        health -= 8
        print("Beep's health is " + "♥" * health + "!")
    else:
        print("\"You're distracted!\"")
        time.sleep(1)
        print("Masked Man attacks! Colossal damage!")
        time.sleep(1)
        health -= 8
        print("Beep's health is " + "♥" * health + "!")

# Second combat
    decision5 = input("\nBeep's Health = " + "♥" * health + "\nMasked Man's Health = " + "♦" * maskedhealth + "\nWhat should Beep do? \nFight(1) \nDefend(2) \nFlee(3)")
    if (decision5 == "1"):
        print("Beep attacks!")
        time.sleep(1)
        maskedhealth -= 3
        if (maskedhealth <= 0):
            print("The Masked Man dies!")
            time.sleep(1)
            sys.exit()
        print("Masked Man's health is " + "♦" * maskedhealth + "!")
        time.sleep(1)
        print("Masked Man attacks!")
        time.sleep(1)
        health -= 4
        if (health <= 0):
            print("Beep dies!")
            time.sleep(1)
            sys.exit()
        print("Beep's health is " + "♥" * health + "!")
    elif (decision5 == "2"):
        print("\"Defending, huh? Well, that won't work against me!\"")
        time.sleep(1)
        print("Masked Man attacks! Colossal damage!")
        time.sleep(1)
        health -= 8
        if (health <= 0):
            print("Beep dies!")
            time.sleep(1)
            sys.exit()
        print("Beep's health is " + "♥" * health + "!")
    elif (decision5 == "3"):
        print("\"Running, huh? Well, that won't work against me!\"")
        time.sleep(1)
        print("Masked Man attacks! Colossal damage!")
        time.sleep(1)
        health -= 8
        if (health <= 0):
            print("Beep dies!")
            time.sleep(1)
            sys.exit()
        print("Beep's health is " + "♥" * health + "!")
    else:
        print("\"You're distracted!\"")
        time.sleep(1)
        print("Masked Man attacks! Colossal damage!")
        time.sleep(1)
        health -= 8
        if (health <= 0):
            print("Beep dies!")
            time.sleep(1)
            sys.exit()
        print("Beep's health is " + "♥" * health + "!")

# Avoiding the question. Seriously?
else:
    print("\"Oh, hah hah hah, very funny. You know, I can see those numbers too you know! Answer my questions!\"")
    time.sleep(2)
    print("The masked man attacks!")
    time.sleep(1)
    print("You died.")
    sys.exit()