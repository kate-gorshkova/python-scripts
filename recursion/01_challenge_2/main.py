def function(n):
    if n > 0:
        function(n - 1)
        print(n)


num = int(input("Введите число: "))
function(num)

# зачёт!
