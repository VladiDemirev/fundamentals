# junk_material = {}
# legendary_material = {
#   "shards": 0,
#   "fragments": 0,
#   "motes": 0
# }
# is_won = False

# while True:
#   data = input().split()

#   for el in range(0, len(data), 2):
#     quantity = int(data[el])
#     material = data[el + 1].lower()
#     if material in legendary_material:
#       legendary_material[material] += quantity
#     elif material not in junk_material:
#       junk_material[material] = quantity
#     else:
#       junk_material[material] += quantity

#     if material == "shards" and legendary_material[material] >= 250:
#       print("Shadowmourne obtained!")
#       legendary_material[material] = abs(250 - legendary_material[material])
#       is_won = True
#       break
#     elif material == "fragments" and legendary_material[material] >= 250:
#       print("Valanyr obtained!")
#       legendary_material[material] = abs(250 - legendary_material[material])
#       is_won = True
#       break
#     elif material == "motes" and legendary_material[material] >= 250:
#       print("Dragonwrath obtained!")
#       legendary_material[material] = abs(250 - legendary_material[material])
#       is_won = True
#       break
#   if is_won:
#     break

# for material, quantity in legendary_material.items():
#   print(f"{material}: {quantity}")

# for material, quantity in junk_material.items():
#   print(f"{material}: {quantity}")


# OPTION 2

junk_material = {}
legendary_material = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
legendary_item_material = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}
is_won = False

while not is_won:
    data = input().split()

    for el in range(0, len(data), 2):
        quantity = int(data[el])
        material = data[el + 1].lower()
        if material in legendary_material:
            legendary_material[material] += quantity
            if legendary_material[material] >= 250:
                legendary_material[material] -= 250
                print(f"{legendary_item_material[material]} obtained!")
                is_won = True
                break
        elif material not in junk_material:
            junk_material[material] = quantity
        else:
            junk_material[material] += quantity

for material, quantity in legendary_material.items():
    print(f"{material}: {quantity}")

for material, quantity in junk_material.items():
    print(f"{material}: {quantity}")