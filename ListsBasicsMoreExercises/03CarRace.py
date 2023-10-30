def race_winner(numbers):
    finish_index = len(numbers) // 2
    time_first_car = 0
    time_second_car = 0

    for time in numbers[:finish_index]:
        if time == 0:
            time_first_car *= 0.8
        time_first_car += time
    for time in numbers[(len(numbers) - 1): finish_index: -1]:
        if time == 0:
            time_second_car *= 0.8
        time_second_car += time

    if time_first_car < time_second_car:
        return f"The winner is left with total time: {time_first_car:.1f}"
    elif time_first_car > time_second_car:
        return f"The winner is right with total time: {time_second_car:.1f}"


numbers_sequence = [int(x) for x in input().split()]
print(race_winner(numbers_sequence))
