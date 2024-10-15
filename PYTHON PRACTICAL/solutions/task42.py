import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:

    def __init__(self, products=[]):
        self.product_list = products

    def add_product(self, product):
        self.product_list.append(product)

    def clear_cart(self):
        self.product_list.clear()

    @staticmethod
    def get_discount(total_count):
        discount = 0
        if total_count >= 5 and total_count < 7:
            discount = 5
        elif total_count >= 7 and total_count < 10:
            discount = 10
        elif total_count >= 10 and total_count < 20:
            discount = 20
        elif total_count >= 20:
            discount = 30
        else:
            discount = 0
        return discount

    def get_total_price(self):
        total_price = 0
        for product in self.product_list:
            disc = self.get_discount(product.count)
            price = product.price * product.count
            price = price - (price * disc / 100)
            total_price += price
        return total_price


class CartTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.clear_cart()
        self.product1 = Product("Product A", 10, 3)
        self.product2 = Product("Product B", 20, 5)
        self.product3 = Product("Product C", 5, 7)
        self.product4 = Product("Product D", 6, 10)
        self.product5 = Product("Product E", 7, 20)
        self.product6 = Product("Product F", 8, 30)

    def tearDown(self):
        self.cart.clear_cart()

    def test_add_product(self):
        self.cart.add_product(self.product1)
        self.assertEqual(len(self.cart.product_list), 1)
        self.assertEqual(self.cart.product_list[0].name, "Product A")

    def test_no_discount(self):
        self.cart.add_product(self.product1)
        t_price = self.cart.get_total_price()
        exp_price = self.product1.price * self.product1.count
        self.assertEqual(t_price, exp_price)

    def test_5_discount(self):
        self.cart.add_product(self.product2)
        t_price = self.cart.get_total_price()
        exp_price_wod = (self.product2.price * self.product2.count)
        exp_price = exp_price_wod - (exp_price_wod * 5 / 100)
        self.assertEqual(t_price, exp_price)

    def test_7_discount(self):
        self.cart.add_product(self.product3)
        t_price = self.cart.get_total_price()
        exp_price_wod = (self.product3.price * self.product3.count)
        exp_price = exp_price_wod - (exp_price_wod * 10 / 100)
        self.assertEqual(t_price, exp_price)

    def test_10_discount(self):
        self.cart.add_product(self.product4)
        t_price = self.cart.get_total_price()
        exp_price_wod = (self.product4.price * self.product4.count)
        exp_price = exp_price_wod - (exp_price_wod * 20 / 100)
        self.assertEqual(t_price, exp_price)

    def test_20_discount(self):
        self.cart.add_product(self.product5)
        t_price = self.cart.get_total_price()
        exp_price_wod = (self.product5.price * self.product5.count)
        exp_price = exp_price_wod - (exp_price_wod * 30 / 100)
        self.assertEqual(t_price, exp_price)
