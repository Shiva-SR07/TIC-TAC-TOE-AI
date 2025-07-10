import math

# Board Setup
board = [' ' for _ in range(9)]

# Print Board
def print_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print('|'.join(row))
        if i < 2:
            print("-----")

# Check for Winner
def check_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # Rows
        [0,3,6], [1,4,7], [2,5,8], # Columns
        [0,4,8], [2,4,6]           # Diagonals
    ]
    for condition in win_conditions:
        if all(brd[i] == player for i in condition):
            return True
    return False

# Check for Draw
def is_draw(brd):
    return ' ' not in brd

# Get Available Moves
def get_available_moves(brd):
    return [i for i, spot in enumerate(brd) if spot == ' ']

# Minimax Algorithm
def minimax(brd, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    elif check_winner(brd, 'X'):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, False)
            brd[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, True)
            brd[move] = ' '
            best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

# Human Move
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is taken.")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number between 1 and 9.")

# Game Loop
def play():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', AI is 'O'")
    print_board()

    while True:
        human_move()
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        print("AI's move:")
        ai_move()
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Start the game
play()
