'''Sprint Challenge 3.1'''

import random
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''This function generates a random list of ACME products.'''
    products = []
    for num in range(num_products):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        price = random.randint(5, 101)
        weight = random.randint(5, 101)
        flammability = random.uniform(0.0, 2.6)
        products.append(Product(name=name, price=price,
                        weight=weight, flammability=flammability))
    return products


def inventory_report(products):
    '''This function takes a list of products and returns some basic
    statistics about the list of products.'''
    names = []
    costs = []
    pounds = []
    hazard = []
    for item in products:
        names.append(item.name)
        costs.append(item.price)
        pounds.append(item.weight)
        hazard.append(item.flammability)
    my_set = set(names)
    unique = len(my_set)
    average_price = sum(costs) / len(costs)
    average_weight = sum(pounds) / len(pounds)
    average_flammability = sum(hazard) / len(hazard)
    return unique, average_price, average_weight, average_flammability


if __name__ == '__main__':
    print(inventory_report(generate_products()))
