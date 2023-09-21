sequence = [int(x) for x in input().split()]
shot_targets = 0

while True:
    command = input()
    if command == "End":
        break
    idx = int(command)
    if idx < 0 or idx > len(sequence) - 1:
        continue
    factor = sequence[idx]
    sequence[idx] = -1
    for i in range(len(sequence)):
        if sequence[i] != -1 and sequence[i] > factor:
            sequence[i] -= factor
        elif sequence[i] != -1 and sequence[i] <= factor:
            sequence[i] += factor
    shot_targets += 1

print(f"Shot targets: {shot_targets} -> {' '.join(str(x) for x in sequence)}")
