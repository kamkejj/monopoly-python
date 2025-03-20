from models.board import Board
from models.player import Player

class Game:
    def __init__(self, board: Board):
        self.board = board

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
        print(f"{player.name} was sent to Jail!")