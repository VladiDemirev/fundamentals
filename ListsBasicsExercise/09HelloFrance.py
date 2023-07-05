collection_items = input().split("|")
budget = float(input())
TICKET = 150
new_price_list = []
string_new_price_list = []
profit = 0

for position in collection_items:
    # items_arguments = position.split("->")
    item, price = position.split("->")
    price = float(price)
    # item = items_arguments[0]
    # price = float(items_arguments[1])
    new_price = 0

    if price > budget:
        continue
    if item == "Clothes" and price > 50:
        continue
    if item == "Shoes" and price > 35:
        continue
    if item == "Accessories" and price > 20.50:
        continue

    budget -= price
    profit += price * 0.4
    new_price += price * 1.4
    new_price_list.append(new_price)
    string_new_price_list.append(f"{new_price:.2f}")

print(" ".join(string_new_price_list))
print(f"Profit: {profit:.2f}")

new_budget = budget + sum(new_price_list)

if new_budget >= TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")


# OPTION 2

# collection_items = input().split("|")
# budget = float(input())
# TICKET = 150
# price_list = []
# new_price_list = []
# profit = 0
#
# for position in collection_items:
#     items_arguments = position.split("->")
#
#     item = items_arguments[0]
#     price = float(items_arguments[1])
#
#     if price > budget:
#         continue
#
#     if item == "Clothes" and price > 50:
#         continue
#     if item == "Shoes" and price > 35:
#         continue
#     if item == "Accessories" and price > 20.50:
#         continue
#
#     price_list.append(price)
#
#     budget -= price
#
# for new_price in price_list:
#     new_price = f"{new_price * 1.4:.2f}"
#     new_price_list.append(new_price)
#     profit += float(new_price)
#
# new_budget = budget + profit
# # string_new_price_list = [str(x) for x in new_price_list]
# # print(" ".join(string_new_price_list))
# print(" ".join(new_price_list))
#
# sum_new_price_list = sum(float(x) for x in new_price_list)
#
# total_profit = sum_new_price_list - sum(price_list)
# print(f"Profit: {total_profit:.2f}")
#
# if new_budget >= TICKET:
#     print("Hello, France!")
# else:
#     print("Not enough money.")
