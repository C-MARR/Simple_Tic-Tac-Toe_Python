from winchecks import check_all, piece_count
from tictactoeutils import print_board, split_ttt_string


tic_tac_toe_moves = input("Enter cells: ")
game_grid = split_ttt_string(tic_tac_toe_moves)
print_board(game_grid)
while True:
    coordinates = input("Enter the coordinates: ").split()
    if not coordinates[0].isdigit() or not coordinates[1].isdigit() or len(coordinates) != 2:
        print("You should enter numbers!")
    elif int(coordinates[0]) not in range(1, 4) or int(coordinates[1]) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
    elif game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "X" \
            or game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        game_grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = "X"
        break

print_board(game_grid)
