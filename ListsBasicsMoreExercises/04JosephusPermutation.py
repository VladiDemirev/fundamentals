def executed_people(sequence, count):
    executed_people_list = []
    current_position = 0
    while sequence:
        current_position += (count - 1)
        while current_position >= len(sequence):
            current_position = current_position - len(sequence)
        executed_people_list.append(sequence.pop(current_position))
    return f"[{','.join(executed_people_list)}]"


people_numbers = list(input().split())
number = int(input())
print(executed_people(people_numbers, number))
