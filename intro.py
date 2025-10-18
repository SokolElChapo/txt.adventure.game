def greet_player() -> str:
    name = input(
        "Enter your nickname: "
    )
    if name == "":
        print("You must enter a valid name to proceed")
        return greet_player()
    return name


def choose_race() -> str:
    race = input("you need to choose between (Human, Dwarf, Elf, Demon): ")
    if race == "Human":
        print("As a Human you´ll have a bonus in Strategy.")
    elif race == "Dwarf":
        print("As a Dwarf you`ll be a great Engineer.")
    elif race == "Elf":
        print("As a Elf you`ll have a bonus in Archery.")
    elif race == "Demon":
        print("As a Demon you`ll receive a bonus in Dark Magic.")
    else:
        print("you`ve selected an invalid Race")
        return choose_race()

    return race


def choose_character_class() -> str:
    character_class = input("You must choose between Swordsman, Spearman, Archer, Mage, Alchemist: ")
    if character_class == "Swordsman":
        print("You've selected the Swordsman Class, you'll have assigned a base set for your class")
    elif character_class == "Spearman":
        print("You've selected the Spearman Class, you'll have assigned a base set for your class")
    elif character_class == "Archer":
        print("You've selected the Archer Class, you'll have assigned a base set for your class")
    elif character_class == "Mage":
        print("You've selected the Mage Class, you'll have assigned a base set for your class")
    elif character_class == "Alchemist":
        print("You've selected the Alchemist Class, you'll have assigned a base set for your class")
    else:
        print("You've selected an invalid Class")
        return choose_character_class()

    return character_class
