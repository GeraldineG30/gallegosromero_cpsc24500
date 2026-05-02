from shape import Shape

class Rectabgle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height cannot be negative")
        self._width = float(width)
        self._height = float(height)
    
    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def describe(self):
        return f"Rectangle {self._width} x {self._height}"
        