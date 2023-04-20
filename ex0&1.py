import sys 
import pygame as pg
red=(255,0,0)
gray=(128,128,128)
purple=(128,0,128)
color=red
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        (mouse_x,mouse_y)=pg.mouse.get_pos()
        if self.x<=mouse_x and mouse_x <= self.x+self.w and self.y<=mouse_y<=self.y+self.h:
            return True
        else:
            return False

    def isMousepress(self):
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False

pg.init()
run = True
win_x, win_y = 800, 480
btn = Button(20,20,100,100)
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(20,20,100,100) 

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        color=gray
        if btn.isMousepress():
            color=purple

    else :
        color = red
    firstObject.draw(screen) 
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
