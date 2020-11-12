class Users(list):
    cart = []

    def __init__(self, cart):
        self.cart = cart

    def __str__(self):
        return f'Корзина: {self.cart}'

