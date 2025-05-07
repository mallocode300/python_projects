def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
            
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
            
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
        
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    # Initialize empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Enter moves using numbers 1-9 (left to right, top to bottom)")
    print("Example board with positions:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("\nLet's begin!\n")
    
    while True:
        print_board(board)
        print(f"\nPlayer {current_player}'s turn")
        
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Please enter a number between 1 and 9")
                    continue
                    
                row = move // 3
                col = move % 3
                
                if board[row][col] != " ":
                    print("That position is already taken!")
                    continue
                    
                board[row][col] = current_player
                break
                
            except ValueError:
                print("Please enter a valid number!")
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"\nPlayer {current_player} wins!")
            break
            
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break
            
        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
