import pygame

width = 10
height = 10

class Cell:
    def __init__(self,xpos,ypos,centreNumber):
        self.xpos = xpos
        self.ypos = ypos
        self.size = 1
        x = width
        y = height
        self.centreNum = centreNumber
        self.smallList = []

    def draw_big(self,text):
        fw,fh = self.font.size(text)
        surface = self.font.render(text,True,(0,255,0))
        self.screen.blit(surface, ((self.width - fw)//2, (self.height - fh) // 2))

    def draw_small(self,text):
        fw,fh = self.font.size(text)
        surface = self.font.render(text,True,(0,255,0))
        self.screen.blit(surface, ((self.width - fw)//2, (self.height - fh) // 2))

    def draw(self):
