def winner(field):
    for row in field:
        sum_row = sum(int(x) for x in row if x != " ")
        if (row[0] == row[2]) and sum_row == 3:
            return "First player won"
        elif (row[0] == row[2]) and sum_row == 6:
            return "Second player won"

    col1 = field[0][0] + field[1][0] + field[2][0]
    col2 = field[0][2] + field[1][2] + field[2][2]
    col3 = field[0][4] + field[1][4] + field[2][4]
    col_list = [col1, col2, col3]
    for col in col_list:
        sum_col = sum(int(x) for x in col if x != " ")
        if (col[1] == col[2]) and sum_col == 3:
            return "First player won"
        elif (col[1] == col[2]) and sum_col == 6:
            return "Second player won"

    diagonal1 = field[0][0] + field[1][2] + field[2][4]
    diagonal2 = field[0][4] + field[1][2] + field[2][0]
    diagonal_list = [diagonal1, diagonal2]
    for diagonal in diagonal_list:
        sum_diagonal = sum(int(x) for x in diagonal if x != " ")
        if (diagonal[1] == diagonal[2]) and sum_diagonal == 3:
            return "First player won"
        elif (diagonal[1] == diagonal[2]) and sum_diagonal == 6:
            return "Second player won"

    return "Draw!"


game_field = []

for _ in range(3):
    user_input = input()
    game_field.append(user_input)

print(winner(game_field))
