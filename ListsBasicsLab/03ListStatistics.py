number = int(input())
positive = []
negative = []

for _ in range(number):
    integer = int(input())
    if integer < 0:
        negative.append(integer)
    else:
        positive.append(integer)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)} \nSum of negatives: {sum(negative)}")
