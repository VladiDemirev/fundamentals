initial_energy = int(input())
won_battles = 0
has_ended = False

while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
        break
    distance = int(distance)
    if distance > initial_energy:
        has_ended = True
        break
    initial_energy -= distance
    won_battles += 1
    if won_battles % 3 == 0:
        initial_energy += won_battles

if has_ended:
    print(f"Not enough energy! Game ends with {won_battles} won battles "
          f"and {initial_energy} energy")