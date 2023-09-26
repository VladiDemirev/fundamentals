count = int(input())
plants_rarity = {}
plants_rating = {}

for _ in range(count):
    plant, rarity = input().split("<->")
    # plants_rarity[plant] = int(rarity)
    plants_rarity[plant] = rarity
    plants_rating[plant] = []

while True:
    command = input()
    if command == "Exhibition":
        break

    command_args = command.split(":")
    action = command_args[0].strip()
    other_args = command_args[1].split()
    plant = other_args[0].strip()

    if plant not in plants_rarity:
        print("error")
        continue
    if action == "Rate":
        rating = other_args[2].strip()
        plants_rating[plant].append(int(rating))
    elif action == "Update":
        new_rarity = other_args[2].strip()
        plants_rarity[plant] = new_rarity
    elif action == "Reset":
        plants_rating[plant] = [0]

print("Plants for the exhibition:")
for plant, rarity in plants_rarity.items():
    if len(plants_rating[plant]) < 1:
        plants_rating[plant] = [0]
    average_rating = sum(plants_rating[plant]) / len(plants_rating[plant])
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
