'''Sprint Challenge 3.1'''

import random


class Product:

    '''This class contains functions to help determine different
    attributes of ACME products.'''

    def __init__(self, name, identifier=random.randint(999999, 10000000),
                 price=10, weight=20, flammability=0.5):
        self.name = name
        self.identifier = identifier
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        '''This function will determine how stealable a product is.'''
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        if 0.5 <= ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        '''This function will determine how explosive a product is.'''
        result = self.flammability * self.weight
        if result < 10:
            return "...fizzle."
        elif (result >= 10) & (result < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):

    '''This is a child class of Product that contains functions specific to
    boxing glove products.'''

    def __init__(self, name, identifier=random.randint(999999, 10000000),
                 price=10, weight=10, flammability=0.5):
        super().__init__(name, identifier, price, weight, flammability)

    def explode(self):
        '''This function overides the Product explode() function to always
        return "...it's a glove." in the output.'''
        return "...it's a glove."

    def punch(self):
        '''This function will determines the affect of a punch depending on
        the weight of a boxing glove.'''
        if self.weight < 5:
            return "That tickles."
        if 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
