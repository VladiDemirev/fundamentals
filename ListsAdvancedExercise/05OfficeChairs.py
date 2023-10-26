number_rooms = int(input())
sum_free_chairs = 0

for room in range(1, number_rooms + 1):
    chairs_and_visitors = input().split()
    chairs = chairs_and_visitors[0]
    visitors = int(chairs_and_visitors[1])

    if len(chairs) < visitors:
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")
        sum_free_chairs -= visitors - len(chairs)
    else:
        sum_free_chairs += len(chairs) - visitors

if sum_free_chairs >= 0:
    print(f"Game On, {sum_free_chairs} free chairs left")


