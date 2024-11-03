def find_common_participants(participants_first_group, participants_second_group, separator=","):
    first_group_list = participants_first_group.split(separator)
    second_group_list = participants_second_group.split(separator)
    common_participants = list(set(first_group_list) & set(second_group_list))
    common_participants.sort()
    return common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator=",")
print(f"Общие участники: {common_participants}")
# TODO Проверьте работу функции с разделителем отличным от запятой
