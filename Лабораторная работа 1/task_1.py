numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum_num = 0
count = 0
for num in numbers:
    if num is not None:
        sum_num += num
        count += 1

average = sum_num / count

index_of_none = numbers.index(None)

numbers[index_of_none] = average

print("Измененный список:", numbers)

