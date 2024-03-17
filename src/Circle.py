import math
from src import Figure


class Circle(Figure):

    def __init__(self, radius, name):
        super().__init__(name="Circle")
        if radius < 0:
            ValueError("You can't build a Circle")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimetr(self):
        return 2 * math.pi * self.radius

