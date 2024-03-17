from abc import ABC, abstractmethod
import Figure


class Figure:
    def __init__(self, name):
        self.name = name


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
<<<<<<< Updated upstream
        super().__init__(name="Rectangel")
=======
        super().__init__(name="Rectangle")
>>>>>>> Stashed changes
        if side_a < 0 or side_b < 0:
            raise ValueError("You can't build a rectangle")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimetr(self):
        return 2 * (self.side_a + self.side_b)





