class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.k = 1 / 1000

    def tax(self):
        return self.worth * self.k


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.k = 1 / 200

    def tax(self):
        return self.worth * self.k


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.k = 1 / 500

    def tax(self):
        return self.worth * self.k


def all_tax(*args):
    total = 0
    for i_tax in args:
        total += i_tax
    return total


money = int(input("Введите кол-во денег: "))
apartment_cost = int(input("Введите стоимость квартиры: "))
car_cost = int(input("Введите стоимость машины: "))
country_house_cost = int(input("Введите стоимость дачи: "))

apartment_tax = Apartment(apartment_cost).tax()
car_tax = Car(car_cost).tax()
country_house_tax = CountryHouse(country_house_cost).tax()
total_tax = all_tax(apartment_tax, car_tax, country_house_tax)

if money > total_tax:
    print("Налог на квартиру составляет:", apartment_tax)
    print("Налог на машину составляет:", car_tax)
    print("Налог на дачу составляет:", country_house_tax)
else:
    print("Недостающая сумма:", total_tax - money)

# зачёт!
