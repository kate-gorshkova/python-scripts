import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
tour_winners = [(team_1[i_team] if team_1[i_team] > team_2[i_team] else team_2[i_team]) for i_team in range(20)]
print("Первая команда:", team_1)
print("Вторая команда:", team_2)
print("Победители тура:", tour_winners)

# зачёт!
