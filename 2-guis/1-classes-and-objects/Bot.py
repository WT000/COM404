class Bot:
    # Constructor
    def __init__(self, name, age=0, energy=0, shield=0):
        self.__name = name
        self.__age = age
        self.__energy = energy
        self.__shield = shield
        # Energy and shield could be a fixed number
        # Constants could be outside in the class, e.g. ENERGY =, SHIELD =

     # Methods
    def display_name(self):
        print("#" + "#" * len(self.__name) + "#")
        print("#{}#".format(self.__name))
        print("#" + "#" * len(self.__name) + "#")

    def display_age(self):
        print(" " + str(self.__age))
        print("/  \\")
        print("____")
        # As you can see, the cake is very high quality.

    def display_energy(self):
        print("Energy level:", "|" * self.__energy)

    def display_shield(self):
        print("Shield level:", "O" * self.__shield)

    def display_summary(self):
        print("{} is {} years old. \nEnergy level is: {} \nShield level is: {}".format(self.__name, self.__age, self.__energy, self.__shield))

    def __str__(self):
        return "name="+self.__name, "age="+str(self.__age), "energy="+str(self.__energy), "shield="+str(self.__shield)

# Object of Bot
# robo = Bot("Robo", 15, 5, 4)
# robo.display_summary()