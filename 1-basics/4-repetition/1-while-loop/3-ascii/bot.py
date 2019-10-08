# Asking the user how many bars should be charged
print("How many bars should be charged?")
max_bars = int(input())

# Bars control variable
charged_bars = 0

while (charged_bars < max_bars):
    charged_bars = charged_bars + 1
    print("Charging: ", "█" * charged_bars)

# Completed battery charge
print("The battery is fully charged.")