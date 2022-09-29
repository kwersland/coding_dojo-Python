from classes.character import Character
import random

class Monk(Character):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 100
        self.stamina = 35

    def airbend(self, target):
        roll = random.randint(1,20)
        damage = self.strength
        if (roll > 18):
            self.strength *= random.randint(1,5)
            if self.strength > 79:
                target.health -= (damage * 3)
                print(f"Vortex: Triple Damage!  {target.name} -{damage * 3} health")
            elif self.strength > 39:
                target.health -= (damage * 2)
                print(f"Air Whip: Double Damage!  {target.name} -{damage * 2} health")
            else:
                target.health -= damage
                print(f"{self.name} attacked! {target.name} -{damage} health")
        else:
            target.health -= damage
            print(f"{self.name} attacked! {target.name} -{damage} health")

