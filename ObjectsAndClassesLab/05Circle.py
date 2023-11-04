class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        self.circumference = Circle.__pi * self.diameter
        return self.circumference

    def calculate_area(self):
        self.area = Circle.__pi * ((self.diameter / 2) ** 2)
        return self.area

    def calculate_area_of_sector(self, angle):
        self.angle = angle
        self.area_of_sector = (self.angle / 360) * Circle.__pi * ((self.diameter / 2) ** 2)
        return self.area_of_sector


diameter = float(input())
angle = float(input())

circle = Circle(diameter)

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
