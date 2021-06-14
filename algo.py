'''
board = [[4, 6, 7, 9, 2, 1, 3, 5, 8],
         [8, 9, 5, 4, 7, 3, 2, 6, 1],
         [2, 3, 1, 8, 6, 5, 7, 4, 9],
         [5, 1, 3, 6, 9, 8, 4, 2, 7],
         [9, 2, 8, 7, 0, 4, 6, 1, 3],
         [7, 4, 6, 1, 3, 2, 9, 8, 5],
         [3, 5, 4, 2, 8, 7, 1, 9, 6],
         [1, 8, 9, 3, 4, 6, 5, 7, 2],
         [6, 7, 2, 5, 1, 9, 8, 3, 4]]

board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

board = [[2, 0, 8, 0, 0, 3, 7, 5, 0],
         [0, 0, 6, 0, 7, 1, 8, 0, 3],
         [7, 5, 0, 0, 4, 0, 1, 0, 9],
         [5, 3, 0, 0, 0, 0, 0, 0, 8],
         [6, 0, 9, 0, 1, 0, 2, 0, 5],
         [0, 0, 7, 4, 9, 0, 0, 0, 1],
         [0, 0, 2, 1, 0, 0, 3, 0, 7],
         [0, 0, 5, 6, 0, 0, 4, 9, 0],
         [3, 7, 0, 0, 8, 0, 0, 0, 0]]
'''

import time

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def showBoard(board):
    print('-' * 27)
    s = ""
    for i in range(9):
        for j in range(9):
            s += str(board[i][j])
            s += "  "
            if j == 2 or j == 5:
                s += " "
        s += "\n"
        if i == 2 or i == 5:
            s += "\n"
    print(s)
    
    print('-' * 27)


def solve(board, show=False):
    if show:
        showBoard(board)
        
    empty = checkEmpty(board)
    if empty:
        row, col = empty

        for i in range(1, len(board) + 1):
            back = True

            if check(board, (row, col), i):
                board[row][col] = i
                back = False
                if solve(board, show):
                    return True
                else:
                    back = True

        if back:
            board[row][col] = 0
            return False

    else:
        return True
        


def checkEmpty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

    return None


def check(board, pos, num):
    for i in range(len(board)):
        if board[pos[0]][i] == num:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num:
            return False

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True

if __name__ == '__main__':
    start = time.time()
    solve(grid, True)
    print('Solved in ', (time.time() - start))
    showBoard(grid)
