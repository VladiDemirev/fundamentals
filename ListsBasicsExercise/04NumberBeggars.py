integers = input().split(", ")
beggars = int(input())

sum_integers = []
int_integers = [int(x) for x in integers]
starting_index = 0

while starting_index < beggars:
    sum_current_beggar = 0

    for i in range(starting_index, len(int_integers), beggars):
        sum_current_beggar += int_integers[i]
    sum_integers.append(sum_current_beggar)
    starting_index += 1

print(sum_integers)
