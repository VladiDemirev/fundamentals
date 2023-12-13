# tickets = [ticket.strip() for ticket in input().split(", ")]
# winning_symbols = ['@', '#', '$', '^']
#
# for ticket in tickets:
#     is_won = False
#     if len(ticket) != 20:
#         print("invalid ticket")
#         continue
#
#     left_part = ticket[:10]
#     right_part = ticket[10:]
#
#     for match_symbol in winning_symbols:
#         for uninterrupted_match_length in range(10, 5, -1):
#             winning_symbols_repetition = match_symbol * uninterrupted_match_length
#             if winning_symbols_repetition in left_part and winning_symbols_repetition in right_part:
#                 if uninterrupted_match_length == 10:
#                     print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!')
#                     is_won = True
#                     break
#                 else:
#                     print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')
#                     is_won = True
#                     break
#         if is_won:
#             break
#     if is_won:
#         continue
#     else:
#         print(f'ticket "{ticket}" - no match')


#  OPTION 2

def matching_symbols(part, matching_symbol):
    current_streak = 0
    best_uninterrupted = 0
    for char in part:
        if char == matching_symbol:
            current_streak += 1
        else:
            best_uninterrupted = max(best_uninterrupted, current_streak)
            current_streak = 0
    return max(best_uninterrupted, current_streak)


tickets = [ticket.strip() for ticket in input().split(", ")]

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left_part = ticket[:10]
    right_part = ticket[10:]

    best_symbol = ""
    overall_score = 0

    for symbol in winning_symbols:
        left_part_score = matching_symbols(left_part, symbol)
        right_part_score = matching_symbols(right_part, symbol)
        if min(left_part_score, right_part_score) > overall_score:
            overall_score = min(left_part_score, right_part_score)
            best_symbol = symbol

    is_winning = overall_score >= 6
    is_jackpot = is_winning and overall_score == 10

    if is_jackpot:
        print(f'ticket "{ticket}" - {overall_score}{best_symbol} Jackpot!')
    elif is_winning:
        print(f'ticket "{ticket}" - {overall_score}{best_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')


#   OPTION 3 - 81/100 IN JUDGE

# tickets = [ticket.strip() for ticket in input().split(", ")]
#
# winning_symbols = ['@', '#', '$', '^']
#
# for ticket in tickets:
#     if len(ticket) != 20:
#         print("invalid ticket")
#         continue
#
#     left_part = ticket[:10]
#     right_part = ticket[10:]
#
#     # current_streak_l = 0
#     best_uninterrupted_l = 0
#     best_symbol_l = ""
#     # current_streak_r = 0
#     best_uninterrupted_r = 0
#     best_symbol_r = ""
#
#     for symbol in winning_symbols:
#         current_streak_l = 0
#         # best_uninterrupted_l = 0
#         # best_symbol_l = ""
#         overall_score = 0
#         for char in left_part:
#             if char == symbol:
#                 current_streak_l += 1
#                 if current_streak_l > 5:
#                     best_symbol_l = symbol
#             else:
#                 best_uninterrupted_l = max(best_uninterrupted_l, current_streak_l)
#                 # if best_uninterrupted_l > 5:
#                     # best_symbol_l = symbol
#                 current_streak_l = 0
#         best_uninterrupted_l = max(best_uninterrupted_l, current_streak_l)
#
#     for symbol in winning_symbols:
#         current_streak_r = 0
#         # best_uninterrupted_r = 0
#         # best_symbol_r = ""
#         for char in right_part:
#             if char == symbol:
#                 current_streak_r += 1
#                 if current_streak_r > 5:
#                     best_symbol_r = symbol
#             else:
#                 best_uninterrupted_r = max(best_uninterrupted_r, current_streak_r)
#                 # if best_uninterrupted_r > 5:
#                 #     best_symbol_r = symbol
#                 current_streak_r = 0
#         best_uninterrupted_r = max(best_uninterrupted_r, current_streak_r)
#
#     if best_symbol_l == best_symbol_r:
#         best_uninterrupted = min(best_uninterrupted_l, best_uninterrupted_r)
#
#         is_winning = best_uninterrupted >= 6
#         is_jackpot = is_winning and best_uninterrupted == 10
#
#         if is_jackpot:
#             print(f'ticket "{ticket}" - {best_uninterrupted}{best_symbol_l} Jackpot!')
#         elif is_winning:
#             print(f'ticket "{ticket}" - {best_uninterrupted}{best_symbol_l}')
#         else:
#             print(f'ticket "{ticket}" - no match')

