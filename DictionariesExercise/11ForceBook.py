data = input()
force_by_side = {}
force_by_user = {}

while data != "Lumpawaroo":
    if "|" in data:
        force_side, force_user = data.split(" | ")
        if force_side not in force_by_side:
            force_by_side[force_side] = []
        if force_user not in force_by_user:
            force_by_user[force_user] = force_side
            force_by_side[force_side].append(force_user)

    elif "->" in data:
        force_user, force_side = data.split(" -> ")
        if force_side not in force_by_side:
            force_by_side[force_side] = []

        force_by_side[force_side].append(force_user)

        if force_user in force_by_user:
            old_side = force_by_user[force_user]
            force_by_side[old_side].remove(force_user)
            force_by_user[force_user] = force_side
        else:
            force_by_user[force_user] = force_side

        print(f"{force_user} joins the {force_side} side!")

    data = input()

for side, members in force_by_side.items():
    if len(members) == 0:
        continue
    print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")


# data = input()
# profiles = {}
#
# while data != "Lumpawaroo":
#     if "|" in data:
#         force_side, force_user = data.split(" | ")
#         if force_side not in profiles:
#             profiles[force_side] = [force_user]
#         else:
#             if profiles[force_side] not in profiles.values():
#                 profiles[force_side].append(force_user)
#
#     elif "->" in data:
#         force_user, force_side = data.split(" -> ")
#         if force_side not in profiles:
#             profiles[force_side] = [force_user]
#         if force_user in profiles.values():
#             profiles.pop(force_user)
#         elif force_user not in profiles.values():
#             profiles[force_side].append(force_user)
#             print(f"{force_user} joins the {force_side} side!")
#
#     data = input()
#
# for side, user in profiles.items():
#     print(f"Side: {side}, Members: {len(user)}")
#     for user in profiles[side]:
#         print(f"! {user}")
