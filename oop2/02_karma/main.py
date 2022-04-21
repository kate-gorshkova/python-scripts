import random


class KillError(Exception):
    def __str__(self):
        return "KillError"


class DrunkError(Exception):
    def __str__(self):
        return "KillError"


class CarCrashError(Exception):
    def __str__(self):
        return "CarCrashError"


class GluttonyError(Exception):
    def __str__(self):
        return "GluttonyError"


class DepressionError(Exception):
    def __str__(self):
        return "DepressionError"


def one_day():
    num = random.randint(1, 10)
    problem = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
    if num == 10:
        raise random.choice(problem)

    return random.randint(1, 7)


total_karma = 0
while total_karma < 500:
    try:
        karma = one_day()
        total_karma += karma
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as err:
        with open("karma.log", "a", encoding="utf-8") as karma_file:
            karma_file.write("Ошибка {}\n".format(err))

print("Карма достигла уровня константы")

# зачёт!
