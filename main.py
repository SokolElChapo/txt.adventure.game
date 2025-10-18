from intro import greet_player, choose_race, choose_character_class
from first_adventure import meticulous_adventure


def game_script():
    print("Farewell Adventurer, welcome to the World of Asgard, please tell us your Name")
    player_name = greet_player()
    print(f"What a Prodigious name {player_name}, which race do you want to select?")
    player_race = choose_race()
    print(f"Now that you`ve selected {player_race} please proceed on selecting which class are you willing to Play")
    player_class = choose_character_class()

    print(f"now you are ready for a meticulous adventure {player_class} {player_name} press Enter To Proceed")
    print(
        "You casually got hit by a truck, and you find yourself in a waste forest and near to you there is a Crystal Ball"
    )
    print("confused you go and check why is it shining")

    print("a virtual message appears into your brain, do you want to look at it?")
    meticulous_adventure(player_name)

    player_stats = {
        "HP": 100,
        "ATK": 10,
        "DEF": 5,
        "MANA": 3
    }

    print(f"{player_name} here are your stats {player_stats}")

if __name__ == "__main__":
    game_script()
