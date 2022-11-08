import random


class Property:
    def __init__(self):
        self.selling_cost = random.randint(100, 300)
        self.rent = random.randint(1, 100)
        self.owner = None

    def can_be_bought(self, cash):
        """
        Checks if the property can be bought by a player
        :param cash: How much cash the player has
        """
        return cash >= self.selling_cost

    def vacate(self):
        """
        Vacates the property
        """
        self.owner = None
