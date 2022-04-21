from abc import ABC, abstractmethod
import math


class Figure(ABC):
    """
    Абстрактный базовый класс Фигура

    Args ana attrs:
        length (int): 1-ый размерный параметр фиругы
        height (int): 2-ый размерный параметр фиругы
    """

    def __init__(self, length: int, height: int) -> None:
        self.length = length
        self.height = height

    @abstractmethod
    def area(self) -> None:
        pass

    @abstractmethod
    def perimeter(self) -> None:
        pass


class Square(Figure):
    def __init__(self, length: int):
        super().__init__(length, length)

    def area(self) -> int:
        return self.length * self.height

    def perimeter(self) -> int:
        return self.length * 4


class Triangle(Figure):
    def area(self) -> float:
        return 1 / 2 * self.length * self.height

    def perimeter(self) -> float:
        hypotenuse = math.sqrt((self.length / 2) ** 2 + self.height ** 2)
        return 2 * hypotenuse + self.height


class SurfaceAreaMixin:
    def sum_area(self) -> float:
        return sum([i_area.area() for i_area in self.list_figure])


class Cube(SurfaceAreaMixin):
    def __init__(self, length):
        self.list_figure = [
            Square(length),
            Square(length),
            Square(length),
            Square(length),
            Square(length),
            Square(length)
        ]

    def get_list_area(self):
        return [i_area.area() for i_area in self.list_figure]


class Pyramid(SurfaceAreaMixin):
    def __init__(self, length, height):
        self.list_figure = [
            Square(length),
            Triangle(length, height),
            Triangle(length, height),
            Triangle(length, height),
            Triangle(length, height)
        ]

    def get_list_area(self):
        return [i_area.area() for i_area in self.list_figure]


sq_1 = Square(length=2)
print(sq_1.area())
print(sq_1.perimeter())
tr_1 = Triangle(length=4, height=6)
print(tr_1.area())
print(tr_1.perimeter())
cube_1 = Cube(length=3)
cube_1_list_area = cube_1.get_list_area()
print(cube_1.sum_area())
pyramid_1 = Pyramid(length=5, height=7)
pyramid_1_list_area = pyramid_1.get_list_area()
print(pyramid_1.sum_area())

# зачёт!
