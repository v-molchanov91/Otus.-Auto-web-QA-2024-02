import math
from abc import ABC, abstractmethod
import Figure


class Figure:
    def __init__(self, name):
        self.name = name


class Circle(Figure):

    def __init__(self, radius, name):
        super().__init__(name="Circle")
        if radius < 0:
            ValueError("You can't build a Circle")
<<<<<<< Updated upstream
            self.radius = radius
=======
        self.radius = radius
>>>>>>> Stashed changes

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimetr(self):
        return 2 * math.pi * self.radius
<<<<<<< Updated upstream
=======

a = Circle(8, "Circle")

print(a.get_area())
>>>>>>> Stashed changes
