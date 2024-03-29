from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, name):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("нельзя создать треугольник")
        elif side_a + side_b < side_c and side_b + side_c < side_a and side_a + side_b < side_b:
            raise ValueError("фигура не является треугольником")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return (1 / 2) * (self.side_a * self.side_b * self.side_c) ** 0.5

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

