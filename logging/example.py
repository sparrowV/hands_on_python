import logging
import  os
os.remove("test.log")

logger = logging.getLogger("The logger")
logger.setLevel(logging.DEBUG)
logger_file = logging.FileHandler("test.log")
logger_file.setFormatter(logging.Formatter("%(levelname)s:%(asctime)s:%(message)s"))
logger.addHandler(logger_file)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logger.info("Create item with name {} and price {}".format(name,price))

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class ShoppingCart:
    def __init__(self):
        logger.info("Create shopping cart")
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        logger.info("adding item with name {} to shopping cart".format(item.get_name()))

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.get_name() != item_name]
        logger.info("removing item with name {} from shopping cart".format(item_name))

    def get_total_price(self):
        sum = 0
        for item in self.items:
            sum += item.get_price()
        return sum


class Client:
    def __init__(self, username):
        self.shopping_cart = None
        self.username = username
        self.balance = 0
        logger.info("Create client with username {}".format(username))

    def add_funds(self, amount):
        self.balance += amount
        logger.info("Increase balance by {} for client {}".format(amount,self.username))

    def set_shopping_cart(self, shopping_cart):
        self.shopping_cart = shopping_cart
        logger.info("Setting shopping cart for client {}".format(self.username))

    def get_shopping_cart(self):
        return self.shopping_cart

    def checkout(self):
        total_price = self.shopping_cart.get_total_price()
        if (total_price > self.balance):
            logger.error("Couldn't checkout: Client balance is {} ,"
                         " but cart total price is {}".format(self.balance,total_price))
        else:
            self.shopping_cart = None
            self.balance -= total_price
            logger.info("Successful checkout : checkout amount is {} , "
                        "remaining balance is {}".format(total_price,self.balance))

client = Client("Sam")
client.add_funds(500)
shopping_cart = ShoppingCart()
item1 = Item("item1",100)
item2 = Item("item2",200)
item3 = Item("item3",300)
# item3 = Item("item3",200)
shopping_cart.add_item(item1)
shopping_cart.add_item(item2)
shopping_cart.add_item(item3)
# shopping_cart.remove_item("item2")
client.set_shopping_cart(shopping_cart)
client.checkout()

