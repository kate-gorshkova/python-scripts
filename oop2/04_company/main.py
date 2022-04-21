class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name


class Employee(Person):
    def calculation_salary(self):
        pass


class Manager(Employee):
    def calculation_salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.sales_volume = sales_volume

    def calculation_salary(self):
        return 5000 + self.sales_volume / 100 * 5


class Worker(Employee):
    def __init__(self, name, surname, age, count_hours):
        super().__init__(name, surname, age)
        self.count_hours = count_hours

    def calculation_salary(self):
        return 100 + self.count_hours


employee_list = [
    Manager(name="Ann", surname="Moroz", age=26),
    Manager(name="Boris", surname="Ivanov", age=37),
    Manager(name="Petr", surname="Sidorov", age=29),
    Agent(name="Elena", surname="Novikova", age=23, sales_volume=50000),
    Agent(name="Mariya", surname="Petrova", age=31, sales_volume=100000),
    Agent(name="Larisa", surname="Kalinina", age=46, sales_volume=78000),
    Worker(name="Sergey", surname="Chugunov", age=40, count_hours=160),
    Worker(name="Konstantin", surname="Emelianenko", age=38, count_hours=180),
    Worker(name="Pavel", surname="Nikolaev", age=36, count_hours=195),
]

for employee in employee_list:
    print("{} earned {}".format(employee.get_name(), employee.calculation_salary()))

# зачёт!
