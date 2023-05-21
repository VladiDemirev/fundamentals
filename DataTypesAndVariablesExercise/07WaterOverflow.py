# num_lines = int(input())
# CAPACITY = 255
# liters_in = 0
#
# for i in range(num_lines):
#     liters = int(input())
#     liters_in += liters
#
#     if liters_in > CAPACITY:
#         print("Insufficient capacity!")
#         liters_in -= liters
#
# print(liters_in)


#   OPTION 2

# num_lines = int(input())
# CAPACITY = 255
# liters_in = 0
#
# for i in range(num_lines):
#     liters = int(input())
#
#     if CAPACITY - liters < 0:
#         print("Insufficient capacity!")
#         continue
#     CAPACITY -= liters
#     liters_in += liters
#
# print(liters_in)


#   OPTION 3

num_lines = int(input())
CAPACITY = 255

for i in range(num_lines):
    liters = int(input())

    if CAPACITY - liters < 0:
        print("Insufficient capacity!")
        continue
    CAPACITY -= liters

print(255 - CAPACITY)

