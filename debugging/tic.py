#!/usr/bin/python3
def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner on the Tic-Tac-Toe board."""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Play a game of Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                if row not in [0, 1, 2]:
                    raise ValueError
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if col not in [0, 1, 2]:
                    raise ValueError
                if board[row][col] == " ":
                    board[row][col] = player
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
                    break
                else:
                    print("That spot is already taken! Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid row and column.")

    print_board(board)
    if player == "X":
        winning_player = "O"
    else:
        winning_player = "X"
    print("Player " + winning_player + " wins!")

tic_tac_toe()
