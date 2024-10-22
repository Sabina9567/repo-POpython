list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

num_players = len(list_players)

if num_players % 2 == 0:
    team1 = list_players[:num_players // 2]
    team2 = list_players[num_players // 2:]
else:
    team1 = list_players[:(num_players // 2) + 1]
    team2 = list_players[(num_players // 2) + 1:]
print("Команда 1:", team1)
print("Команда 2:", team2)
