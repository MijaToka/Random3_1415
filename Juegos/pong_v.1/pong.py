import pygame
import random
pygame.init()

#Variables

Width = 1000
Height = 600
Border = 10
IVelx = 1
IVely = 1
fps = 160
length = 100
radius = 15
Vel1,Vel2 = 0,0
dV1,dV2 = 2,2
##Colours

bgColour = pygame.Color('Black')
fgColour = pygame.Color('White')

#Def Objects


class Ball:
    Radius = radius
    def __init__(self,x,y,vx,vy):
        
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
            
    def show(self,colour):           
        global screen
        pygame.draw.circle(screen,colour,(self.x,self.y),self.Radius)
        
    def update(self): #Updates th position of the ball
        
        newx = self.x +self.vx
        newy = self.y + self.vy   
        self.show(bgColour)
        
        if (newy > Height - (Border + self.Radius)) \
            or (newy < Border + self.Radius):
            self.vy = -self.vy
        elif newx > Width - (Border + self.Radius) \
            and abs(newy - (Pad2Y + Paddle2.Length//2))  < Paddle2.Length//2:
                self.vx = -(self.vx + 1)
                self.vy += random.randint(-5,5)
        elif newx < (Border + self.Radius) \
            and abs(newy - (Pad1Y + Paddle2.Length//2))  < Paddle1.Length//2:
                self.vx = -(self.vx + 1)
                self.vy += random.randint(-5,5)
        elif newx > Width :
            self.vx = 0 ;self.vy = 0
            self.x -= self.Radius 
        elif newx < 0: 
            self.vx = 0 ;self.vy = 0
            self.x += self.Radius
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        self.show(fgColour)

            
class Paddle1:
    global event
    Length = length
    def __init__(self,x,y):
        self.x = x
        self.y = y
   
    def show(self,colour):           
        global screen
        pygame.draw.rect(screen,colour,pygame.Rect((self.x,self.y),(Border,self.Length)))
    
    def update(self,d1):
        self.show(bgColour)        
        self.y += d1
        self.show(fgColour)
        return self.y
        
class Paddle2:    
    Length = length
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self,colour):           
        global screen
        pygame.draw.rect(screen,colour,pygame.Rect((self.x,self.y),(Border,self.Length)))
    
    def update(self,d2):
        self.show(bgColour)
        self.y += d2
        self.show(fgColour)
        return self.y
#Scene

screen = pygame.display.set_mode([Width,Height])
clock = pygame.time.Clock()

##Borders

pygame.draw.rect(screen,fgColour,pygame.Rect((0,0),(Width,Border)))
pygame.draw.rect(screen,fgColour,pygame.Rect((0,Height-Border),(Width,Border)))

##Initial state

ballPlay = Ball(Width//2,Height//2,IVelx,IVely)
Paddle1Play = Paddle1(0,Height//2 - length//2)
Paddle2Play = Paddle2(Width - Border,Height//2 - length//2)
##Display

ballPlay.show(fgColour)
Paddle1Play.show(fgColour)
Paddle2Play.show(fgColour)

run = True
while run:     
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Vel1 -= dV1
            if event.key == pygame.K_s:
                Vel1 += dV1
            if event.key == pygame.K_UP:
                Vel2 -= dV2
            if event.key == pygame.K_DOWN:
                Vel2 += dV2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                Vel1 = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Vel2 = 0
    Paddle1Play.update(Vel1)
    Paddle2Play.update(Vel2)
    Pad1Y = Paddle1Play.update(Vel1)
    Pad2Y = Paddle2Play.update(Vel2)
    ballPlay.update()
    
    pygame.display.flip()
    
    event = pygame.event.poll()    
    if event.type == pygame.QUIT:
        run = False
    

pygame.quit()
    
    


    
