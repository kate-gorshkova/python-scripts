import random


class Man:
    def __init__(self, name, home, satiety=50):
        self.name = name
        if isinstance(home, Home):
            self.home = home
        self.satiety = satiety

    def eat(self):
        if self.home.food > 0:
            self.satiety += 10
            self.home.food -= 10

    def work(self):
        self.satiety -= 10
        self.home.money += 10

    def play(self):
        self.satiety -= 10

    def shop(self):
        if self.home.money > 0:
            self.home.food += 10
            self.home.money -= 10

    def print_info(self):
        print("Уровень сытости у {}: {}".format(self.name, self.satiety))


class Home:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def print_info(self):
        print("Еды в доме: {}\nДенег в доме: {}".format(self.food, self.money))


def live_day(man):
    any_num = random.randint(1, 6)
    if man.satiety < 20:
        man.eat()
    elif man.home.food < 10:
        man.shop()
    elif man.home.money < 50:
        man.work()
    elif any_num == 1:
        man.work()
    elif any_num == 2:
        man.eat()
    else:
        man.play()


my_home = Home()
man_1 = Man("Roman", my_home)
man_2 = Man("Mariya", my_home)
for i_day in range(1, 366):
    if man_1.satiety > 0 and man_2.satiety > 0:
        live_day(man_1)
        live_day(man_2)
    else:
        print("Кто-то покинул этот мир =( в {} день".format(i_day))
        break

man_1.print_info()
man_2.print_info()
my_home.print_info()
