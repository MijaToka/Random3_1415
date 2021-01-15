import pygame
import random 
pygame.init()
pygame.font.init()
#Variables

Width = 1000
Height = 600
Border = 10
IVelx = 3
IVely = 0
fps = 60
length = 100
radius = 15
counter = 0
main_font = pygame.font.SysFont('comicsans', 50)
lost_font = pygame.font.SysFont('comicsans', 100)
score_font = pygame.font.SysFont('comicsans', 50)

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
        global counter,lost
        newx = self.x +self.vx
        newy = self.y + self.vy   
        self.show(bgColour)
        
        if (newy > Height - (Border + self.Radius)) \
            or (newy < Border + self.Radius):
            self.vy = -self.vy
        elif newx < Border + self.Radius:
            self.vx = -self.vx
        elif newx > Width - (Border + self.Radius) \
            and abs(newy - paddley)  < Paddle.Length//2:
                self.vx = -(self.vx + 1)
                self.vy += random.randint(-5,5)
                counter += 1
        elif newx > Width + self.Radius:
            self.vx = 0
            self.vy = 0
            self.x = -self.Radius 
            self.y = -self.Radius
            lost = True
            
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        self.show(fgColour)

            
class Paddle:
    global event
    Length = length
    def __init__(self,x,y):
        self.x = x
        self.y = y
   
    def show(self,colour):           
        global screen
        pygame.draw.rect(screen,colour,pygame.Rect((self.x,self.y),(Border,self.Length)))
    
    def update(self):
        newy = pygame.mouse.get_pos()[1]
        PaddlePlay.show(bgColour)
        if newy > Border:
            self.y = newy - self.Length//2
        elif newy < (Height - Border - self.Length):
            self.y = newy - self.Length//2
        else:
            self.y = self.y
            
        PaddlePlay.show(fgColour)

#Scene

screen = pygame.display.set_mode([Width,Height])
clock = pygame.time.Clock()

##Borders

pygame.draw.rect(screen,fgColour,pygame.Rect((0,0),(Width,Border)))
pygame.draw.rect(screen,fgColour,pygame.Rect((0,Height-Border),(Width,Border)))
pygame.draw.rect(screen,fgColour,pygame.Rect((0,0),(Border,Height)))

##Initial state

lost = False 
ballPlay = Ball(Width//2,Height//2,IVelx,IVely)
PaddlePlay = Paddle(Width - Border,Height//2 - length//2)

##Display

ballPlay.show(fgColour)
PaddlePlay.show(fgColour)
menu_count = 0
lost_count = 0
run = True


while run:     
    
    clock.tick(fps) 
    
    pygame.display.update()
    
    if lost == True:
        
        screen.fill(bgColour)
        lost_label = lost_font.render('GAME OVER', 1, fgColour)
        screen.blit(lost_label,(Width//2 - lost_label.get_width()//2 , Height//2 - lost_label.get_height()//2))
        score_label = score_font.render(f'Score: {counter}', 1, fgColour)
        screen.blit(score_label,(Width//2 - score_label.get_width()//2 , Height*2//3 - score_label.get_height()//2))
        
        lost_count += 1

    if lost:
        if lost_count > fps * 5:
                run = False
    
    PaddlePlay.update()
    draw_counter = main_font.render(f"Score: {counter}", 1, bgColour)
    screen.blit(draw_counter, (Width//2 - draw_counter.get_width()//2 , Border + draw_counter.get_height()//2))
    ballPlay.update()
    draw_counter = main_font.render(f"Score: {counter}", 1, fgColour)
    screen.blit(draw_counter, (Width//2 - draw_counter.get_width()//2 , Border + draw_counter.get_height()//2))
    
    paddley = pygame.mouse.get_pos()[1]
    pygame.display.flip()
    
    event = pygame.event.poll()    
    if event.type == pygame.QUIT:
        run = False
    
    
        
    

pygame.quit()