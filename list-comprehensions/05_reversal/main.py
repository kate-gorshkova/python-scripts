stroke = input("Введите строку: ")
stroke_copy = stroke
number1 = stroke.index("h")
number2 = len(stroke) - stroke[::-1].index("h") - 2
part_1 = stroke[:stroke.index("h") + 1]
part_2 = stroke[number2:number1:-1]
part_3 = stroke[len(stroke) - stroke[::-1].index("h") - 1:]
print(part_1 + part_2 + part_3)

# зачёт!
