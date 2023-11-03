""""5. **Tic-Tac-Toe**: Build a two-player Tic-Tac-Toe game with a text-based interface.
Made with ChatGPT.
"""

# Initialize the board
board = [' ' for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Function to check if the game is over
def is_game_over(board):
    return ' ' not in board

# Function to check if a player has won
def check_win(board, player):
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if all(board[i] == player for i in combo):
            return True
    return False

# Main game loop
player = 'X'

while True:
    display_board(board)
    move = int(input(f'Player {player}, enter your move (0-8): '))

    if board[move] == ' ':
        board[move] = player
        if check_win(board, player):
            display_board(board)
            print(f'Player {player} wins!')
            break
        if is_game_over(board):
            display_board(board)
            print('It\'s a draw!')
            break
        player = 'O' if player == 'X' else 'X'
