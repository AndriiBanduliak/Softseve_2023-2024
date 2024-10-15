class Goods:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            return self.discount_strategy(self.price)
        else:
            return self.price

    def __str__(self):
        return f'Price: {self.price}, price after discount: {self.price_after_discount()}'


def on_sale_discount(order):
    return order * 0.5


def twenty_percent_discount(order):
    return order * 0.8
