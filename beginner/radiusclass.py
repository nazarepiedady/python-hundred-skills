class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * 3.14


circle = Circle(2)

print(circle.area())
