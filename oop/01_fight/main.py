import random


class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def hit(self, enemy):
        enemy.health -= 20
        print("{} has attacked".format(self.name))
        print("{} has {} health\n".format(enemy.name, enemy.health))


warrior1 = Warrior("Warrior1", 100)
warrior2 = Warrior("Warrior2", 100)


while warrior1.health > 0 and warrior2.health > 0:
    question = int(input("Enter 1 to let some warrior attack: "))
    if question == 1:
        j = random.randint(1, 2)
        if j == 1:
            warrior1.hit(warrior2)
        else:
            warrior2.hit(warrior1)
    else:
        print("Wrong input.")

if warrior1.health != 0:
    print("{} has won".format(warrior1.name))
else:
    print("{} has won".format(warrior2.name))
