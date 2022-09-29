from classes.ninja import Ninja
from classes.pirate import Pirate
import random

ninja = Ninja("You")
pirate = Pirate("Popeye")

sayings = [
    "I yam what I yam an' tha's all I yam",
    "Ahoy!",
    "Oh my gorshk!",
    "Arf! Arf!",
    "I'm strong to the finich, cause I eats me spinach, \n I'm Popeye the Sailor Man!"
]


print("Welcome to the Arena")
print("You are playing as the Ninja")
print("Your opponent, Popeye, \n says 'If we can't be frens we'll be emenies'")

while ninja.health > 0 and pirate.health > 0:

    response = input("Will you \n 1) Attack \n 2) Heal \n >")
    if response == "1":
        ninja.ninja_speed(pirate)
    if response == "2":
        ninja.random_recovery()
        print("You ate Onigiri")
    roll = random.randint(1,3)
    if roll == 1:
        pirate.pirate_punch(ninja)
        rand = random.randrange(5)
        print(f"Popeye said '{sayings[rand]}'")
    if roll == 2:
        pirate.random_recovery()
        print("Popeye ate some spinach")
    if roll == 3:
        print("*rattled Popeye says 'Shiver me timbers!'")

    print(f"Your health is {ninja.health}")
    print(f"Popeye's health is {pirate.health}")

if pirate.health <= 0 and ninja.health <= 0:
    print("Stalemate!")
elif pirate.health <= 0:
    print("Game Over, You Won! \n Popeye says 'Thats all I can stands, cause I cant stands no more!'")
else:
    print("Game Over, You Lost :( \n Popeye stands over your unconcious body \n and says uhkuhkuhkuhk while smoking his pipe")





