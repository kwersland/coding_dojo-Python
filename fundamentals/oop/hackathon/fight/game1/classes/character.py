import random

class Character:

    def __init__(self):
        self.strength = 20
        self.speed = 2
        self.health = 100

    def attack(self, target):
        print(f"{self.name} attacked")
        target.health -= self.strength 

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def random_recovery(self):
        roll = random.randint(1,20)
        hp_added = random.randint(5,15)
        if (roll > 18):
            health_potion = hp_added + random.randint(5,15)
            print(f"{self.name} consumed a health potion! \n {health_potion} points recovered!")
            return health_potion
        else:
            self.health += hp_added