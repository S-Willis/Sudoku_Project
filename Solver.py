from sudoku import *

def solve(grid, processgrid):
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] != 0:
    #
    i, j = 0

    while(i!=9 and j!=9):
        if processgrid[i][j]==0:
            if k!=9 :
                k = grid[i][j] + 1
                while(checkAll(grid, i, j, k) != True):
                    k += 1
                grid[i][j] = k
            else:
                i = i-1
                if(i==-1):
                    i = 0
                    j = j-1
            continue
        i = i + 1
        if(i==9):
            i = 0
            j = j + 1
