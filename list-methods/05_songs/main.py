violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
total_time = 0
N = int(input("Сколько песен выбрать? "))
for num_song in range(1, N + 1):
    print("Название", num_song, "песни:", end=" ")
    name_song = input()
    for song in violator_songs:
        if song[0] == name_song:
            total_time += song[1]
            break
print("Общее время звучания песен:", total_time, "минут")

# зачёт!
