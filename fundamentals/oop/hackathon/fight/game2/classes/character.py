import random

class Character:

    def __init__(self):
        self.strength = 20
        self.health = 100

    def attack(self, target):
        norm_attack = self.strength - random.randint(5,15)
        print(f"{self.name} attacked, {target.name} -{norm_attack} health")
        target.health -= norm_attack

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nStamina: {self.stamina}\nHealth: {self.health}\n")

    def heal(self):
        print(f"{self.name} is healing, +{self.stamina} health!")
        self.health += self.stamina

    def random_recovery(self):
        roll = random.randint(1,20)
        hp_added = random.randint(5,15)
        if (roll > 18):
            health_potion = hp_added + self.stamina
            print(f"{self.name} consumed a health potion! \n {health_potion} points recovered!")
            return health_potion
        else:
            self.health += hp_added
            print(f"{self.name} healed, + {hp_added} health!")