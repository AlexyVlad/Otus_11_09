from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @staticmethod
    def _validate_positive_sides(*sides):
        for side in sides:
            if side <= 0:
                raise ValueError("All sides must be greater than 0")

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Can add only another figure")
        return self.area + other_figure.area
