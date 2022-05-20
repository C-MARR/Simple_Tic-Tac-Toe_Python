def print_board(game_grid):
    border = "---------"
    print(border)
    for row in range(3):
        print("| ", end="")
        for column in range(3):
            print(f"{game_grid[row][column]} ", end="")
        print("|")
    print(border)


def split_ttt_string(tic_tac_toe_moves):
    index = 0
    game_grid = []
    for _ in range(3):
        new_row = []
        for _ in range(3):
            new_row.append(tic_tac_toe_moves[index])
            index += 1
        game_grid.append(new_row)
    return game_grid
