from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.fixture(params=[(4, 7, 22), (3.5, 5.5, 18)])
def data(request):
    side_a, side_b, perimetr = 4, 7, 22

    yield side_a, side_b, perimetr

    side_a, side_b, perimetr = 4, 7, 22


@pytest.fixture(params=[(4, 16), (3.5, 14)])
def square_p(request):
    side_a, perimetr = request.param

    yield side_a, perimetr

    side_a, perimetr = 4, 16


@pytest.fixture
def circle():
    return Circle(5, "Circle")


@pytest.fixture
def triangle():
    return Triangle(3, 4, 5, "Triangle")

