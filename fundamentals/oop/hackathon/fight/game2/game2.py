from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.monk import Monk
import random

ninja = Ninja("Ninja")
pirate = Pirate("Pirate")
monk = Monk("Monk")

you_are_ninja = [
    pirate,
    monk
]

you_are_pirate = [
    ninja,
    monk
]

you_are_monk = [
    ninja,
    pirate
]

print("Welcome to the Arena")
ninja.show_stats()
pirate.show_stats()
monk.show_stats()

choice = input(f"Choose your character\n a) Ninja \n b) Pirate \n c) Monk \n >")

# You Chose Ninja

if choice == "a":
    print("You are playing as the Ninja")
    cpu = random.choice(you_are_ninja)
    print(f"Your opponent is {cpu.name}")
    print("")
    ninja = Ninja(input("Name your fighter \n >"))
    print("")
    while ninja.health > 0 and cpu.health > 0:

# Your turn
        response = input("Will you \n 1) Attack \n 2) Heal \n 3) Both \n * upon selecting both you will both attack and heal for less points, \n but there is a chance you can get double or triple attack and a health potion \n >")
        if response == "1":
            ninja.attack(cpu)
        if response == "2":
            ninja.heal()
        if response == "3":
            ninja_random = [
        ninja.ninja_speed(cpu),
        ninja.random_recovery()
        ]
        print("")

# CPU's turn
        roll = random.randint(1,3)
        if roll == 1:
            cpu.attack(ninja)
        if roll == 2:
            cpu.attack(ninja)
        if roll == 3:
            cpu.heal()
        print("")

# Display health
        print(f"Your health is {ninja.health}")
        print(f"{cpu.name}'s health is {cpu.health}")
        print("")

    if ninja.health <= 0 and cpu.health <= 0:
        print("Stalemate!")
    elif cpu.health <= 0:
        print("Game Over, You Won!")
    else:
        print("Game Over, You Lost :(")
    print("")


# You Chose Pirate

if choice == "b":
    print("You are playing as the Pirate")
    cpu = random.choice(you_are_pirate)
    print(f"Your opponent is {cpu.name}")
    print("")
    pirate = Pirate(input("Name your fighter \n >"))
    print("")
    while pirate.health > 0 and cpu.health > 0:

# Your turn
        response = input("Will you \n 1) Attack \n 2) Heal \n 3) Both \n * upon selecting both you will both attack and heal for less points, \n but there is a chance you can get double or triple attack and a health potion \n >")
        if response == "1":
            pirate.attack(cpu)
        if response == "2":
            pirate.heal()
        if response == "3":
            pirate_random = [
        pirate.pirate_punch(cpu),
        pirate.random_recovery()
        ]
        print("")

# CPU's turn
        roll = random.randint(1,3)
        if roll == 1:
            cpu.attack(pirate)
        if roll == 2:
            cpu.attack(pirate)
        if roll == 3:
            cpu.heal()
        print("")

# Display health
        print(f"Your health is {pirate.health}")
        print(f"{cpu.name}'s health is {cpu.health}")
        print("")

    if pirate.health <= 0 and cpu.health <= 0:
        print("Stalemate!")
    elif cpu.health <= 0:
        print("Game Over, You Won!")
    else:
        print("Game Over, You Lost :(")
    print("")


# You Chose Monk

if choice == "c":
    print("You are playing as the Monk")
    cpu = random.choice(you_are_monk)
    print(f"Your opponent is {cpu.name}")
    print("")
    monk = Monk(input("Name your fighter \n >"))
    print("")
    while monk.health > 0 and cpu.health > 0:

# Your turn
        response = input("Will you \n 1) Attack \n 2) Heal \n 3) Both \n * upon selecting both you will both attack and heal for less points, \n but there is a chance you can get double or triple attack and a health potion \n >")
        if response == "1":
            monk.attack(cpu)
        if response == "2":
            monk.heal()
        if response == "3":
            monk_random = [
        monk.airbend(cpu),
        monk.random_recovery()
        ]
        print("")

# CPU's turn
        roll = random.randint(1,3)
        if roll == 1:
            cpu.attack(monk)
        if roll == 2:
            cpu.attack(monk)
        if roll == 3:
            cpu.heal()
        print("")

# Display health
        print(f"Your health is {monk.health}")
        print(f"{cpu.name}'s health is {cpu.health}")
        print("")

    if monk.health <= 0 and cpu.health <= 0:
        print("Stalemate!")
    elif cpu.health <= 0:
        print("Game Over, You Won!")
    else:
        print("Game Over, You Lost :(")
    print("")

