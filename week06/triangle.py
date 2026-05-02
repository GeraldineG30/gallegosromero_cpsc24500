import math
from shape import Shape

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides must be positive")
        
        if (side_a + side_b <= side_c or
            side_a + side_c <= side_b or
            side_c + side_b <= side_a):
            raise ValueError("Triangle inequality! the sum of two sides is less or equal to the third")
        
        self._side_a = float(side_a)
        self._side_b = float(side_b)
        self._side_c = float(side_c)

    def area(self):
        s = (self._side_a + self._side_b + self._side_c) / 2
        return math.sqrt(s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c))
    
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c
    
    def describe(self):
        return f"Triangle with sides {self._side_a}, {self._side_b}, {self._side_c}"
    