def check_inventory(inventory_list):
    while True:
        command = input().split(" - ")
        if command[0] == "Craft!":
            break
        action = command[0]
        item = command[1]
        if action == "Collect":
            if item not in inventory_list:
                inventory_list.append(item)
        elif action == "Drop":
            if item in inventory_list:
                inventory_list.remove(item)
        elif action == "Combine Items":
            old_item, new_item = item.split(":")
            if old_item in inventory_list:
                inventory_list.insert(inventory_list.index(old_item) + 1, new_item)
        elif action == "Renew":
            if item in inventory_list:
                inventory_list.append(item)
                inventory_list.remove(item)
    return ", ".join(inventory_list)


journal = input().split(", ")

print(check_inventory(journal))
