from math import ceil

num_people = int(input())
capacity = int(input())

num_courses = ceil(num_people / capacity)

print(num_courses)

#   OPTION 2
# num_people = int(input())
# capacity = int(input())
#
# num_courses = 0
#
# while num_people > 0:
#     num_courses += num_people // capacity
#     if num_people < capacity:
#         num_courses += 1
#     num_people -= (num_courses * capacity)
#
# print(num_courses)
