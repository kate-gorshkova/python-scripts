guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print("Сейчас на вечеринке", len(guests), "человек:", guests)
    print("Гость пришёл или ушёл?", end=" ")
    come_away = input()
    if come_away == "Пора спать":
        break
    guest_name = input("Имя гостя: ")
    if len(guests) < 6 and come_away == "пришёл" and guest_name not in guests:
        print("Привет,", guest_name + "!")
        guests.append(guest_name)
    elif come_away == "ушёл" and guest_name in guests:
        print("Пока,", guest_name + "!")
        guests.remove(guest_name)
    elif len(guests) >= 6 and come_away == "пришёл":
        print("Прости,", guest_name + ",", "но мест нет.")
print("Вечеринка закончилась, все легли спать.")

# зачёт!
