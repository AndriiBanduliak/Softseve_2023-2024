class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        Pizza.order_number += 1
        self.order_number = Pizza.order_number
        self.ingredients = ingredients

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])


# Reset order_number before running tests
Pizza.order_number = 0

p1 = Pizza(["bacon", "parmesan", "ham"])
print(p1.ingredients)
print(p1.order_number)

p2 = Pizza(["bacon2", "parmesan2", "ham2"])
print(p2.ingredients)
print(p2.order_number)

p3 = Pizza.garden_feast()
print(p3.ingredients)
print(p3.order_number)

p4 = Pizza.hawaiian()
print(p4.ingredients)
print(p4.order_number)

p5 = Pizza.meat_festival()
print(p5.ingredients)
print(p5.order_number)

my_pizza = Pizza(["pepperoni", "cheese"])
print(my_pizza.ingredients)
print(my_pizza.order_number)

print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
print(my_pizza.order_number)
