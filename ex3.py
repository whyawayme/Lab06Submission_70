class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(51,255,255),(self.x,self.y,self.w,self.h))
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

class InputBox:


    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)

class Inputnum:


    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if event.unicode.isnumeric():
                        self.text += event.unicode
                    else:
                        return False
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)
        
import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') 
COLOR_ACTIVE = pg.Color('dodgerblue2')    
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_box3 = Inputnum(100, 300, 140, 32) # สร้าง InputBox2
input_boxes = [input_box1, input_box2,input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
firstObject = Rectangle(500,300,150,50) 

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('firstname', True, (0,0,204)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
textRect.center = (200, 80)

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text1 = font.render('lastname', True, (0,0,204)) # (text,is smooth?,letter color,background color)
textRect1 = text1.get_rect() # text size
textRect1.center = (200, 180)

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text2 = font.render('age', True, (0,0,204)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (200, 280)

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text3 = font.render('submit', True, (0,0,204)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (573, 325)

while run:
    screen.fill((255, 255, 255))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    if firstObject.isMouseOn():
        if firstObject.isMousepress():
            font = pg.font.Font('freesansbold.ttf', 28) # font and fontsize
            text3 = font.render('Hello  '+str(input_box1.text)+' '+str(input_box2.text)+'  '+ 'You are  ' +str(input_box3.text)+ ' '+'years old.', True, (0,0,204)) # (text,is smooth?,letter color,background color)
            textRect3 = text3.get_rect() # text size
            textRect3.center = (400,450 )


    firstObject.draw(screen)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    pg.time.delay(1)
    pg.display.update()