import os


def dirs(path):
    file_size = 0
    any_file_count = 0
    for i_elem in os.listdir(path):
        my_path = os.path.join(path, i_elem)
        if os.path.isdir(my_path):

            for i_file in os.listdir(my_path):
                new_path = os.path.join(my_path, i_file)
                if os.path.isfile(new_path):
                    any_file_count += 1
                    file_size += os.path.getsize(new_path)

    return file_size, any_file_count


abs_path = os.path.abspath(os.path.join("..", "..", "Module22"))
print(abs_path)

size, file_count = dirs(abs_path)

print("Размер каталога (в Кб): {}".format(size / 1024))
print("Количество подкаталогов: {}".format(len(os.listdir(abs_path))))
print("Количество файлов: {}".format(file_count))

# зачёт!
