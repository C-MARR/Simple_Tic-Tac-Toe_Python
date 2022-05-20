def print_board(t_t_t_string):
    border = "---------"
    print(border)
    for tic in range(0, 9, 3):
        print(f"| {t_t_t_string[tic]} {t_t_t_string[tic + 1]} {t_t_t_string[tic + 2]} |")
    print(border)


ttt = input("Enter cells: ")
print_board(ttt)
