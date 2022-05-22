'''Sprint Challenge 3.1'''

from acme import Product
from acme_report import generate_products


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_weight():
    '''Test default product weight being 20'''
    prod = Product('Test Product')
    assert prod.weight == 20


def test_default_product_flame():
    '''Test default product flammability being 0.5'''
    prod = Product('Test Product')
    assert prod.flammability == 0.5


def test_stealability():
    '''Test that the method returns correct values.'''
    prod = Product('Test Product')
    assert prod.stealability() == "Kinda stealable."


def test_explode():
    '''Test that the method returns correcr values.'''
    prod = Product('Test Product')
    assert prod.explode() == "...boom!"


def test_gen_prod():
    '''Test that the function returns a list with a default number of
    30 items in it.'''
    prod = generate_products()
    assert len(prod) == 30
