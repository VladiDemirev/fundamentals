happiness = list(map(int, input().split()))
factor = int(input())

happiness_multiplied = list(map(lambda x: x * factor, happiness))
average_happiness = sum(happiness_multiplied) / len(happiness_multiplied)

# happy_count = 0
total_count = len(happiness)

# for employee in happiness_multiplied:
#     if employee > average_happiness:
#         happy_count += 1

happy_count = list(filter(lambda x: x >= average_happiness, happiness_multiplied))

if len(happy_count) >= total_count // 2:
    print(f"Score: {len(happy_count)}/{total_count}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{total_count}. Employees are not happy!")
