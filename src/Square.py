from abc import ABC, abstractmethod
import Figure

class Square(Figure)

    def __init__(self, side_a):
        super().__init__(name = "Square")
        if side_a < 0
            raise ValueError("You can't build a Square")
        self.side_a = side_a


    def get_area(self):
        return self.side_a ** 2

    def get_perimetr(self):
        return  self.side_a * 4
