import math


class Circle:
    def __init__(self, r, x=0, y=0):
        self.r = r
        self.x = x
        self.y = y

    def area_circle(self):
        return math.pi * self.r ** 2

    def perimeter_circle(self):
        return 2 * math.pi * self.r

    def increase_circle(self, k):
        area = math.pi * (self.r * k) ** 2
        perimeter = 2 * math.pi * self.r * k
        return area, perimeter

    def cross_circle(self, circle):
        if self.r + circle.r >= math.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2):
            print("Окружности пересекаются")
        else:
            print("Окружности не пересекаются")


circle1 = Circle(3, 3, 1)
circle2 = Circle(5, 1, 2)
print("Площадь 1 окружности: {}".format(circle1.area_circle()))
print("Периметр 1 окружности: {}\n".format(circle1.perimeter_circle()))

print("Площадь 2 окружности: {}".format(circle2.area_circle()))
print("Периметр 2 окружности: {}\n".format(circle2.perimeter_circle()))

print("Увелиение 1 окружности в 2 раза")
s, p = circle1.increase_circle(2)
print("Площадь 1 окружности: {}".format(s))
print("Периметр 1 окружности: {}\n".format(p))

print("Увелиение 2 окружности в 3 раза")
s, p = circle2.increase_circle(3)
print("Площадь 1 окружности: {}".format(s))
print("Периметр 1 окружности: {}\n".format(p))
