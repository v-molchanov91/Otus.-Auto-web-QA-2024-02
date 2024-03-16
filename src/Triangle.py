from abc import ABC, abstractmethod
import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.perimetr = (side_a + side_b + side_c) / 2

    def get_area(self):
        return (self.perimetr * (self.perimetr - self.side_a) * (self.perimetr - self.side_b) * (self.perimetr - self.side_c)) ** 0.5

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c


