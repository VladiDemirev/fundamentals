def items_needed_for_pig(food, hay, cover, weight):
    daily_food_eaten = 300 / 1000

    for day in range(1, 31):
        food -= daily_food_eaten
        if day % 2 == 0:
            hay -= (food * 0.05)
        if day % 3 == 0:
            cover -= (weight / 3)
        if (
                food < 0 or
                hay < 0 or
                cover < 0
        ):
            return "Merry must go to the pet store!"

    else:
        return f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}."


quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
pig_weight = float(input())

print(items_needed_for_pig(quantity_food, quantity_hay, quantity_cover, pig_weight))

#   OPTION 2

# quantity_food = float(input())
# quantity_hay = float(input())
# quantity_cover = float(input())
# pig_weight = float(input())
#
# DAILY_FOOD_EATEN = 300 / 1000
#
# for day in range(1, 31):
#     quantity_food -= DAILY_FOOD_EATEN
#     if day % 2 == 0:
#         quantity_hay -= (quantity_food * 0.05)
#     if day % 3 == 0:
#         quantity_cover -= (pig_weight / 3)
#     if (
#             quantity_food < 0 or
#             quantity_hay < 0 or
#             quantity_cover < 0
#     ):
#         print("Merry must go to the pet store!")
#         break
#
# else:
#     print(
#         f"Everything is fine! Puppy is happy! Food: {quantity_food:.2f}, Hay: {quantity_hay:.2f}, Cover: {quantity_cover:.2f}.")
