num_coffees = 0
events_lowercase = ["coding", "dog", "cat", "movie"]
events_uppercase = ["CODING", "DOG", "CAT", "MOVIE"]

while True:
    command = input()

    if command == "END":
        break

    if command in events_lowercase:
        num_coffees += 1
    elif command in events_uppercase:
        num_coffees += 2

if num_coffees <= 5:
    print(num_coffees)
else:
    print("You need extra sleep")
