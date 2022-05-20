def check_rows(game_grid, piece):
    for row in range(3):
        if game_grid[row][0] == piece and game_grid[row][0] == game_grid[row][1] == game_grid[row][2]:
            if piece == "X":
                return 1
            elif piece == "O":
                return -1
    return 0


def check_columns(game_grid, piece):
    for column in range(3):
        if game_grid[0][column] == piece and game_grid[0][column] == game_grid[1][column] == game_grid[2][column]:
            if piece == "X":
                return 1
            elif piece == "O":
                return -1
    return 0


def check_diagonals(game_grid, piece):
    for row in range(3):
        if game_grid[1][1] == piece and (game_grid[0][0] == game_grid[1][1] == game_grid[2][2]
                                         or game_grid[0][2] == game_grid[1][1] == game_grid[2][0]):
            if piece == "X":
                return 1
            elif piece == "O":
                return -1
    return 0


def check_all(game_grid, piece):
    for check in [check_diagonals(game_grid, piece), check_columns(game_grid, piece), check_rows(game_grid, piece)]:
        if check != 0:
            return check
    return 0


def piece_count(piece, game_grid):
    count = 0
    for row in range(3):
        for column in range(3):
            if game_grid[row][column] == piece:
                count += 1
    return count
