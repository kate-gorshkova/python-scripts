import math


class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, r):
        self.x += r * math.cos(math.radians(self.angle))
        self.y += r * math.sin(math.radians(self.angle))

    def print_info(self):
        print("Координата x: {}\nКоордината y: {}\nУгол: {}\n".format(
            self.x,
            self.y,
            self.angle
        ))

    def set_angle(self, new_angle):
        self.angle = new_angle


class Bus(Car):
    def __init__(self, x, y, angle, passengers_count=0, money=0):
        super().__init__(x, y, angle)
        self.passengers_count = passengers_count
        self.money = money

    def enter(self, n):
        if self.passengers_count >= 0:
            self.passengers_count += n

    def exit(self, n):
        if n >= self.passengers_count:
            self.passengers_count = 0
        else:
            self.passengers_count -= n

    def move(self, r):
        super().move(r)
        self.money += r * self.passengers_count

    def print_info(self):
        print("Координата x: {}\nКоордината y: {}\nУгол: {}\nКол-во пассажиров: {}\nКол-во денег: {}\n".format(
            self.x,
            self.y,
            self.angle,
            self.passengers_count,
            self.money
        ))


def trip(any_exit, any_enter, any_angle, dist):
    bus.exit(any_exit)
    bus.enter(any_enter)
    bus.set_angle(any_angle)
    bus.move(dist)


bus = Bus(0, 0, 90)
bus.enter(40)
bus.move(80)

trip(10, 2, 0, 20)
trip(20, 5, 60, 40)

bus.print_info()

# зачёт!
