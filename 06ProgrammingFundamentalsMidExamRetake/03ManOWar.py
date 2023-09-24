pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_section_health = int(input())

command = input()

while command != "Retire":
    is_sunken = False
    if command == "Status":
        need_repair = [section for section in pirate_ship if section < max_section_health * 0.2]
        print(f"{len(need_repair)} sections need repair.")

    else:
        action, value = command.split(" ",1)
        if action == "Fire":
            values = [int(x) for x in value.split()]
            index = values[0]
            damage = values[1]
            if index in range(len(warship)):
                warship[index] -= damage
                if warship[index] <= 0:
                    print("You won! The enemy ship has sunken.")
                    # exit()
                    is_sunken = True
                    break
            if is_sunken:
                break

        elif action == "Defend":
            values = [int(x) for x in value.split()]
            start_index = values[0]
            end_index = values[1]
            damage = values[2]
            if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
                for section in range(start_index, end_index + 1):
                    pirate_ship[section] -= damage
                    if pirate_ship[section] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        # exit()
                        is_sunken = True
                        break
                if is_sunken:
                    break

        elif action == "Repair":
            values = [int(x) for x in value.split()]
            index = values[0]
            health = values[1]
            if index in range(len(pirate_ship)):
                if health <= max_section_health - pirate_ship[index]:
                    pirate_ship[index] += health
                else:
                    pirate_ship[index] += max_section_health - pirate_ship[index]

    command = input()

else:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
