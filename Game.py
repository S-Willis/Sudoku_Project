import sys

def processGrid(grid):
    processgrid = [[0]*len(grid) for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] != 0):
                processgrid[i][j] = 1;
    return processgrid


class Game:

    def __init__(self, gamegrid):
        self.initialgrid = gamegrid
        self.gamegrid = gamegrid
        self.grid_dim = len(self.gamegrid)
        self.fixgrid = processGrid(self.gamegrid)

    def checkCol(self, col, val):
        for i in range(self.grid_dim):
            if self.gamegrid[i][col] == val:
                # print('column ' + str(col) + ' row ' + str(i))
                return False
        return True

    def checkRow(self, row, val):
        for j in range(self.grid_dim):
            if self.gamegrid[row][j] == val:
                # print('row ' + str(row) + ' column ' + str(j))
                return False
        return True

    def checkBox(self, col, row, val):

        i=0
        j=0

        if(col<(self.grid_dim/3)):
            i=0
        elif(col<2*(self.grid_dim/3)):
            i=3
        elif(col<self.grid_dim):
            i=6
        else:
            print("Error, column higher than grid dim")

        if(row<(self.grid_dim/3)):
            j=0
        elif(row<2*(self.grid_dim/3)):
            j=3
        elif(row<self.grid_dim):
            j=6
        else:
            print("Error, row higher than grid dim")

        for x in range(i,i+3):
            for y in range(j,j+3):
                if self.gamegrid[y][x] == val:
                    # print('box, ' + str(x) + ' ' + str(y))
                    return False

        return True


    def checkAll(self, col, row, val):
        if self.fixgrid[row][col]!=0:
            print('fixgrid error' + str(self.fixgrid[row][col]) + ' '+  str((row,col)))
        return(self.fixgrid[row][col]==0 and
               self.checkCol(col,val) and
               self.checkRow(row,val) and
               self.checkBox(col,row,val))

    def printGrid(self):
        grid = self.gamegrid
        print('\n')
        for i in range(len(grid)):
            toPrint = ''
            for j in range(len(grid[0])):
                toPrint = toPrint + str(grid[i][j])
                if(j<8):
                    toPrint = toPrint + ' '
                    if((j+1)%3==0):
                        toPrint = toPrint + '| '
            print(toPrint)
            if((i+1)%3==0 and i!=8):
                print(21*'-')
        print('')
        return


    def solve(self):

        self.gamegrid = self.initialgrid

        row=0
        col=0

        backtracking = False


        while(row<9 and col<9):

            backtracking = False

            if(self.fixgrid[row][col]==0):
                # self.printGrid()
                current_val = self.gamegrid[row][col]

                if(current_val<9):
                    current_val = current_val + 1
                    # print('Val < 9 Val=' + str(current_val))
                    # self.gamegrid[row][col] = current_val
                    store_val = current_val
                    if(self.checkAll(col,row,current_val)):
                        self.gamegrid[row][col] = current_val
                    else:
                        self.gamegrid[row][col] = current_val
                        continue
                elif(current_val==9 and self.checkAll(col,row,current_val)==False):
                    # print('9 but wrong')
                    self.gamegrid[row][col] = 0
                    backtracking=True




            if(backtracking):
                col = col - 1

                if(col==-1):
                    row = row - 1
                    col = 8
                if(row==-1):
                    print("No solution")
                    return
            else:

                col = col + 1

                if(col==9):
                    row = row + 1
                    col = 0
                if(row==9):
                    print("Solution!")
                    self.printGrid()
                    return

        return





def main():

    # game = Game([[0,2,0,4,5,6,7,8,9],
    #             [4,5,7,0,8,0,2,3,6],
    #             [6,8,9,2,3,7,0,4,0],
    #             [0,0,5,3,6,2,9,7,4],
    #             [2,7,4,0,9,0,6,5,3],
    #             [3,9,6,5,7,4,8,0,0],
    #             [0,4,0,6,1,8,3,9,7],
    #             [7,6,1,0,4,0,5,2,8],
    #             [9,3,8,7,2,5,0,6,0]])

    game = Game([[5,3,0,0,7,0,0,0,0],
               [6,0,0,1,9,5,0,0,0],
               [0,9,8,0,0,0,0,6,0],
               [8,0,0,0,6,0,0,0,3],
               [4,0,0,8,0,3,0,0,1],
               [7,0,0,0,2,0,0,0,6],
               [0,6,0,0,0,0,2,8,0],
               [0,0,0,4,1,9,0,0,5],
               [0,0,0,0,8,0,0,7,9]])

    ROW = None
    COL = None
    VAL = None

    print("Welcome to sudoku.")

    print("Play or solve? P or S")

    Solve = input()

    if Solve == 'S':
        game.solve()
        sys.exit()

    while(True):
        game.printGrid()

        print("Enter row: ")
        ROW = int(input())
        print("Enter col: ")
        COL = int(input())
        print("Enter val:" )
        VAL = int(input())

        if(game.fixgrid[ROW][COL] != 0):
            print("Invalid Square choice")
            continue
        elif (game.checkAll(COL,ROW,VAL)):
            game.gamegrid[ROW][COL] = VAL
        else:
            print("Incorrect value choice")

if __name__ == '__main__':
    main()
