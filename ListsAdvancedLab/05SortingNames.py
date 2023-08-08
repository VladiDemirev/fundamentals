names = input().split(", ")

sorted_list_by_length = sorted(names, key=lambda x: (-len(x), x))

print(sorted_list_by_length)
