class Bot:
    # Constructor
    def __init__(self, name, age=0, energy=0, shield=0):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield
        # Energy and shield could be a fixed number
        # Constants could be outside in the class, e.g. ENERGY =, SHIELD =

     # Methods
    def display_name(self):
        print("#" + "#" * len(self.name) + "#")
        print("#{}#".format(self.name))
        print("#" + "#" * len(self.name) + "#")

    def display_age(self):
        print(" " + str(self.age))
        print("/  \\")
        print("____")
        # As you can see, the cake is very high quality.

    def display_energy(self):
        print("Energy level:", "|" * self.energy)

    def display_shield(self):
        print("Shield level:", "O" * self.shield)

    def display_summary(self):
        print("{} is {} years old. \nEnergy level is: {} \nShield level is: {}".format(self.name, self.age, self.energy, self.shield))

    def __str__(self):
        return "name="+self.name, "age="+str(self.age), "energy="+str(self.energy), "shield="+str(self.shield)

# Object of Bot
# robo = Bot("Robo", 15, 5, 4)
# robo.display_summary()