"""Practice №8 "TicTacToe" game"""


def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("---------")

def check_winner(board):
    # Перевірка по горизонталі, вертикалі та діагоналям
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        try:
            row, col = map(int, input("Enter the coordinates: ").split())
        except ValueError:
            print("You should enter numbers!")
            continue

        if 1 <= row <= 3 and 1 <= col <= 3:
            if board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = current_player
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"{winner} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")

if __name__ == "__main__":
    main()
