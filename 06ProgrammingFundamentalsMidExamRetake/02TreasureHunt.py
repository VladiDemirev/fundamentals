treasure_chest = input().split("|")

while True:
    command = input().split()
    # command = input()
    # action, amount = command.split(" ", 1)
    if command[0] == "Yohoho!":
        break
    action = command[0]
    if action == "Loot":

        item_list = [command[idx] for idx in range(1, len(command))]    # OPTION 1

        # item_list = []    # OPTION 2
        # for idx in range(1, len(command)):
        #     item_list.append(command[idx])

        # item_list = command[1::]  # OPTION 3

        for item in item_list:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif action == "Drop":
        index = int(command[1])
        # if index in range(-len(treasure_chest), len(treasure_chest)):
        if index in range(len(treasure_chest)):

            treasure_chest.append(treasure_chest[index])
            treasure_chest.remove(treasure_chest[index])

            # treasure_chest.append(treasure_chest[index])  # OPTION 1
            # if index < 0:
            #     treasure_chest.remove(treasure_chest[index - 1])
            # else:
            #     treasure_chest.remove(treasure_chest[index])

            # removed_loot = treasure_chest.pop(index)    # OPTION 2
            # treasure_chest.append(removed_loot)

    elif action == "Steal":
        count = int(command[1])
        stolen_list = []
        for i in range(min(count, len(treasure_chest))):
            stolen_list.append(treasure_chest.pop())
        stolen_list.reverse()
        print(", ".join(stolen_list))

if len(treasure_chest) > 0:
    items_length = sum(len(item) for item in treasure_chest)
    average_gain = items_length / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
