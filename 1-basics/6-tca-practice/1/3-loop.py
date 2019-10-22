# Asking the user how many miles must be travelled
print("How many miles must I travel before I reach the secret base?")

# Miles variable
miles = int(input())

# Countdown miles loop
print("I will count the miles...")
for count in range(miles, 0, -1):
    print("I have", count, "miles to go before I reach the base.")

# Final message
print("I have arived at the secret headquarters of the MIB! \nIt is time to sneak in.")