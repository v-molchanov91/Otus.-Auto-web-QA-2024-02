from src.Rectangel import Rectangle
from src.Square import Square
from src.Circle import Circle
import pytest
from datetime import datetime


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [(7, 9, 63), (3.15, 4.33, 13.6395)])
def test_rectangel_add_int(side_a, side_b, area):
    a = Rectangle(side_a, side_b, name="Rectangle")
    assert a.get_area() == area, f'area should be {side_a * side_b}'


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [(-3, 5)])
def test_rectangel_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b, name="Rectangle")


def test_perimetr_rectangle(data):
    side_a, side_b, perimetr = data
    a = Rectangle(side_a, side_b, name="Rectangle")
    assert a.get_perimetr() == perimetr, f'area should be {2 * (side_a * side_b)}'


@pytest.mark.parametrize(
    ("side_a", "area"),
    [(4, 16), (2.5, 6.25)])
def test_area_square(side_a, area):
    a = Square(side_a, name="Square")
    assert a.get_area() == area, f'area should be {2 ** side_a}'


@pytest.mark.parametrize(
    ("side_a", "area"),
    [(-4, 16)])
def test_negative_area_square(side_a, area):
    with pytest.raises(ValueError):
        Square(side_a, name="Square")


def test_perimetr_suare(square_p):
    side_a, perimetr = square_p
    a = Square(side_a, name="Square")
    assert a.get_perimetr() == perimetr, f'area should be {side_a * 4}'


def test_get_area_circle(circle):
    expected_area = 78.5398
    area = circle.get_area()
    assert area == pytest.approx(expected_area)


def test_get_perimetr_circle(circle):
    expected_perimetr = 31.4159
    perimetr = circle.get_perimetr()
    assert perimetr == pytest.approx(expected_perimetr)


def test_get_area_triangle(triangle):
    expected_area = 6
    area = triangle.get_area()
    assert area == pytest.approx(expected_area)


def test_get_perimetr_triangle(triangle):
    expected_perimetr = 12
    perimetr = triangle.get_perimetr()
    assert perimetr == pytest.approx(expected_perimetr)

