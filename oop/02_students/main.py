class Student:
    def __init__(self, name_surname, group, progress):
        self.name_surname = name_surname
        self.group = group
        self.progress = progress

    def average_score(self):
        return sum(self.progress) / len(self.progress)


my_list = [
    Student("Ivan Ivanov", 3409, [2, 3, 4, 5, 5]),
    Student("Petr Petrov", 3404, [3, 3, 5, 5, 5]),
    Student("Vasily Vasiliev", 3408, [2, 3, 4, 3, 5]),
    Student("Alina Ivanova", 3401, [4, 5, 5, 5, 5]),
    Student("Irina Petrova", 3409, [3, 3, 4, 5, 5]),
    Student("Marina Marinina", 3409, [5, 3, 4, 4, 2]),
    Student("Olga Olgina", 3412, [3, 3, 4, 4, 5]),
    Student("Roman Romanov", 3414, [5, 5, 5, 5, 5]),
    Student("Mihail Mihailov", 3410, [3, 2, 3, 4, 5]),
    Student("Elena Vasilieva", 3412, [4, 5, 5, 4, 5])
]

my_list.sort(key=lambda elem: elem.average_score(), reverse=True)
for item in my_list:
    print("{}  {}  {}".format(item.name_surname, item.group, item.average_score()))
