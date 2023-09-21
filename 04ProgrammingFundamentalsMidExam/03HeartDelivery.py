needed_hearts = [int(x) for x in input().split("@")]
current_index = 0
is_love = False

while True:
    command = input().split()
    if command[0] == "Love!":
        is_love = True
        break
    elif command[0] == "Jump":
        length = int(command[1])

        if length > ((len(needed_hearts) - 1) - current_index):
            current_index = 0
            if needed_hearts[current_index] == 0:
                print(f"Place {current_index} already had Valentine's day.")
            elif needed_hearts[current_index] > 0:
                needed_hearts[current_index] -= 2
                if needed_hearts[current_index] == 0:
                    print(f"Place {current_index} has Valentine's day.")

        else:
            current_index += length
            if needed_hearts[current_index] == 0:
                print(f"Place {current_index} already had Valentine's day.")
            elif needed_hearts[current_index] > 0:
                needed_hearts[current_index] -= 2
                if needed_hearts[current_index] == 0:
                    print(f"Place {current_index} has Valentine's day.")

if is_love:
    print(f"Cupid's last position was {current_index}.")
    if sum(needed_hearts) == 0:
        print("Mission was successful.")
    else:
        failed_places = [x for x in needed_hearts if x > 0]
        print(f"Cupid has failed {len(failed_places)} places.")

