# sequence = [int(x) for x in input().split(", ")]
#
# group = 10
#
# while len(sequence) > 0:
#     current_list = []
#     for number in sequence[::-1]:
#         if number <= group:
#             current_list.append(number)
#             sequence.remove(number)
#     current_list.reverse()
#     print(f"Group of {group}'s: {current_list}")
#     group += 10


#   OPTION 2

# from math import ceil
#
# sequence = [int(x) for x in input().split(", ")]
#
# low_boundary = 1
# high_boundary = 10
#
# for number in range(1, (ceil(max(sequence) / 10)) + 1):
#     group = [x for x in sequence if low_boundary <= x <= high_boundary]
#
#     print(f"Group of {number * 10}'s: {group}")
#     low_boundary += 10
#     high_boundary += 10


#   OPTION 3

sequence = [int(x) for x in input().split(", ")]

group = 10

while sequence:
    current_group = [number for number in sequence if number in range(group + 1)]
    sequence = [num for num in sequence if num not in current_group]
    print(f"Group of {group}'s: {current_group}")
    group += 10
