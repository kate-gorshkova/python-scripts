def summa(*args):
    result = 0
    for arg in args:
        if isinstance(arg, int):
            result += arg
        else:
            if isinstance(arg, list or tuple):
                for i_arg in arg:
                    result += summa(i_arg)
    return result


print(summa([[1, 2, [3]], [1], 3]))
print(summa(1, 2, 3, 4, 5))

# зачёт!
