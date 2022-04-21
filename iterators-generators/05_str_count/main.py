import os
from collections.abc import Iterable


def gen_str_count(folder: str) -> Iterable[int]:
    path_folder = os.path.abspath(folder)
    files_list = os.listdir(path_folder)
    for file in files_list:
        if file.endswith(".py"):
            count_str = 0
            with open(os.path.join(path_folder, file), "r") as py_file:
                for i_line in py_file:
                    if i_line.startswith("#") or i_line == "\n":
                        continue
                    else:
                        count_str += 1
            yield count_str


my_folder = "folder_for_check"
summa = 0
for i in gen_str_count(my_folder):
    summa += i
print(summa)

# зачёт!
