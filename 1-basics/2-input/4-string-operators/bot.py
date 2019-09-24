print("Please enter the number of lives.")
lives = int(input())
print("\nPlease enter the energy level.")
energy = int(input())
print("\nPlease enter the shield level.")
shield = int(input())

print("Health has been set.")

newlives = "♥" * lives
newenergy = "♦" * energy
newshield = "♦" * shield

print("Lives:  " + newlives)
print("Energy: " + newenergy)
print("Shield: " + newshield)