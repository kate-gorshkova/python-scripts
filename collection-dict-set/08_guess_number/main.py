import random

max_number = int(input("Введите максимальное число: "))

num_set = set(list(range(1, max_number + 1)))
print(num_set)

magic_num = random.randint(1, max_number)
print(magic_num)

while True:
    print("Нужное число есть среди вот этих чисел:", end=" ")
    numbers = input()

    if numbers == "Помогите!":
        print("Артём мог загадать следующие числа:", num_set)
        break

    else:
        numbers = numbers.split()
        numbers_set = set([int(num) for num in numbers])

        if magic_num in numbers_set:
            print("Ответ Артёма: Да")
            num_set = numbers_set

            if len(num_set) == 1:
                print("Ты угадал!")
                break
        else:
            print("Ответ Артёма: Нет")
            num_set = num_set - numbers_set

# зачёт!
