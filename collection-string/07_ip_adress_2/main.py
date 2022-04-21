def check_address(my_address):
    if my_address.count(".") == 3:
        for digit in my_address.split("."):
            if not digit.isdigit():
                print(digit, "- не целое число")
                return False
            elif int(digit) > 255:
                print(int(digit), "превышает 255")
                return False
    else:
        print("Адрес - это четыре числа, разделённые точками")
        return False
    return True


ip_address = input("Введите IP: ")
if check_address(ip_address):
    print("IP-адрес корректен")

# зачёт!
