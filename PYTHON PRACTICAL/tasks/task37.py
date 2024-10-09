from abc import abstractmethod, ABC


class FactoryProducer(ABC):

    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory()
        if type_of_factory == 'french':
            return FrenchDishesFactory()


class Factory(FactoryProducer):


    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return FetuccineAlfredo()
        if type_of_meal == 'dessert':
            return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()
        if type_of_meal == 'dessert':
            return CremeBrulee()


class Product(ABC):
    @abstractmethod
    def cook(self):
        pass


class FetuccineAlfredo(Product):
    def __init__(self):
        self.name = "Fettuccine Alfredo"

    def cook(self):
        return print(f'Italian main course prepared: {self.name}')


class Tiramisu(Product):
    def __init__(self):
        self.name = "Tiramisu"

    def cook(self):
        return print(f'Italian dessert prepared: {self.name}')


class DuckALOrange(Product):
    def __init__(self):
        self.name = "Duck À L'Orange"

    def cook(self):
        return print(f'French main course prepared: {self.name}')


class CremeBrulee(Product):
    def __init__(self):
        self.name = "Crème brûlée"

    def cook(self):
        return print(f'French dessert prepared: {self.name}')

