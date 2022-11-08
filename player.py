import random


class Player:
    def __init__(self, persona):
        self.cash = 300
        self.persona = persona
        self.rounds_played = 0

    def buy_property(self, property):
        """
        Buy the property
        :param property: property that will be bought
        """
        buy = [self.persona == 'impulsivo' and property.can_be_bought(self.cash),
               self.persona == 'exigente' and property.can_be_bought(self.cash) and property.rent > 50,
               self.persona == 'cauteloso' and self.cash - property.selling_cost >= 80,
               self.persona == 'aleatorio' and property.can_be_bought(self.cash) and random.choice([False, True])]
        if any(buy):
            self.cash -= property.selling_cost
            return True
        return False
