snowballs = int(input())
highest_value = 0
current_value = 0
highest_value_weight = 0
highest_value_time = 0
highest_value_quality = 0

for i in range(snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_value = (snowball_weight / snowball_time) ** snowball_quality
    if current_value > highest_value:
        highest_value = current_value
        highest_value_weight = snowball_weight
        highest_value_time = snowball_time
        highest_value_quality = snowball_quality

print(f"{highest_value_weight} : {highest_value_time} = {int(highest_value)} ({highest_value_quality})")
