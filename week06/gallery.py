
class Gallery:
    def __init__(self, name):
        self._name = name
        self._shapes = []
    
    def add_shape(self, shape):
        self._shapes.append(shape)

    def total_area(self):
        if self._shapes:
            return sum(shape.area() for shape in self._shapes)
        else:
            0.0
    
    def largest_shape(self):
        if not self._shapes:
            return None
        largest = self._shapes [0]
        for s in self._shapes[1:]:
            if s.area() > largest.area():
                largest = s
        return largest
    
    def display_all(self):
        print(f"\n Gallery: {self._name}")
        print("\n" + "-" * 55 )
        for shape in self._shapes:
            print(f"    {shape.describe()}")
            print(f"    Area: {shape.area():.2f}")
            print(f"    Perimeter: {shape.perimeter():.2f}\n")
        print("-" * 55 + "\n")