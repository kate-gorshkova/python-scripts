file_name = input("Название файла: ")
symbol = "@№$%^&*()"
flag = True

if not (file_name.endswith(".txt") or file_name.endswith(".docx")):
    flag = False
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    for sym in symbol:
        if file_name.startswith(sym):
            flag = False
            print("Ошибка: название начинается на один из специальных символов")
            break
if flag:
    print("Файл назван верно.")

# зачёт!
