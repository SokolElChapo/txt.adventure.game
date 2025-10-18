def fight() -> bool:
    answer = input("you found near to you a rusted sword do you want to use it? (Yes/No)")
    if answer == "Yes":
        return True
    elif answer == "No":
        return False
    else:
        print("you must select a valid answer")
        return fight()


def goblin_attack() -> None:
    answer = input("what do you want to do? (Run/Fight)")
    if answer == "":
        print("you must select a valid answer")
        return goblin_attack()

    if answer == "Run":
        print("you started running with all the energy you had, after some time you reach a non turning point.")
        print("you must fight the goblin to survive")

    is_victory = fight()
    if is_victory:
        print("you fight and defeat the goblin")
    else:
        print("you died from a goblin attack.")
    return None


def meticulous_adventure(player_name: str) -> None:
    answer = input("Please type Yes or No: ")

    if answer == "Yes":
      print(f"Hello {player_name} Welcome to the virtual World of Asgard.")
      print(f"I know that you're probably confused, who am I and how I am talking to you.")
      print(f"that's not what it matters right now, in short, you Died and got resurrected with advanced technology")
      print(f"welcome back to life. {player_name}! From now on your new life begins here in the huge world of Asgard.")
      print("for more info please use your mind to activate the statistic interface, and have fun in this new life of yours!")
    elif answer == "No":
      print("a Goblin sees you and starts attacking you.")
      goblin_attack()
    else:
      print("you need to choose a valid answer yes or no")
      return meticulous_adventure(player_name)
    return None