rooms = input().split("|")
MAX_HEALTH = 100
current_health = MAX_HEALTH
bitcoins = 0
room_count = 1

for room in rooms:
    command, number = room.split()
    int_number = int(number)
    if command == "potion":
        healed_points = int_number
        current_health += healed_points
        if current_health > MAX_HEALTH:
            healed_points = MAX_HEALTH - (current_health - healed_points)
            current_health = MAX_HEALTH
        print(f"You healed for {healed_points} hp.")
        print(f"Current health: {current_health} hp.")
    elif command == "chest":
        print(f"You found {int_number} bitcoins.")
        bitcoins += int_number
    else:
        current_health -= int_number
        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            break
    room_count += 1

else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")
