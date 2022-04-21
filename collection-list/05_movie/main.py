films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
count_films = int(input("Кол-во фильмов, которое хотите добавить в свой список: "))
favorite_film_list = []
for _ in range(count_films):
    favorite_film = input("Введите название фильма: ")
    error = 0
    for film in films:
        if favorite_film == film:
            favorite_film_list.append(favorite_film)
            break
        else:
            error += 1
    if error == 9:
        print("Ошибка.")

print("Список любимых фильмов: ", favorite_film_list)

# зачёт!
