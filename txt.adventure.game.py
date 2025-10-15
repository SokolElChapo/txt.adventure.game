import random
import character
input("Farewell Adventurer, welcome to the World of Asgard, please tell us your Name, Press Enter To Proceed")
Name = input("Enter your nickname: ")
print (f"What a Prodigious name {Name}, which race do you want to select?")
race = input("you need to choose between (Human, Dwarf, Elf, Demon: ")

def choose_race(race):
    if  race == "Human":
      print("As a Human you´ll have a bonus in Strategy.")
    elif race == "Dwarf":
      print("As a Dwarf you`ll be a great Engineer.")
    elif race == "Elf":
      print("As a Elf you`ll have a bonus in Archery.")
    elif race == "Demon":
      print("As a Demon you`ll receive a bonus in Dark Magic.")
    else:
      print("you`ve selected an invalid Race")
      return choose_race(race)
    return race

print(f"Now that you`ve selected {race} please proceed on selecting which class are you willing to Play")

Class = input("You must choose between Swordsman, Spearman, Archer, Mage, Alchemist: ")
def combat_class(Class):
    if Class == "Swordsman":
      print("You've selected the Swordsman Class, you'll have assigned a base set for your class")
    elif Class == "Spearman":
      print("You've selected the Spearman Class, you'll have assigned a base set for your class")
    elif Class == "Archer":
      print("You've selected the Archer Class, you'll have assigned a base set for your class")
    elif Class == "Mage":
      print("You've selected the Mage Class, you'll have assigned a base set for your class")
    elif Class == "Alchemist":
      print("You've selected the Alchemist Class, you'll have assigned a base set for your class")
    else:
      print("You've selected an invalid Class")
      return combat_class(Class)
    return Class
input(f"now you are ready for a meticulous adventure {Name} press Enter To Proceed ")

print(f"You casually got hit by a truck, and you find yourself in a waste forest and near to you there is a Crystal Ball ")

print(f"confused you go and check why is it shining")

identity = input("a virtual message appears into your brain, do you want to look at it? (Yes/No)")


def yes_or_no(answer):

    if answer == "Yes":
      print(f"Hello {Name} Welcome to the virtual World of Asgard.")
      print(f"I know that you're probably confused, who am I and how I am talking to you.")
      print(f"that's not what it matters right now, in short, you Died and got resurrected with advanced technology")
      print(f"welcome back to life. {Name}! From now on your new life begins here in the huge world of Asgard.")
      print("for more info please use your mind to activate the statistic interface, and have fun in this new life of yours!")
    elif answer == "No":
      print("a Goblin sees you and starts attacking you.")
      fight1 = input("what do you want to do? (Run/Fight)")
      def goblin_attack(fight1):
            if answer =="Run":
                    print("you started running with all the energy you had, after some time you reach a non turning point.")
                    print("you must fight the goblin to survive")
                    sword = input("you found near to you a rusted sword do you want to use it? (Yes/No)")
                    if answer == "Yes":
                         print("you fight and defeat the goblin")
                    elif answer == "No":
                         print("you died from a goblin attack.")
                    else:
                       print("you must select a valid answer")
                       return goblin_attack(fight1)
                    return fight1
      goblin_attack(fight1)
    else:
      print("you need to choose a valid answer")
      new_answer = input("Please type Yes or No: ").capitalize()
      return yes_or_no(answer)
    return answer

yes_or_no(identity)

player_stats = {
    "HP": 100,
    "ATK": 10,
    "DEF": 5,
    "MANA": 3
}
print(f"Hello {Name} here are your stats {player_stats}")
