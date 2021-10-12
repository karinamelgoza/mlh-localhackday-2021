board = [['', '', ''], ['', '', ''], ['', '', '']]
player = 'X'


def printBoard(board):
    for line in board:
        print(line)


def makeMove():
    global player
    x = int(input('Player '+player + ', What is the X coordinate?'))
    y = int(input('What is the Y coordinate?'))

    while board[y][x] != '':
        print('You must choose an empty spot')
        x = int(input('Player '+player + ', What is the X coordinate?'))
        y = int(input('What is the Y coordinate?'))

    if player == 'X':
        board[y][x] = 'X'
        player = 'O'
    else:
        board[y][x] = 'O'
        player = 'X'


def isWin():
    global player
    if player == 'X':
        p = "O"
    else:
        p = "X"

    for col in range(len(board)):
        win = True
        for row in range(len(board)):
            if board[col][row] != p:
                win = False
                break
        if win:
            return True

    for col in range(len(board)):
        win = True
        for row in range(len(board)):
            if board[row][col] != p:
                win = False
                break
        if win:
            return True

    win = True
    for c in range(3):
        if board[c][c] != p:
            win = False
            break
    if win:
        return True
    win = True
    for c in range(len(board)):
        if board[row][len(board)-1-row] != p:
            win = False
            break
    if win:
        return True

    return False


def main():
    gamewon = False
    while gamewon == False:
        printBoard(board)
        makeMove()
        gamewon = isWin()
    print('Game Over')
    printBoard(board)


main()
