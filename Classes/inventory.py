"""
Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an inventory class which keeps track of various products
and can sum up the inventory value.
"""


class Product:
    """Defines price, name, quantity of product."""
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity

    def recieve(self, i):
        self.quantity = self.quantity + i

    def remove(self, i):
        self.quantity = self.quantity - i


class Inventory:
    pass
