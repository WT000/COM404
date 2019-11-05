# Importing classes from Bot.py
from Bot import Bot

class SuperBot(Bot):
    def __init__(self, name, age, energy, shield, super_power_level):
        super().__init__(name, age, energy, shield)
        self.super_power_level = super_power_level

    def display_super_power_level(self):
        print(self.super_power_level)