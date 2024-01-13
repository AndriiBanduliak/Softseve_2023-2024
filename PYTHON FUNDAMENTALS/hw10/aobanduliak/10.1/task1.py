class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]


class Rectangle(Polygon):
    def __init__(self, length, breadth):
        Polygon.__init__(self, 2)
        self.sides = [length, breadth]

    def find_square(self):
        return self.sides[0] * self.sides[1]
