import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

circle1 = Circle(5)
print("Area of the circle:", circle1.area())
print("Perimeter of the circle:", circle1.perimeter())
