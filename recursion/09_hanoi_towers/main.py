def move(disk, start, finish):
    if disk == 1:
        print("Переложить диск 1 со стержня номер {num1} на стержень номер {num2}".format(num1=start, num2=finish))
    else:
        temp = 6 - start - finish
        move(disk - 1, start, temp)
        print("Переложить диск {num1} со стержня номер {num2} на стержень номер {num3}".format(num1=disk,
                                                                                               num2=start,
                                                                                               num3=finish))
        move(disk - 1, temp, finish)


n = int(input("Введите количество дисков: "))

move(n, 1, 3)

# зачёт!