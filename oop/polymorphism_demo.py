import math

class Shape:
    def area(self):
        """Base method to calculate area, must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle (length × width)."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle (π × r²)."""
        return math.pi * (self.radius ** 2)
