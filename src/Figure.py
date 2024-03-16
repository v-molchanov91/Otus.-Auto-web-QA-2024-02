from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass


    def get_add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Need to transfer the figure")
        return self.get_area() + other_figure.get_area()

