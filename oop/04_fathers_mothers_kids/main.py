import random


class Parent:
    def __init__(self, name, children_list):
        self.name = name
        self.children_list = children_list

    def age(self):
        age_list = [i_child.age_ch for i_child in self.children_list]
        return random.randint(16, 45) + max(age_list)

    def info(self):
        name_list = [i_child.name_ch for i_child in self.children_list]
        print("Имя: {}\nВозраст: {}\nСписок детей: {}\n".format(self.name, self.age(), name_list))

    def calm(self, child):
        if child in self.children_list:
            child.state_calm += 10

    def feed(self, child):
        if child in self.children_list:
            child.state_feed += 10


class Child:
    def __init__(self, name_ch, age_ch, state_calm, state_feed):
        self.name_ch = name_ch
        self.age_ch = age_ch
        self.state_calm = state_calm
        self.state_feed = state_feed

    def info_ch(self):
        print(
            "Имя: {}\nВозраст: {}\nУровень спокойствия: {}\nУровень голода: {}\n".format(
                self.name_ch, self.age_ch, self.state_calm, self.state_feed
            )
        )


child_1 = Child("Вася", 17, random.randint(0, 100), random.randint(0, 100))
child_2 = Child("Петя", 20, random.randint(0, 100), random.randint(0, 100))

my_children_list = [child_1, child_2]

parent_1 = Parent("Мария", my_children_list)
parent_1.info()

for my_child in my_children_list:
    my_child.info_ch()

print("-" * 25)

for my_child in my_children_list:
    while my_child.state_calm < 50:
        parent_1.calm(my_child)

    while my_child.state_feed < 50:
        parent_1.feed(my_child)

    my_child.info_ch()
