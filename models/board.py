from .property_model import Property
from .player import Player

class PropertyNode:
    """Node for linked list for each Property"""

    def __init__(self, prop: Property):
        self.value = prop
        self.next = None

class Board:
    """Board for the game as a circular linked list"""

    def __init__(self):
        self.start = None
        self.initialize()

    def initialize(self):
        """Initialize the board"""
        go = PropertyNode(Property("Go"))
        p1 = PropertyNode(Property("Mediteranean Avenue", 60))
        p2 = PropertyNode(Property("Community Chest"))
        p3 = PropertyNode(Property("Baltic Avenue", 60))
        p4 = PropertyNode(Property("Income Tax"))
        p5 = PropertyNode(Property("Reading Railroad", 200))
        p6 = PropertyNode(Property("Oriental Avenue", 100))
        p7 = PropertyNode(Property("Vermont Avenue", 100))
        p8 = PropertyNode(Property("Connecticut Avenue", 120))
        p9 = PropertyNode(Property("Jail"))
        p10 = PropertyNode(Property("St. Charles Place", 140))
        p11 = PropertyNode(Property("Electric Company", 150))
        p12 = PropertyNode(Property("States Avenue", 140))
        p13 = PropertyNode(Property("Virginia Avenue", 160))
        p14 = PropertyNode(Property("Pennsylvania Railroad", 200))
        p15 = PropertyNode(Property("St. James Place", 180))
        p16 = PropertyNode(Property("Community Chest"))
        p17 = PropertyNode(Property("Tennessee Avenue", 180))
        p18 = PropertyNode(Property("New York Avenue", 200))
        p19 = PropertyNode(Property("Free Parking"))
        p20 = PropertyNode(Property("Kentucky Avenue", 220))
        p21 = PropertyNode(Property("Chance"))
        p22 = PropertyNode(Property("Indiana Avenue", 220))
        p23 = PropertyNode(Property("Illinois Avenue", 240))
        p24 = PropertyNode(Property("B. & O. Railroad", 200))
        p25 = PropertyNode(Property("Atlantic Avenue", 260))
        p26 = PropertyNode(Property("Ventnor Avenue", 260))
        p27 = PropertyNode(Property("Water Works", 150))
        p28 = PropertyNode(Property("Marvin Gardens", 280))
        p29 = PropertyNode(Property("Go To Jail"))
        p30 = PropertyNode(Property("Pacific Avenue", 300))
        p31 = PropertyNode(Property("North Carolina Avenue", 300))
        p32 = PropertyNode(Property("Community Chest"))
        p33 = PropertyNode(Property("Pennsylvania Avenue", 320))
        p34 = PropertyNode(Property("Short Line", 200))
        p35 = PropertyNode(Property("Chance"))
        p36 = PropertyNode(Property("Park Place", 350))
        p37 = PropertyNode(Property("Luxury Tax", ))
        p38 = PropertyNode(Property("Boardwalk", 400))

        # Set linked list of the board
        go.next = p1
        p1.next = p2
        p2.next = p3
        p3.next = p4
        p4.next = p5
        p5.next = p6
        p6.next = p7
        p7.next = p8
        p8.next = p9
        p9.next = p10
        p10.next = p11
        p11.next = p12
        p12.next = p13
        p13.next = p14
        p14.next = p15
        p15.next = p16
        p16.next = p17
        p17.next = p18
        p18.next = p19
        p19.next = p20
        p20.next = p21
        p21.next = p22
        p22.next = p23
        p23.next = p24
        p24.next = p25
        p25.next = p26
        p26.next = p27
        p27.next = p28
        p28.next = p29
        p29.next = p30
        p30.next = p31
        p31.next = p32
        p32.next = p33
        p33.next = p34
        p34.next = p35
        p35.next = p36
        p36.next = p37
        p37.next = p38
        # Back to start "Go"
        p38.next = go

        # Starting place (property) on the board
        self.start = go

    def traverse(self, steps: int, starting_position=None):
        """Traverse the board a certain number of steps from a position."""
        if starting_position is None:
            starting_position = self.start

        current = starting_position
        for _ in range(steps):
            current = current.next

        return current

    def income_tax(self, player: Player):
        """Player pays income tax.
        
        Player can pay $200 or %10 of their net worth.

        Args:
            player (Player): The player who pays the income tax.
        """
        # Player can pay $200 or %10 of their net worth
        tax = min(200, 0.1 * player.money)
        player.money -= tax
        print(f"{player.name} paid income tax of {tax}.")

