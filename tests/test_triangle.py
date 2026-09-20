import pytest
from src.triangle import Triangle


def test_triangle_creation_success():
    triangle = Triangle(3, 4, 5)
    assert triangle.side_a == 3
    assert triangle.side_b == 4
    assert triangle.side_c == 5


def test_triangle_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter == 12


def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert triangle.area == pytest.approx(6.0)


@pytest.mark.parametrize("side_a, side_b, side_c", [
    (1, 2, 3),
    (1, 1, 10),
    (10, 1, 1),
    (1, 10, 1)
])
def test_triangle_invalid_sides_raises_error(side_a, side_b, side_c):
    with pytest.raises(ValueError, match="Triangle with such sides cannot exist"):
        Triangle(side_a, side_b, side_c)
