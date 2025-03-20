import random

from models.board import Board
from models.player import Player
from game.game_logic import Game

# Init board
board = Board()

# Init game
game = Game(board)

# Number of rounds to play
num_rounds = int(input("Enter the number of rounds to play: "))
# Number of players up to 4
num_players = int(input("Enter the number of players: "))

# Init player
players = []
for i in range(num_players):
    name = input(f"Enter player {i+1} name: ")
    players.append(Player(name))
    players[-1].position = game.game_start()

for player in players:
    print(f"{player.name} starts at {player.position.value.name}")

for round in range(num_rounds):
    print(f"\nRound {round + 1}")
    for player in players:  
        # Simulate rolling two dice
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_roll = dice1 + dice2
        current_property = game.move_player(player, dice_roll)

        print(f"{player.name} rolled a {dice_roll}")
        print(f"{player.name} landed on {current_property.name}")
