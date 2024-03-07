def print_board(board):
    for row in board:
        print(" |".join(row))
        print("_" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
        for col in range(3):
            return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        return False
    
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
        return True
    
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:

        print_board(board)
        row = int(input(f"player{current_player}, 
                        enter row(0, 1, or 2):"))
        
        if board[row][col] != " ":
            print("That position is already taken. Please try again.")
            continue
        board[row][col] = current_player
        if check_winner(board, current_player):

            print_board(board)

            print(f"Player{current_player} Wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("You have tied!")
            break

            current_player = "O"
        else: current_player = "X"
            
        tic_tac_toe()