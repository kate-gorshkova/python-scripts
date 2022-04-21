class Potato:
    states = {0: "Отсутствует", 1: "Росток", 2: "Зелёная", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print("Картошка {} сейчас {}".format(self.index, Potato.states[self.state]))


class PotatoGarden:

    def __init__(self, new_gardener):
        self.potatoes = []
        self.host = new_gardener

    def check_ripe(self):
        if len(self.potatoes) == 0:
            return True

    def add_potato(self, *args):
        for i_potato in args:
            self.potatoes.append(i_potato)

    def grow_all(self):
        print("Картошка прорастает!")
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if i_potato.is_ripe():
                self.host.remove_potatoes(i_potato)
            else:
                self.host.water()

    def potato_removed(self, ripe_potato):
        self.potatoes.remove(ripe_potato)


class Gardener:

    def __init__(self, name):
        self.name = name
        self.garden_beds = []

    def add_beds(self, *args):
        for bed in args:
            self.garden_beds.append(bed)

    def water(self):
        print("{} поливает картошку.".format(self.name))
        for bed in self.garden_beds:
            bed.grow_all()

    def remove_potatoes(self, ripe_potato):
        print("{} убирает картошку.".format(self.name))
        for bed in self.garden_beds:
            bed.potato_removed(ripe_potato)
        print("Картошка убрана")


my_gardener = Gardener("Джек")
my_garden = PotatoGarden(my_gardener)
for elem in range(1, 6):
    new_potato = Potato(elem)
    my_garden.add_potato(new_potato)
my_gardener.add_beds(my_garden)

while True:
    my_garden.are_all_ripe()
    if my_garden.check_ripe():
        break

print("\nУрожай собран")
