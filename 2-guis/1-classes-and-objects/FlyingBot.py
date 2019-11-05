# Importing classes from SuperBot
from SuperBot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self, name, age, energy, shield, super_power_level, hover):
        super().__init__(name, age, energy, shield, super_power_level)
        self.hover = hover

    def display_hover(self):
        print(self.hover)