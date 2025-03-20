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
    for player_index, player in enumerate(players):
        # Player may get multiple turns if they roll doubles
        doubles_count = 0
        taking_turn = True
        
        while taking_turn:
            # Execute player's turn using the game's player_turn method
            dice1, dice2, dice_roll, current_property, rolled_double, continue_turn = game.player_turn(player)

            print(f"{player.name} rolled a {dice1} and a {dice2} for a total of {dice_roll}")
            print(f"{player.name} landed on {current_property.name}")
            
            # Check if player rolled a double and if they should continue their turn
            if rolled_double and continue_turn:
                doubles_count += 1
                print(f"{player.name} rolled a double! They get another turn.")
                
                # In Monopoly, if a player rolls 3 doubles in a row, they go to jail
                if doubles_count == 3:
                    print(f"{player.name} rolled 3 doubles in a row and is going to jail!")
                    game.go_to_jail(player)
                    taking_turn = False
            else:
                # No double or player was sent to jail, turn is over
                taking_turn = False
