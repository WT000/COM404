# United league function
def is_league_united(first_hero, second_hero):
    if (first_hero == "Superman") and (second_hero == "Wonder Woman"):
        league_united = True
    else:
        league_united = False
    return league_united

# Plan decision function
def decide_plan(first_hero, second_hero):
    league_united = is_league_united(first_hero, second_hero)
    if (league_united == True):
        print("Time to save the world!")
    else:
        print("We must unite the league!")

# Run function (runs on start)
def run():
    print("Who is the first hero?")
    first_hero = input()
    print("Who is the second hero?")
    second_hero = input()
    print("Please enter \"league\" or \"plan\"")
    user_decision = input()

    # Decides which function to run
    if (user_decision == "league"):
        league_united = is_league_united(first_hero, second_hero)
        print(str(league_united))

    elif (user_decision == "plan"):
        decide_plan(first_hero, second_hero)

    else:
        print("Invalid command. Please try again.")

# Run the program
run()