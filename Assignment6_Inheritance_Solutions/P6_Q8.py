# Q8. Polymorphism - Shape Area

import math


class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        raise NotImplementedError("Subclasses must implement area().")


class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length ** 2


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return math.pi * self.length ** 2


def main():
    square_side = float(input("Enter square side: "))
    circle_radius = float(input("Enter circle radius: "))

    shapes = [Square(square_side), Circle(circle_radius)]
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
