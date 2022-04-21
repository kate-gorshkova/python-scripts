import math


class MyMath:
    def __init__(self):
        pass

    @classmethod
    def circle_len(cls, radius: int) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_vol(cls, length: int) -> float:
        return length ** 3

    @classmethod
    def sphere_sq(cls, radius: int) -> float:
        return 4 * math.pi * radius ** 2

    @classmethod
    def cone_vol(cls, height: int, radius: int) -> float:
        return height / 3 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_vol(length=3)
res_4 = MyMath.sphere_sq(radius=4)
res_5 = MyMath.cone_vol(height=5, radius=3)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)

# зачёт!
