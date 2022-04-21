import random


class Deck:
    def __init__(self):
        self.deck = {
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "jack": 10,
            "queen": 10,
            "king": 10,
            "ace": 11,
        }

    def get_card(self):
        key_card = random.choice([i_key for i_key in self.deck.keys()])
        return self.deck.pop(key_card)


class Player:
    def __init__(self, name):
        self.name = name
        self.cards_list = []

    def get_points(self):
        if sum(self.cards_list) >= 21 and 11 in self.cards_list:
            return sum(self.cards_list) - 10
        else:
            return sum(self.cards_list)

    def set_card(self, any_card):
        self.cards_list.append(any_card)

    def get_count_cards(self):
        return len(self.cards_list)


while True:
    print("\nСтарт игры")
    cards = Deck()
    p = Player("Roman")
    d = Player("Dealer")

    for i in range(4):
        if p.get_count_cards() < 2:
            p.set_card(cards.get_card())
        else:
            d.set_card(cards.get_card())

    print("Кол-во очков:", p.get_points())

    print("\nВзять карту - 1; остановиться - 2")
    action = int(input())

    while action == 1:
        p.set_card(cards.get_card())
        print("Кол-во очков:", p.get_points())
        print("\nВзять карту - 1; остановиться - 2")
        action = int(input())

    print("Счёт")
    print("{}: {}".format(p.name, p.get_points()))
    print("{}: {}".format(d.name, d.get_points()))
    win = ""
    if d.get_points() < p.get_points() <= 21:
        win = p.name
    elif p.get_points() < d.get_points() <= 21:
        win = d.name
    elif p.get_points() == d.get_points():
        print("Ничья")
        continue
    else:
        win = d.name
    print("Победитель:", win)
    continue
