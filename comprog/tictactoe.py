from random import randrange

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            row, column = divmod(move - 1, 3)
            if board[row][column] in ['X', 'O']:
                print("This field is already occupied. Choose another one.")
                continue
            board[row][column] = 'O'
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def make_list_of_free_fields(board):
    free_fields = []
    for r in range(3):
        for e in range(3):
            if board[r][e] not in ['X', 'O']:
                free_fields.append((r, e))
    return free_fields

def victory_for(board, sign):
    win = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combo in win:
        if all(board[r][e] == sign for r, e in combo):
            return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = randrange(len(free_fields))
        row, column = free_fields[move]
        board[row][column] = 'X'

print("Welcome to Tic Tac Toe!")
print("You are 'O' and the computer is 'X'.")
print("X goes first.")

board[1][1] = 'X'
display_board(board)

game_over = False

while not game_over:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("Congratulations! You won!")
        game_over = True
        break
    if not make_list_of_free_fields(board):
        print("It's a draw!")
        game_over = True
        break

    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer wins! Better luck next time.")
        game_over = True
        break
    if not make_list_of_free_fields(board):
        print("It's a draw!")
        game_over = True
        break