import re

num_list = ['9999999999', '999999-999', '99999x9999']

for i_num, num in enumerate(num_list, start=1):
    if re.findall(r"[8-9]\d{9}", num):
        print("{} номер: всё в порядке".format(i_num))
    else:
        print("{} номер: не подходит".format(i_num))

# зачёт!
