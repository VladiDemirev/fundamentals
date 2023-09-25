number_pieces = int(input())
collection = {}

for _ in range(number_pieces):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    collection[piece] = []
    collection[piece].append(composer)
    collection[piece].append(key)

command = input()

while command != "Stop":
    command_args = command.split("|")
    action = command_args[0]

    if action == "Add":
        piece = command_args[1]
        composer = command_args[2]
        key = command_args[3]
        if piece not in collection:
            collection[piece] = []
            collection[piece].append(composer)
            collection[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        piece = command_args[1]
        if piece not in collection:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            collection.pop(piece)
            print(f"Successfully removed {piece}!")
    elif action == "ChangeKey":
        piece = command_args[1]
        new_key = command_args[2]
        if piece not in collection:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

    command = input()

for key, value in collection.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
