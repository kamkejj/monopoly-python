from .property_model import Property

class Player:
    def __init__(self, name: str):
        self.name = name
        self.position = None
        self.money = 1500  # Standard starting money in Monopoly
        self.in_jail = False
        self.jail_turns = 0  # Track how many turns a player has been in jail
        self.net_worth = 0
        self.properties = []

    def update_net_worth(self):
        """Update the player's net worth."""
        self.net_worth = self.money
        # @todo Add properties to net worth

    def add_property(self, property: Property):
        """Add a property to the player's properties."""
        self.properties.append(property)
        self.update_net_worth()

    def remove_property(self, property: Property):
        """Remove a property from the player's properties."""
        self.properties.remove(property)
        self.update_net_worth()
