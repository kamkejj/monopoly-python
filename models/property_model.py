class Property:
    """Define the attributes of a property"""

    # Constructor
    def __init__(self, name: str, purchase: int = None):
        self.name = name
        self.purchase = purchase

    # Getter
    @property
    def get_name(self):
        return self.name
