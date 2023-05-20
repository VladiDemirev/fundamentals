number = int(input())

for letter1 in range(ord("a"), ord("a") + number):
    for letter2 in range(ord("a"), ord("a") + number):
        for letter3 in range(ord("a"), ord("a") + number):
            print(chr(letter1) + chr(letter2) + chr(letter3))
