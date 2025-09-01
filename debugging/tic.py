#!/usr/bin/python3

def print_board(board):
    """Displays the current game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there's a winning condition on the board.

    Returns:
        bool: True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_board_full(board):
    """
    Checks if the board is full (i.e., a draw).

    Returns:
        bool: True if no empty spaces remain, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position. Must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()