number_commands = int(input())
parking_users = {}

for _ in range(number_commands):
    command = input().split()
    if command[0] == "register":
        username, license_plate_number = command[1], command[2]
        if username not in parking_users:
            parking_users[username] = license_plate_number
            print(f"{username} registered {parking_users[username]} successfully")
        elif parking_users[username] == license_plate_number:
            print(f"ERROR: already registered with plate number {parking_users[username]}")

    elif command[0] == "unregister":
        username = command[1]
        if username not in parking_users:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking_users.pop(username)

for name, plate in parking_users.items():
    print(f"{name} => {plate}")
    