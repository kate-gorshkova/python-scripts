def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


num_pos = int(input("Введите позицию числа в ряде Фибоначчи: "))
print(fibonacci(num_pos))

# зачёт!
