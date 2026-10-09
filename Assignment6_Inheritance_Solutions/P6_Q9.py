# Q9. Interface - Shape, Circle and Triangle

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Every concrete shape must implement this method."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def main():
    radius = float(input("Enter circle radius: "))
    base = float(input("Enter triangle base: "))
    height = float(input("Enter triangle height: "))

    shapes = [Circle(radius), Triangle(base, height)]
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
