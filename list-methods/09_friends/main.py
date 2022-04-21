def check(receipt, count, f_list):
    while True:
        print()
        print(receipt, "расписка")
        print("Кому дали в долг:", end=" ")
        your_debtor = int(input())
        print("От кого получили в долг:", end=" ")
        your_lender = int(input())
        print("Сколько получили в долг:", end=" ")
        duty = int(input())
        if (your_debtor <= count and your_lender <= count) and your_debtor != your_lender:
            f_list[your_debtor - 1] -= duty
            f_list[your_lender - 1] += duty
            break
        else:
            pass


N = int(input("Кол-во друзей: "))
K = int(input("Долговых расписок: "))
friend_list = []
for _ in range(N):
    friend_list.append(0)

for rec in range(1, K + 1):
    check(rec, N, friend_list)
print("\nБаланс друзей:")
for friend in range(1, len(friend_list) + 1):
    print(str(friend) + ":", friend_list[friend - 1])

# зачёт!
