#activity2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Circle :{3.14 * self.radius ** 2}"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"Rectangle :{self.width * self.height}"

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return f"Triangle : {0.5 * self.base * self.height}"

def print_area(shape):
    print(f"Area {shape.area()}")

shapes = [
    Circle(3),
    Rectangle(4, 5),
    Triangle(6, 2)
]

for shape in shapes:
    print_area(shape)

