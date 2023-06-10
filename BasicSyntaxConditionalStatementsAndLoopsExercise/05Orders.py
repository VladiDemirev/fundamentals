orders = int(input())
total_price = 0

for _ in range(orders):

    price_capsule = float(input())
    days = int(input())
    daily_capsules = int(input())

    if (
            (price_capsule < 0.01 or price_capsule > 100.00) or
            (days < 1 or days > 31) or
            (daily_capsules < 1 or daily_capsules > 2000)
    ):
        continue

    price = daily_capsules * days * price_capsule
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price

print(f"Total: ${total_price:.2f}")

