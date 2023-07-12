from random import randrange
board = [[1, 2, 3], 
         [4, 5, 6],
         [7, 8, 9]]
def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != "X" and board[row][col] != "O":
                free_fields.append((row, col))
    return free_fields

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")
def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if not free_fields:
        print("No more free fields. The game is a tie.")
        return
    row, col = free_fields[randrange(len(free_fields))]
    board[row][col] = "X"
    display_board(board)
    
def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    if not free_fields:
        print("No more free fields. The game is a tie.")
        return
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Enter a number between 1 and 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == "X" or board[row][col] == "O":
                print("This cell is already occupied. Choose another one.")
                continue
            board[row][col] = "O"
            display_board(board)
            return
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.") 
ef victory_for(board, sign):
    



draw_move(board)
enter_move(board)
