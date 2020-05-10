from tkinter import *
import sudoku

def entered():
    global current_i
    global current_j
    if (sudoku.checkAll(sudoku.gamegrid, current_i, current_j, int(box.get()))
        and sudoku.processgrid[current_i][current_j] == 0):
        buttons[current_i][current_j].config(text=box.get(), fg = 'black')


def selected(i,j):
    buttons[i][j].config(fg = 'red')
    global current_i
    global current_j
    current_i = i
    current_j = j

def guess():
    global current_i
    global current_j
    if(sudoku.processgrid[current_i][current_j]==0):
        buttons[current_i][current_j].config(text=box.get(), fg='blue')


window = Tk()
window.title("Sudoku")
window.geometry('345x500')

n = 9
m = 9

current_i = None
current_j = None

enterButton = Button(window, text="Enter", command= entered)
enterButton.grid(column = 6, row = 10)

guessButton = Button(window, text="Guess", command= guess)
guessButton.grid(column = 2, row = 10)

buttons = [[0]*m for i in range(n)]

# labels = [[0]*m for i in range(n)]


for i in range(9):
    for j in range(9):
        btn = Button(window, text="0", command= lambda row=i, col=j : selected(row,col))
        btn.config(width = 4, height = 2, bg='white')
        btn.grid(column = i, row = j)
        buttons[i][j] = btn

for i in range(9):
    for j in range(9):
        buttons[i][j].config(text= str(sudoku.gamegrid[j][i]))



box = Entry(window, width = 4)
box.grid(column=4, row=10)



if __name__ == "__main__":
    sudoku.processGrid(sudoku.gamegrid)
    window.mainloop()

# from tkinter import *
#
# def clicked():
#     res = "Welcome to " + txt.get()
#     lbl.configure(text=res)
#
# window = Tk()
#
# window.title("Welcome to LikeGeeks app")
# window.geometry('350x200')
#
# lbl = Label(window, text="Hello", font=("Arial Bold", 12))
# lbl.grid(column=0, row=0)
#
# btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
# btn.grid(column=2, row=0)
#
# txt = Entry(window,width=10)
# txt.grid(column=1, row=0)
# txt.focus()
#
#
#
# window.mainloop()

# import pygame
#
# pygame.init()
#
# screen = pygame.display.set_mode((640,480))
# background = pygame.Surface(screen.get_size())
#
# background.fill((255,255,255))
# background = background.convert()
#
# screen.blit(background, (0,0))
#
# clock = pygame.time.Clock()
#
# mainloop = True
# FPS = 30
# playtime = 0.0
#
# while mainloop:
#     milliseconds = clock.tick(FPS)
#     playtime+= milliseconds/1000.0
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             mainloop = False
#         elif event.type == pygame.KEYDOWN:
#             if eveent.key == pygame.K_ESCAPE:
#                 mainloop = False
#     text = "FPS: {0:.2f}  Playtime: {1:.2f}".format(clock.get_fps(),playtime)
#     pygame.display.set_caption(text)
#
#     pygame.display.flip()
#
# pygame.quit()
#
# print("This game was played for {0:.2f} seconds".format(playtime))
