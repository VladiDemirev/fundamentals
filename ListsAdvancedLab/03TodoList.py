# to_do_list = []
#
# while True:
#     to_do_notes = input()
#     if to_do_notes == "End":
#         break
#     split_to_do_notes = to_do_notes.split("-")
#     importance = int(split_to_do_notes[0])
#     note = split_to_do_notes[1]
#     to_do_list.append([importance, note])
#
# sorted_list = [note[1] for note in sorted(to_do_list)]
#
# print(sorted_list)


#   OPTION 2

to_do_list = [0] * 10

while True:
    to_do_notes = input()
    if to_do_notes == "End":
        break
    split_to_do_notes = to_do_notes.split("-")
    importance = int(split_to_do_notes[0]) - 1
    note = split_to_do_notes[1]
    to_do_list.pop(importance)
    to_do_list.insert(importance, note)

final_list = [task for task in to_do_list if task != 0]

print(final_list)
