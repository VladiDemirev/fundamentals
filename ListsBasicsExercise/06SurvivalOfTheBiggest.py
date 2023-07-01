numbers_list = input().split()
number = int(input())

int_list = [int(x) for x in numbers_list]

# int_list = []
# for x in numbers_list:
#   int_list.append(int(x))

sorted_list = sorted(int_list)

for i in range(number):
    if sorted_list[i] in int_list:
        int_list.remove(sorted_list[i])

print(*int_list, sep=", ")
