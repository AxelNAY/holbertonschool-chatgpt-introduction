#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        valid_input = False
        while not valid_input:
            row = input("Enter row (0, 1, or 2) for player " + player + ": ")
            col = input("Enter column (0, 1, or 2) for player " + player + ": ")
            if is_valid_input(row) and is_valid_input(col):
                row, col = int(row), int(col)
                valid_input = True
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")
    print_board(board)
    if player == "X":
        winning_player = "O"
    else:
        winning_player = "X"
    print("Player " + winning_player + " wins!")

tic_tac_toe()
