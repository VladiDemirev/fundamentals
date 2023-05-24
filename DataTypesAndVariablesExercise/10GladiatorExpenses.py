# lost_fights_count = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# expenses = 0
#
# for i in range(1, lost_fights_count + 1):
#     if i % 2 == 0:
#         expenses += helmet_price
#     if i % 3 == 0:
#         expenses += sword_price
#     if i % 6 == 0:
#         expenses += shield_price
#     if i % 12 == 0:
#         expenses += armor_price
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")


# OPTION 2

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = lost_fights_count // 2
broken_swords = lost_fights_count // 3
broken_shields = lost_fights_count // (2 * 3)
broken_armors = broken_shields // 2

expenses = broken_helmets * helmet_price + \
           broken_swords * sword_price + \
           broken_shields * shield_price + \
           broken_armors * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
