 events = input().split("|")

INITIAL_ENERGY = 100
INITIAL_COIN = 100
is_over = False

for event in events:
    event_args = event.split("-")
    event_or_order = event_args[0]
    energy_or_coin = int(event_args[1])

    if event_or_order == "rest":
        current_energy = INITIAL_ENERGY
        INITIAL_ENERGY += energy_or_coin
        if INITIAL_ENERGY > 100:
            INITIAL_ENERGY = 100

        gained_energy = INITIAL_ENERGY - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {INITIAL_ENERGY}.")

    elif event_or_order == "order":
        if INITIAL_ENERGY >= 30:
            INITIAL_COIN += energy_or_coin
            INITIAL_ENERGY -= 30
            print(f"You earned {energy_or_coin} coins.")
        else:
            print("You had to rest!")
            INITIAL_ENERGY += 50

    else:
        if INITIAL_COIN >= energy_or_coin:
            print(f"You bought {event_or_order}.")
            INITIAL_COIN -= energy_or_coin
        else:
            print(f"Closed! Cannot afford {event_or_order}.")
            is_over = True
            break

if not is_over:
    print("Day completed!")
    print(f"Coins: {INITIAL_COIN}")
    print(f"Energy: {INITIAL_ENERGY}")
