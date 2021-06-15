import pygame as pg
from time import sleep
import algo
import generator


BLACK = (20, 20, 20)
WHITE = (245, 245, 245)
DARKGRAY = (169, 169, 169)
GRAY = (105, 105, 105)


def grid(screen):
    pg.draw.rect(screen, DARKGRAY, pg.Rect(8, 8, 460, 460), width=1)

    for i in range(3):
        for j in range(3):
            pg.draw.rect(screen, DARKGRAY, pg.Rect(11 + 152 * i, 11 + 152 * j, 150, 150), width=1)

    for i in [50, 100, 202, 252, 354, 404]:
        for j in [0, 152, 304]:
            pg.draw.line(screen, WHITE, (i + 11, j + 11), (i + 11, j + 149 + 11), width=1)
            pg.draw.line(screen, WHITE, (j + 11, i + 11), (j + 149 + 11, i + 11), width=1)


def show(screen, font, board, ogboard):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != 0:
                col = GRAY
                if ogboard[j][i] == 0:
                    col = WHITE
                    
                screen.blit(font.render(str(board[j][i]), True, col), (11 + 14 + (50 * i) + (3 * (i // 3)), 11 + 3 + (50 * j) + (3 * (j // 3))))


def click(screen, pos):
    if 11 < pos[0] < 464 and 11 < pos[1] < 464:
        box = ((pos[0] - 11) // 151, (pos[1] - 11) // 151)
        inbox = ((pos[0] - 11) // 50) % 3, ((pos[1] - 11) // 50) % 3

        pg.draw.rect(screen, DARKGRAY, pg.Rect(13 + inbox[0] * 50 + box[0] * 152, 13 + inbox[1] * 50 + box[1] * 152, 47, 47), width=1)


def checkClick(po):
    box = ((po[0] - 11) // 151, (po[1] - 11) // 151)
    inbox = ((po[0] - 11) // 50) % 3, ((po[1] - 11) // 50) % 3

    return box, inbox


def check(board):
    if not algo.checkEmpty(board):
        for i in range(len(board)):
            for k in range(1, 10):
                if board[i][:].count(k) > 1:
                    return False
                if board[:][i].count(k) > 1:
                    return False

        for i in range(len(board) // 3):
            for j in range(len(board) // 3):
                block = []
                for k in range(len(board) // 3):
                    for l in range(len(board) // 3):
                        block.append(board[i * 3 + k][j * 3 + l])

                for k in range(1, 10):
                    if block.count(k) > 1:
                        return False


        return True

    else:
        return None


def play():
    pencil = False
    sol = False
    last = []

    ogboard = generator.getBoard()
    
    board = [x[:] for x in ogboard]
    sboard = [x[:] for x in ogboard]

    algo.solve(sboard)

    pg.init()
    screen = pg.display.set_mode((476, 476))
    pg.display.set_caption('Sudoku')
    pg.display.set_icon(pg.image.load('icon.png'))

    font = pg.font.SysFont("microsoftsansserif", 40)

    run = True
    pos = None
    s = 0
    while run:
        screen.fill(BLACK)

        grid(screen)
        show(screen, font, board, ogboard)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if not sol:
                if event.type == pg.MOUSEBUTTONUP:
                    if not pos:
                        pos = pg.mouse.get_pos()
                    else:
                        if checkClick(pos) == checkClick(pg.mouse.get_pos()):
                            pos = None
                        else:
                            pos = pg.mouse.get_pos()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_s:
                        sol = True
                        board = [x[:] for x in ogboard]
                    if event.key == pg.K_p:
                        pencil = not pencil  # Add pencil functioning
                    if event.key == pg.K_u:
                        if len(last) > 0:
                            board[last[-1][0]][last[-1][1]] = last[-1][2]
                            del last[-1]
                    if pos:
                        if 11 < pos[0] < 464 and 11 < pos[1] < 464:
                            bo = (pos[0] - 11) // 50, (pos[1] - 11) // 50
                            if ogboard[bo[1]][bo[0]] == 0:
                                if event.key == pg.K_e:
                                    last.append([bo[1], bo[0], board[bo[1]][bo[0]]])
                                    board[bo[1]][bo[0]] = 0
                                if 49 <= event.key <= 57:
                                    last.append([bo[1], bo[0], board[bo[1]][bo[0]]])
                                    board[bo[1]][bo[0]] = event.key - 48

        if sol:
            pos = None
            i, j = s // 9, s % 9
            board[i][j] = sboard[i][j]
            s += 1

        if pos:
            click(screen, pos)

        if check(board):
            #print('Solved!')
            
            screen.fill(BLACK)
            grid(screen)
            show(screen, font, board, ogboard)
            pg.display.update()
            
            sleep(2)
            run = False
        
        pg.display.update()

    pg.quit()


if __name__ == '__main__':
    play()
