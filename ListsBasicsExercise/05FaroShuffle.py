card_string = input().split()
shuffles = int(input())

current_shuffle = 0

while current_shuffle < shuffles:
    shuffled_deck = []
    half_deck1 = []
    half_deck2 = []
    for i in range(len(card_string) // 2):
        half_deck1.append(card_string[i])
    for j in range(len(card_string) // 2, len(card_string)):
        half_deck2.append(card_string[j])
    for index_deck in range(len(card_string) // 2):
        shuffled_deck.append(half_deck1[index_deck])
        shuffled_deck.append(half_deck2[index_deck])

    card_string = shuffled_deck
    current_shuffle += 1

print(shuffled_deck)


# OPTION 2

# card_string = input().split()
# shuffles = int(input())
#
# current_shuffle = 0
#
# while current_shuffle < shuffles:
#     shuffled_deck = []
#     middle_deck = (len(card_string) // 2)
#     half_deck_left = card_string[0: middle_deck]
#     half_deck_right = card_string[middle_deck::]
#
#     for card_index in range(len(half_deck_left)):
#         shuffled_deck.append(half_deck_left[card_index])
#         shuffled_deck.append(half_deck_right[card_index])
#
#     card_string = shuffled_deck
#     current_shuffle += 1
#
# print(shuffled_deck)

