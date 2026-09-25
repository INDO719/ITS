def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings

def row_winner(board):
    return any(winning_line(row) for row in board)

def column_winner(board):
    return row_winner(zip(*board))

def main_diagonal_winner(board):
    return winning_line(row[i] for i, row in enumerate(board))

def diagonal_winner(board):
    return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'

def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))

def make_board(size):
    return [[' '] * size for _ in range(size)]

def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")

def draw(board):
    cnt = [1
           for y in range(len(board))
           for x in range(len(board))
           if board[y][x] != " "
           ]
    return sum(cnt) == len(board) ** 2

def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    players = (player1, player2)
    s = 0
    while True:
        play_move(board, players[s % 2])
        if winner(board):
            print_winner(players[s % 2])
            break
        if draw(board):
            print_draw()
            break
        s += 1


def main():
    play_game(3, 'X', 'O')


if __name__ == '__main__':
    main()
