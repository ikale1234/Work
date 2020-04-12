import pygame
import random

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Osu")
run = True
cs = []
addcir = 0
def drawcircles():
    for i in range(len(cs)):
        cs[i].draw(win)
    pygame.display.update()

class circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rad = 40
        self.rad2 = 80
        self.vis = True
    def draw(self, win):
        if self.vis:
            pygame.draw.circle(win, (0, 0, 255), (self.x, self.y), self.rad)
            pygame.draw.circle(win, (0, 0, 255), (self.x, self.y), self.rad2, 2)
        if self.rad2 <= 30:
            self.vis = False
while run:
    win.fill((255,255,255))
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #add circles
        addcir+=1
        for i in range(len(cs)):
            if cs[i].vis == False:
                cs.pop(i)
                break
        for i in range(len(cs)):
            cs[i].rad2-=1
        if addcir == 20:
            addcir = 0
            cs.append(circle(random.randrange(75, 725), random.randrange(75, 725)))
        


    drawcircles()
    pygame.display.update()
pygame.quit()