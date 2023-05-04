quantity_decorations = int(input())
days_to_xmas = int(input())

total_cost = 0
total_spirit = 0

ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLAND = 3
TREE_LIGHTS = 15

for days in range(1, days_to_xmas + 1):
    if days % 11 == 0:
        quantity_decorations += 2
    if days % 2 == 0:
        total_cost += (ORNAMENT_SET * quantity_decorations)
        total_spirit += 5
    if days % 3 == 0:
        total_cost += (TREE_SKIRT * quantity_decorations + TREE_GARLAND * quantity_decorations)
        total_spirit += 3 + 10
    if days % 5 == 0:
        total_cost += (TREE_LIGHTS * quantity_decorations)
        total_spirit += 17
    if days % 15 == 0:
        total_spirit += 30
    if days % 10 == 0:
        total_cost += (TREE_SKIRT + TREE_GARLAND + TREE_LIGHTS)
        total_spirit -= 20

if days_to_xmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
