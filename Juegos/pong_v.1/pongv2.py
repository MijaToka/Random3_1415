import pygame
import random
import os
import time

pygame.font.init()


#Variables
WIDTH, HEIGHT = 1000 , 750
p1_score = 0
p2_score = 0
#main_font = pygame.font.SysFont('')
#scene

WIN = pygame.display.set_mode([WIDTH,HEIGHT])


#Objects

class Ball():
    RADIUS = 15
    def __init__(self,x,y,vel_x,vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        
    def show(self,window):
        
        pygame.draw.circle(window,FG,(self.x,self.y),self.RADIUS)
    
    #def move(self):
        


#Game runner
def pongv2():
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    
    def refresh():
        
        pygame.display.flip()
        Ball.show(WIN)  
    
    while running :
        clock.tick(FPS)
        refresh()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                key = pygame.key.get_pressed()
                #if event.type == pygame.KEYDOWN:
                    
                    #if key[pygame.K_UP]:
                        
                    #if key[pygame.K_DOWN]:
                        
                    #if key[pygame.K_w]:
                        
                    #if key[pygame.K_s]:
                    
    pygame.quit()   


