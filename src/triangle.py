from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Triangle with such sides cannot exist")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        half_p = self.perimeter / 2.0
        return pow((half_p * (half_p - self.side_a) * (half_p - self.side_b) * (half_p - self.side_c)), 0.5)
