def pirates_plunder(total_days, actual_plunder, wanted_plunder):
    total_plunder = 0
    for day in range(1, days + 1):
        total_plunder += actual_plunder
        if day % 3 == 0:
            additional_plunder = actual_plunder * 0.5
            total_plunder += additional_plunder
        if day % 5 == 0:
            lost_plunder = total_plunder * 0.3
            total_plunder -= lost_plunder

    if total_plunder >= wanted_plunder:
        return f"Ahoy! {total_plunder:.2f} plunder gained."
    else:
        return f"Collected only {(total_plunder / expected_plunder) * 100:.2f}% of the plunder."


days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

print(pirates_plunder(days, daily_plunder, expected_plunder))
