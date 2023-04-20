import sys
import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Rectangle(20,20,100,100)
pos_x = 100
pos_y = 100

run = True
while(run):
    screen.fill((255, 255, 255))
    btn.draw(screen) 
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            btn.y -= 10
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            btn.x -=10
       
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            btn.y += 10
     

        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            btn.x +=10
    pg.display.update()