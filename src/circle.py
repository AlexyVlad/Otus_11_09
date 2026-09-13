import math

from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self._validate_positive_sides(radius)
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return self.radius * self.radius * math.pi
