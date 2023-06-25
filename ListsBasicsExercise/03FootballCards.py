red_cards = input().split()

team_A = ["A-" + str(i) for i in range(1, 12)]
team_B = ["B-" + str(i) for i in range(1, 12)]

is_terminated = False

for player in red_cards:
    if player in team_A:
        team_A.remove(player)
    elif player in team_B:
        team_B.remove(player)
    if len(team_A) < 7 or len(team_B) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if is_terminated:
    print("Game was terminated")


#   OPTION 2

# red_cards = input().split()

# team_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
#
# for player in red_cards:
#     if player in team_A:
#         team_A.remove(player)
#     elif player in team_B:
#         team_B.remove(player)
#     if len(team_A) < 7 or len(team_B) < 7:
#         break
#
# print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
#
# if len(team_A) < 7 or len(team_B) < 7:
#     print("Game was terminated")
