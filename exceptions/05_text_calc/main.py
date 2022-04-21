def elem_count(any_line):
    return len(any_line.split()) == 3


def digit(number1, number2):
    if number1.isdigit() and number2.isdigit():
        return True
    return False


def check_sym(any_sym):
    sym_list = ["+", "-", "*", "/", "//", "%", "**"]
    if any_sym in sym_list:
        return True
    return False


def operation(number1, any_sym, number2):
    if any_sym == "+":
        return number1 + number2
    elif any_sym == "-":
        return number1 - number2
    elif any_sym == "*":
        return number1 * number2
    elif any_sym == "/":
        return number1 / number2
    elif any_sym == "//":
        return number1 // number2
    elif any_sym == "%":
        return number1 % number2
    elif any_sym == "**":
        return number1 ** number2


def result(any_line):
    num1, sym, num2 = any_line.split()
    if not elem_count(any_line):
        raise ValueError
    elif not digit(num1, num2):
        raise ValueError
    elif not check_sym(sym):
        raise SyntaxError
    else:
        return operation(int(num1), sym, int(num2))


total_res = 0
with open("calc.txt", "r") as calc_file:
    num_line = 0
    for i_line in calc_file:
        num_line += 1
        try:
            total_res += result(i_line)
        except (SyntaxError, ValueError):
            print("Ошибка в строке: {}".format(num_line))
print(total_res)

# зачёт!
