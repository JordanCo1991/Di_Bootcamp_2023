def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j], end="|")
        print("\n---------")

def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        if is_board_full(board):
            print("It's a tie!")
            break

        row = int(input("Player {} - Enter the row (0-2): ".format(player)))
        col = int(input("Player {} - Enter the column (0-2): ".format(player)))

        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player {} wins!".format(winner))
            break

        player = "O" if player == "X" else "X"

play_tic_tac_toe()
