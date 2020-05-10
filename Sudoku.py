import pygame, sys

class Window():

    def __init__(self,game):
        self.game = game
        self.WINDOWMULTIPLIER = 5
        self.WINDOWSIZE = 81
        self.WINDOWWIDTH = self.WINDOWSIZE * self.WINDOWMULTIPLIER
        self.WINDOWHEIGHT = self.WINDOWSIZE * self.WINDOWMULTIPLIER
        self.SQUARESIZE = self.WINDOWWIDTH // 3
        self.CELLSIZE = self.SQUARESIZE//3
        self.GRIDSIZE = 9
        self.gamegrid = game.gamegrid
        self.FPS = 10
        self.BASICFONT = None
        self.DISPLAYSURF = None

    def drawBox(self, coords):
        x = coords[0]
        y = coords[1]

        box_x = x*self.CELLSIZE
        box_y = y*self.CELLSIZE

        pygame.draw.rect(self.DISPLAYSURF,(0,0,255),(box_x,box_y,self.CELLSIZE,self.CELLSIZE),1)

        return

    def drawGrid(self):
        for x in range(0,self.WINDOWWIDTH,self.CELLSIZE):
            pygame.draw.line(self.DISPLAYSURF,(200,200,200), (x,0), (x,self.WINDOWHEIGHT))
        for y in range(0,self.WINDOWHEIGHT,self.CELLSIZE):
            pygame.draw.line(self.DISPLAYSURF,(200,200,200), (0,y), (self.WINDOWWIDTH,y))

        for x in range(0,self.WINDOWWIDTH,self.SQUARESIZE):
            pygame.draw.line(self.DISPLAYSURF,(0,0,0), (x,0), (x,self.WINDOWHEIGHT))
        for y in range(0,self.WINDOWHEIGHT,self.SQUARESIZE):
            pygame.draw.line(self.DISPLAYSURF,(0,0,0), (0,y), (self.WINDOWWIDTH,y))
        return

    def populateGrid(self):
        x = self.CELLSIZE//2
        y = self.CELLSIZE//2

        for x_coord in range(self.GRIDSIZE):
            for y_coord in range(self.GRIDSIZE):
                value = self.game.gamegrid[y_coord][x_coord]
                cellSurf = self.BASICFONT.render(str(value), True, (0,0,0))
                cellRect = cellSurf.get_rect()
                cellRect.center = (x+(x_coord*self.CELLSIZE),y+(y_coord*self.CELLSIZE))
                self.DISPLAYSURF.blit(cellSurf,cellRect)

        return

    def getClickedSquare(self,coordinates):

        x_coord = coordinates[0]
        y_coord = coordinates[1]

        x_square = 0
        y_square = 0

        for x in range(self.GRIDSIZE):
            if(x_coord >= x*self.CELLSIZE and x_coord < (x+1)*self.CELLSIZE):
                x_square = x
                break

        for y in range(self.GRIDSIZE):
            if(y_coord >= y*self.CELLSIZE and y_coord < (y+1)*self.CELLSIZE):
                y_square = y
                break

        return (x,y)

    def run(self):
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH,self.WINDOWHEIGHT))
        pygame.display.set_caption('sudoku')
        self.DISPLAYSURF.fill((255,255,255))
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 15)

        selection = None

        while True:
            mouse_clicked = False
            self.DISPLAYSURF.fill((255,255,255))
            self.drawGrid()
            self.populateGrid()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True
                    selection = self.getClickedSquare(pygame.mouse.get_pos())
                    self.drawBox(selection)
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
                    if(self.game.checkAll(selection[1],selection[0],num)):
                        self.game.gamegrid[selection[1]][selection[0]] = num
            pygame.display.flip()
            FPSCLOCK.tick(self.FPS)


        return

import Game

if __name__ == '__main__':

    game = Game.Game([[5,3,0,0,7,0,0,0,0],
               [6,0,0,1,9,5,0,0,0],
               [0,9,8,0,0,0,0,6,0],
               [8,0,0,0,6,0,0,0,3],
               [4,0,0,8,0,3,0,0,1],
               [7,0,0,0,2,0,0,0,6],
               [0,6,0,0,0,0,2,8,0],
               [0,0,0,4,1,9,0,0,5],
               [0,0,0,0,8,0,0,7,9]])

    print(game.fixgrid)

    window = Window(game)

    window.run()
