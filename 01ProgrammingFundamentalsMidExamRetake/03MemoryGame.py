elements = [x for x in input().split()]
number_of_moves = 0
is_won = False

while True:
    command = [x for x in input().split()]

    if command[0] == "end":
        break
    index_first_el = int(command[0])
    index_second_el = int(command[1])
    sequence_middle = len(elements) // 2
    number_of_moves += 1

    if (
            index_first_el == index_second_el or
            index_first_el not in range(len(elements)) or
            index_second_el not in range(len(elements))
    ):
        element_to_be_inserted = f"-{number_of_moves}a"
        elements.insert(sequence_middle, element_to_be_inserted)
        elements.insert(sequence_middle, element_to_be_inserted)
        print("Invalid input! Adding additional elements to the board")

    elif elements[index_first_el] == elements[index_second_el]:
        print(f"Congrats! You have found matching elements - {elements[index_first_el]}!")
        elements = [element for element in elements if element != elements[index_first_el]]
    elif elements[index_first_el] != elements[index_second_el]:
        print("Try again!")

    if len(elements) == 0:
        is_won = True
        break

if is_won:
    print(f"You have won in {number_of_moves} turns!")
else:
    print(f"Sorry you lose :( \n{' '.join(elements)}")
