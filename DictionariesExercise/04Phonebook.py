data = input()
phonebook = {}

while "-" in data:
    name, number = data.split("-")
    phonebook[name] = number

    data = input()

contacts = int(data)
for _ in range(contacts):
    person = input()
    if person in phonebook:
        print(f"{person} -> {phonebook[person]}")
    else:
        print(f"Contact {person} does not exist.")
        