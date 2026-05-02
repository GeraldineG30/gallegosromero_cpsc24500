import math
from shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0 :
            raise ValueError("Radius must be positive")
        self._radius = float(radius)

    def area(self):
        return math.pi * self._radius ** 2

    def perimeter(self):
        return 2 * math.pi * self._radius
    
    def describe(self):
        return f"Circle with radius {self._radius}"