import math
import pytest
from src.circle import Circle
from src.rectangle import Rectangle


def test_circle_creation_success():
    circle = Circle(5)
    assert circle.radius == 5


def test_circle_perimeter():
    circle = Circle(3)
    assert circle.perimeter == 2 * math.pi * 3


def test_circle_area():
    circle = Circle(4)
    assert circle.area == 4 * 4 * math.pi


@pytest.mark.parametrize("invalid_radius", [0, -1, -5.5])
def test_circle_invalid_radius_raises_error(invalid_radius):
    with pytest.raises(ValueError, match="All sides must be greater than 0"):
        Circle(invalid_radius)


def test_circle_add_area_success():
    circle = Circle(2)  # Площадь: 4 * pi
    rectangle = Rectangle(3, 4)
    expected_area = (4 * math.pi) + 12
    assert circle.add_area(rectangle) == expected_area


def test_circle_add_area_invalid_object_raises_error():
    circle = Circle(5)
    with pytest.raises(ValueError, match="Can add only another figure"):
        circle.add_area("Not a figure string")
