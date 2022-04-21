import random


class Home:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0

    def pollute(self):
        self.dirt += 5


class Info:
    def __init__(self):
        self.total_food = 0
        self.total_cat_food = 0
        self.total_money = 0
        self.total_coat = 0

    def print_info(self):
        print("Заработали денег: {}\nСъели еды: {}\nКот съел: {}\nКуплено шуб: {}\n".format(
            self.total_money,
            self.total_food,
            self.total_cat_food,
            self.total_coat
        ))


class Person:
    def __init__(self, name, my_home=None, my_info=None):
        self.name = name
        self.satiety = 30
        self.happy = 100
        self.my_home = my_home
        self.my_info = my_info

    def move_into_house(self, my_home, my_info):
        if isinstance(my_home, Home) and isinstance(my_info, Info):
            self.my_home = Home
            self.my_info = Info

    def pet_cat(self):
        self.happy += 5
        self.satiety -= 10

    def eat(self):
        self.my_home.food -= 30
        self.my_info.total_food += 30
        self.satiety += 30

    def live_day(self):
        if self.my_home.dirt > 90:
            self.happy -= 10
        if self.satiety < 0:
            print("{} умер(ла) от голода".format(self.name))
            return False
        if self.happy < 10:
            print("{} умер(ла) от депрессии".format(self.name))
            return False
        return True


class Husband(Person):
    def play(self):
        self.happy += 20
        self.satiety -= 10

    def work(self):
        self.my_home.money += 150
        self.satiety -= 10
        self.my_info.total_money += 150

    def live_day(self):
        if super().live_day():
            if self.satiety >= 40 and self.happy >= 40 and self.my_home.money < 600:
                self.work()
            elif self.my_home.food > 20 and self.satiety < self.happy < 600:
                self.eat()
            elif self.happy < self.satiety:
                self.play()
            else:
                rand_num = random.randint(1, 2)
                if rand_num == 1 and self.my_home.food > 20:
                    self.eat()
                else:
                    self.pet_cat()


class Wife(Person):
    def buy_food(self):
        if self.my_home.money >= 40:
            self.my_home.food += 40
            self.my_home.money -= 40
            self.satiety -= 10
        if self.my_home.cat_food <= 20 < self.my_home.money >= 20:
            self.buy_cat_food()
        else:
            self.clean()

    def buy_cat_food(self):
        if self.my_home.money >= 20:
            self.my_home.cat_food += 20
            self.my_home.money -= 20
            self.satiety -= 10
        else:
            if self.happy < 20:
                self.pet_cat()
            else:
                self.clean()

    def buy_coat(self):
        if self.my_home.money > 550:
            self.my_home.money -= 350
            self.happy += 60
            self.satiety -= 10
            self.my_info.total_coat += 1
        else:
            self.pet_cat()

    def clean(self):
        self.my_home.dirt -= 80
        self.satiety -= 10

    def live_day(self):
        if super().live_day():
            if self.my_home.food < 40:
                self.buy_food()
            elif self.satiety > 30 and self.happy > 30 and self.my_home.cat_food < 10:
                if self.my_home.food < 50:
                    self.buy_food()
                elif self.my_home.cat_food < 10:
                    self.buy_cat_food()
                else:
                    self.pet_cat()
            elif self.satiety > self.happy:
                self.buy_coat()
            elif self.satiety < self.happy and self.my_home.food > 20:
                self.eat()
            else:
                self.clean()


class Cat:
    def __init__(self, name, my_home=None, my_info=None):
        self.name = name
        self.satiety = 30
        self.my_home = my_home
        self.my_info = my_info

    def move_into_house(self, my_home, my_info):
        if isinstance(my_home, Home) and isinstance(my_info, Info):
            self.my_home = Home
            self.my_info = Info

    def eat(self):
        if self.my_home.cat_food >= 10:
            self.satiety += 10 * 2
            self.my_home.cat_food -= 10
            self.my_info.total_cat_food += 10

    def sleep(self):
        self.satiety -= 10

    def tear_wallpaper(self):
        self.my_home.dirt += 5
        self.satiety -= 10

    def live_day(self):
        if self.is_dead():
            if self.satiety < 20:
                self.eat()
            else:
                rand_num = random.randint(1, 2)
                if rand_num == 1:
                    self.sleep()
                else:
                    self.tear_wallpaper()
        else:
            print("{} умер(ла) от голода".format(cat.name))

    def is_dead(self):
        if self.satiety < 0:
            return False
        return True


home = Home()
info = Info()
husband = Husband(name="Petr", my_home=home, my_info=info)
wife = Wife(name="Ann", my_home=home, my_info=info)
cat = Cat(name="Varsik", my_home=home, my_info=info)

total_day = 0
for day in range(1, 366):
    total_day = day

    home.pollute()
    husband.live_day()
    wife.live_day()
    cat.live_day()

print("Информация на {} день".format(total_day))
info.print_info()

# зачёт!
