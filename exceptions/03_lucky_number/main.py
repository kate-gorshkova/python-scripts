import random

summa = 0
problem = [ValueError, TypeError, ZeroDivisionError, IndexError, NameError]

try:
    with open("num.txt", "a") as num_file:
        while summa < 777:
            num = int(input("Введите число: "))
            number = random.randint(1, 13)
            if number == 13:
                raise random.choice(problem)
            num_file.write(f"{num}\n")
            summa += num
    print("Сумма чисел:", summa)
except (ValueError, TypeError, ZeroDivisionError, IndexError, NameError) as err:
    err = err.__class__.__name__
    print("Ошибка", err)

# зачёт!
