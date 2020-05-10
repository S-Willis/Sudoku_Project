import pygame, sys, sudoku

WINDOWMULTIPLIER = 5
WINDOWSIZE = 81
WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
SQUARESIZE = (WINDOWSIZE * WINDOWMULTIPLIER) // 3
CELLSIZE = SQUARESIZE // 3
GRIDSIZE = 9

FPS = 10

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (200,200,200)

GRID = sudoku.gamegrid

def drawBox(coords):
    global CELLSIZE
    x = coords[0]
    y = coords[1]

    boxX = x*CELLSIZE
    boxY = y*CELLSIZE

    pygame.draw.rect(DISPLAYSURF,(0,0,255),(boxX,boxY,CELLSIZE,CELLSIZE),1)

def drawGrid():
    for x in range(0,WINDOWWIDTH,CELLSIZE):
        pygame.draw.line(DISPLAYSURF,GREY, (x,0), (x,WINDOWHEIGHT))
    for y in range(0,WINDOWHEIGHT,CELLSIZE):
        pygame.draw.line(DISPLAYSURF,GREY, (0,y),(WINDOWWIDTH,y))

    for x in range(0,WINDOWWIDTH,SQUARESIZE):
        pygame.draw.line(DISPLAYSURF,BLACK,(x,0), (x,WINDOWHEIGHT))
    for y in range(0,WINDOWHEIGHT,SQUARESIZE):
        pygame.draw.line(DISPLAYSURF,BLACK,(0,y),(WINDOWWIDTH,y))

def populateGrid():
    global CELLSIZE, GRID, BASICFONT,GREY
    x = CELLSIZE//2
    y = CELLSIZE//2
    for x_coord in range(9):
        for y_coord in range(9):
            value = GRID[y_coord][x_coord]
            cellSurf = BASICFONT.render(str(value), True, GREY)
            cellRect = cellSurf.get_rect()
            cellRect.topleft = (x+(x_coord*CELLSIZE),y+(y_coord*CELLSIZE))
            DISPLAYSURF.blit(cellSurf, cellRect)

def getClickSquare(coordinates):
    global CELLSIZE, GRIDSIZE
    x_square = 0
    y_square = 0
    x_coord = coordinates[0]
    y_coord = coordinates[1]

    ##X LOOP

    for x in range(GRIDSIZE):
        if(x_coord >= x*CELLSIZE and x_coord < (x+1)*CELLSIZE):
            x_square = x
            break

    ##Y LOOP
    for y in range(GRIDSIZE):
        if(y_coord >= y*CELLSIZE and y_coord < (y+1)*CELLSIZE):
            y_square = y
            break

    return (x,y)

def main():
    global DISPLAYSURF, FPSCLOCK,FPS
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Sudoku')
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 15
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    DISPLAYSURF.fill(WHITE)

    selection = None

    while True:

        mouse_clicked = False
        DISPLAYSURF.fill(WHITE)
        drawGrid()
        populateGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
                selection = getClickSquare(pygame.mouse.get_pos())
                drawBox(selection)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    num = 1
                elif event.key == pygame.K_2:
                    num = 2
                elif event.key == pygame.K_3:
                    num = 3
                elif event.key == pygame.K_4:
                    num = 4
                elif event.key == pygame.K_5:
                    num = 5
                elif event.key == pygame.K_6:
                    num = 6
                elif event.key == pygame.K_7:
                    num = 7
                elif event.key == pygame.K_8:
                    num = 8
                elif event.key == pygame.K_9:
                    num = 9

                print(num)
                if(sudoku.checkAll(GRID,selection[1],selection[0],num)):
                    GRID[selection[1]][selection[0]] = num

        pygame.display.flip()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
