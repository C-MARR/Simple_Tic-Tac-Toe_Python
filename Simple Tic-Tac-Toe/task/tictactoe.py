from winchecks import check_all, piece_count
from tictactoeutils import print_board, split_ttt_string

game_grid = split_ttt_string("         ")
print_board(game_grid)
x_turn = True
game_over = False
while not game_over:
    coordinates = input("Enter the coordinates: ").split()
    if not coordinates[0].isdigit() or not coordinates[1].isdigit() or len(coordinates) != 2:
        print("You should enter numbers!")
    elif int(coordinates[0]) not in range(1, 4) or int(coordinates[1]) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
    elif game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "X" \
            or game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "X" if x_turn else "O"
        x_turn = not x_turn
    print_board(game_grid)
    if check_all(game_grid, "X") == 1:
        print("X wins")
        break
    elif check_all(game_grid, "O") == -1:
        print("O wins")
        break
    elif piece_count("X", game_grid) + piece_count("O", game_grid) == 9:
        print("Draw")
        break

