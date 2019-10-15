# Sum weights function
def sum_weights(beep_weight, bop_weight):
    totalsum = beep_weight + bop_weight
    return totalsum

# Average weight function
def calc_avg_weight(beep_weight, bop_weight):
    average = beep_weight + bop_weight / 2
    return average

# Run function
def run():
    print("What is the weight of Beep?")
    beep_weight = int(input())
    print("What is the weight of Bop?")
    bop_weight = int(input())
    print("What would you like to calculate? Sum or Average?")
    calculation = input()

    if (calculation == "Sum") or (calculation == "sum"):
        totalsum = sum_weights(beep_weight, bop_weight)
        print("The sum of Beep and Bop's weight is " + str(totalsum))

    elif (calculation == "Average") or (calculation == "average"):
        average = calc_avg_weight(beep_weight, bop_weight)
        print("The average of Beep and Bop's weight is " + str(average))

    else:
        print("Sorry, I didn't get that.")

# Starting the run function
run()