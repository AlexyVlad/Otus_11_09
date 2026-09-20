import pytest
from src.rectangle import Rectangle


def test_rectangle_creation_success():
    rect = Rectangle(4, 6)
    assert rect.side_a == 4
    assert rect.side_b == 6


def test_rectangle_perimeter():
    rect = Rectangle(3, 5)
    assert rect.perimeter == 16


def test_rectangle_area():
    rect = Rectangle(3, 5)
    assert rect.area == 15


@pytest.mark.parametrize("side_a, side_b", [
    (0, 5),
    (5, 0),
    (-2, 4),
    (4, -2),
    (0, 0)
])
def test_rectangle_invalid_sides_raises_error(side_a, side_b):
    with pytest.raises(ValueError, match="All sides must be greater than 0"):
        Rectangle(side_a, side_b)


def test_rectangle_add_area_success():
    rect1 = Rectangle(2, 3)
    rect2 = Rectangle(4, 5)
    assert rect1.add_area(rect2) == 26
