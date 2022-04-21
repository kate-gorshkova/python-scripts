import os
from collections.abc import Iterable


def gen_files_path(desired_folder: str, abs_path: str = os.path.join(os.path.abspath(os.sep))) -> Iterable[str]:
    for i_folder in os.listdir(abs_path):
        my_path = os.path.join(abs_path, i_folder)
        if os.path.isdir(my_path):
            if my_path.endswith(desired_folder):
                for i_file in os.listdir(my_path):
                    yield i_file
            else:
                yield from gen_files_path(desired_folder, my_path)


path = os.path.abspath(os.path.join("..", "..", "Module26"))
gen = gen_files_path("checked_folder", path)
for i in gen:
    print(i)

# Module26
# 06_linked_list
# checked_folder

# зачёт!
