N = int(input("Кол-во клеток: "))
cell_list = []
bad_cell = ""
for cell in range(1, N + 1):
    print("Эффективность", cell, "клетки:", end=" ")
    efficiency = int(input())
    cell_list.append(efficiency)

    if cell_list[cell - 1] < cell:
        bad_cell += str(efficiency) + " "
print("Неподходящие значения:", bad_cell)

# зачёт!
