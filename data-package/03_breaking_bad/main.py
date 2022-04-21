import requests
import json

my_req = requests.get("https://www.breakingbadapi.com/api/deaths")

data = json.loads(my_req.text)  # десериализация JSON

with open("deaths.json", "w") as file_1:
    json.dump(data, file_1, indent=4)  # сериализация JSON

my_episode = max(data, key=lambda i_episode: i_episode["number_of_deaths"])

new_episode = {k: v for k, v in my_episode.items() if k == 'death_id' or k == 'death' or k == 'season'
               or k == 'episode' or k == 'number_of_deaths'}
print(new_episode)

with open("max_deaths.json", "w") as file_2:
    json.dump(new_episode, file_2, indent=4)  # сериализация JSON

# id эпизода 'death_id' есть по данной ссылке, я проверила с той ссылкой,
# которую Вы указали, там идентичный id, который равен 12, как и тут =)

# хорошо =)
# зачёт!
