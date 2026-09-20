import pytest
from src.square import Square


def test_square_creation_success():
    square = Square(4)
    assert square.side_a == 4


def test_square_perimeter():
    square = Square(4)
    assert square.perimeter == 16


def test_square_area():
    square = Square(4)
    assert square.area == 16


@pytest.mark.parametrize("invalid_side", [0, -3])
def test_square_invalid_side_raises_error(invalid_side):
    with pytest.raises(ValueError, match="All sides must be greater than 0"):
        Square(invalid_side)
