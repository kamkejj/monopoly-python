import random

from models.board import Board
from models.player import Player

class Game:
    def __init__(self, board: Board):
        self.board = board
        # Dictionary to track landing spots: {property_name: count}
        self.landing_spots = {}
        # Dictionary to track dice combinations: {(dice1, dice2): count}
        self.dice_combinations = {}

    def game_start(self):
        return self.board.start

    def move_player(self, player, steps):
        """Move the player a certain number of steps on the board."""
        if player.position is None:
            player.position = self.board.start

        # Move the player
        for _ in range(steps):
            player.position = player.position.next

        # Get current property
        current_property = player.position.value
        
        # Track landing spots (except for Go To Jail which is tracked in go_to_jail method)
        if current_property.name != "Go To Jail":
            property_name = current_property.name
            self.landing_spots[property_name] = self.landing_spots.get(property_name, 0) + 1

        # Check if player landed on Go To Jail
        if current_property.name == "Go To Jail":
            self.go_to_jail(player)
            current_property = player.position.value  # Update current property after going to jail

        return current_property

    def go_to_jail(self, player: Player):
        """Send the player to Jail."""
        # Find the Jail position
        current = self.board.start
        while current.value.name != "Jail":
            current = current.next
            
        # Move player to Jail
        player.position = current
        player.in_jail = True
        player.jail_turns = 0  # Reset jail turns counter
        print(f"{player.name} was sent to Jail!")
        
        # Track landing on Jail (via Go To Jail)
        property_name = "Jail"
        self.landing_spots[property_name] = self.landing_spots.get(property_name, 0) + 1
        
        # Player loses their turn when sent to jail
        return False
        
    def roll_dice(self):
        """Simulate rolling two dice and return the sum."""
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        # Track dice combinations (normalize so that (1,6) and (6,1) are the same)
        # For doubles, keep the order the same
        if dice1 == dice2:
            dice_combo = (dice1, dice2)
        else:
            # Sort the dice values to normalize the combination
            dice_combo = tuple(sorted([dice1, dice2]))
            
        self.dice_combinations[dice_combo] = self.dice_combinations.get(dice_combo, 0) + 1
        
        return dice1, dice2, dice1 + dice2
        
    def player_turn(self, player: Player):
        """Handle a player's turn including rolling dice and moving.
        
        Returns:
            tuple: A tuple containing (dice1, dice2, dice_roll, current_property, rolled_double, continue_turn)
                where rolled_double is a boolean indicating if the player rolled a double,
                and continue_turn is a boolean indicating if the player's turn should continue.
        """
        # Check if player is in jail
        if player.in_jail:
            # Roll the dice
            dice1, dice2, dice_roll = self.roll_dice()
            
            # Check if the player rolled a double
            rolled_double = dice1 == dice2
            
            if rolled_double:
                # Player gets out of jail with a double
                player.in_jail = False
                player.jail_turns = 0  # Reset jail turns counter
                print(f"{player.name} rolled a double and got out of Jail!")
                
                # Move the player and get the current property
                current_property = self.move_player(player, dice_roll)
                
                # Check if they landed on Go To Jail again
                if current_property.name == "Go To Jail":
                    continue_turn = self.go_to_jail(player)
                    current_property = player.position.value  # Update to Jail
                else:
                    continue_turn = True
            else:
                # Increment jail turns counter
                player.jail_turns += 1
                
                # Check if player has been in jail for 3 turns
                if player.jail_turns >= 3:
                    # Player gets out of jail after 3 turns
                    player.in_jail = False
                    player.jail_turns = 0  # Reset jail turns counter
                    print(f"{player.name} has been in Jail for 3 turns and is now released!")
                    
                    # Move the player and get the current property
                    current_property = self.move_player(player, dice_roll)
                    
                    # Check if they landed on Go To Jail again
                    if current_property.name == "Go To Jail":
                        continue_turn = self.go_to_jail(player)
                        current_property = player.position.value  # Update to Jail
                    else:
                        continue_turn = True
                else:
                    # Player stays in jail
                    print(f"{player.name} failed to roll a double and stays in Jail. (Turn {player.jail_turns}/3)")
                    current_property = player.position.value  # They're still in Jail
                    continue_turn = False  # End turn
        else:
            # Normal turn for player not in jail
            dice1, dice2, dice_roll = self.roll_dice()
            
            # Check if the player rolled a double
            rolled_double = dice1 == dice2
            
            # Move the player and get the current property
            current_property = self.move_player(player, dice_roll)
            
            # Check if player landed on Go To Jail
            if current_property.name == "Go To Jail":
                continue_turn = self.go_to_jail(player)
                current_property = player.position.value  # Update to Jail
            else:
                continue_turn = True
        
        # Return the dice values, current property, whether a double was rolled, and if turn continues
        return dice1, dice2, dice_roll, current_property, rolled_double, continue_turn
        
    def get_landing_stats(self):
        """Return statistics about landing spots."""
        return self.landing_spots
    
    def get_dice_stats(self):
        """Return statistics about dice combinations."""
        return self.dice_combinations