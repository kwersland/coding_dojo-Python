from classes.character import Character
import random

class Pirate(Character):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.stamina = 20
        self.strength = 30

    def pirate_punch(self, target):
        roll = random.randint(1,20)
        damage = self.strength
        if (roll > 18):
            self.strength *= random.randint(1,5)
            if self.strength > 119:
                target.health -= (damage * 3)
                print(f"Super Pirate Punch: Triple Damage!  {target.name} -{damage * 3} health")
            elif self.strength > 59:
                target.health -= (damage * 2)
                print(f"Pirate Punch: Double Damage!  {target.name} -{damage * 2} health")
            else:
                target.health -= damage
                print(f"{self.name} attacked! {target.name} -{damage} health")
        else:
            target.health -= damage
            print(f"{self.name} attacked! {target.name} -{damage} health")

