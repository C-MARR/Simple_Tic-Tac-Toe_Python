from winchecks import check_all, piece_count
from tictactoeutils import print_board, split_ttt_string


tic_tac_toe_moves = input("Enter cells: ")
game_grid = split_ttt_string(tic_tac_toe_moves)
print_board(game_grid)

if abs(piece_count("X", game_grid) - piece_count("O", game_grid)) > 1 \
        or (check_all(game_grid, "X") == 1 and check_all(game_grid, "O") == -1):
    print("Impossible")
elif check_all(game_grid, "X") == 1:
    print("X wins")
elif check_all(game_grid, "O") == -1:
    print("O wins")
elif piece_count("X", game_grid) + piece_count("O", game_grid) == 9:
    print("Draw")
else:
    print("Game not finished")

