# old_version = list(map(int, input().split(".")))
#
# if old_version[2] < 9:
#     new_version = f"{old_version[0]}.{old_version[1]}.{old_version[2] +1}"
# elif old_version[1] == 9 and old_version[2] == 9:
#     new_version = f"{old_version[0] + 1}.0.0"
# elif old_version[2] == 9:
#     new_version = f"{old_version[0]}.{old_version[1] + 1}.0"
#
# print(new_version)


#   OPTION 2

# old_version = "".join(input().split("."))
#
# new_version = int(old_version) + 1
#
# print(".".join(str(new_version)))


#   OPTION 3

next_version = [int(x) for x in input().split(".")]

next_version[-1] += 1

for index in range(len(next_version) - 1, - 1, - 1):
    if next_version[index] > 9 and index != 0:
        next_version[index] = 0
        next_version[index - 1] += 1

print(".".join(str(num) for num in next_version))
