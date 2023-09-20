people_waiting = int(input())
current_state = [int(x) for x in input().split()]
max_people = 4

for i in range(len(current_state)):
    people_to_add = max_people - current_state[i]
    if people_waiting >= 4:
        current_state[i] += people_to_add
    else:
        current_state[i] += people_waiting

    people_waiting -= people_to_add
    if people_waiting <= 0:
        break

current_state_not_list = " ".join(str(x) for x in current_state)

if people_waiting <= 0 and current_state[-1] < 4:
    print(f"The lift has empty spots!\n{current_state_not_list}")
elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{current_state_not_list}")
else:
    print(current_state_not_list)


#   OPTION 2 - 90/100 IN JUDGE

# people_waiting = int(input())
# current_state = [int(x) for x in input().split()]
# max_people = 4
#
# for i in range(len(current_state)):
#     people_in_wagon = min(people_waiting, max_people)
#     people_to_add = max_people - current_state[i]
#     if current_state[i] == 0:
#         current_state[i] += people_in_wagon
#     elif current_state[i] > 0 and people_waiting != 0:
#         current_state[i] = 4
#     if current_state[i] < 0:
#         current_state[i] = 0
#     people_waiting -= people_to_add
#     if people_waiting <= 0:
#         break
#
# current_state_not_list = " ".join(str(x) for x in current_state)
#
# if people_waiting <= 0 and current_state[-1] < 4:
#     print(f"The lift has empty spots!\n{current_state_not_list}")
# elif people_waiting > 0:
#     print(f"There isn't enough space! {people_waiting} people in a queue!\n{current_state_not_list}")
# else:
#     print(current_state_not_list)
