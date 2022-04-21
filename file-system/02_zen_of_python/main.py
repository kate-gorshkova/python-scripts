zen_python = open("zen.txt", "r")

my_list = zen_python.readlines()[::-1]
for i_line in my_list:
    print(i_line, end="")

zen_python.close()

# зачёт!
