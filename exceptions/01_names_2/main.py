sym_count = 0
num_string = 0

try:
    with open("people.txt", "r") as people_file:
        for i_name in people_file:
            num_string += 1
            try:
                if len(i_name.strip("\n")) > 3:
                    sym_count += len(i_name) - 1
                else:
                    raise ValueError
            except ValueError:
                print("Ошибка в {} строке".format(num_string))
                with open("errors.log", "a") as errors_file:
                    errors_file.write("Ошибка в {} строке {}".format(num_string, "\n"))
finally:
    print(sym_count)

# зачёт!
