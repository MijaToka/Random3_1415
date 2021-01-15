# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:51:49 2020

@author: Admin
"""
import pygame
pygame.init()
#variables
WIDTH= 1000
HEIGHT = 1000
RADIUS = 15
X , Y = 500,500
VelX, VelY = 0,0
dVx,dVy = 1,1
fgColour = pygame.Color('red')
bgColour = pygame.Color('black')
#screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])

class Ball:
    Radius = RADIUS
    def __init__(self,x,y,vx,vy):
        
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
            
    def show(self,colour):           
        global screen
        pygame.draw.circle(screen,colour,(self.x,self.y),self.Radius)
        
    def update(self,dx,dy):
        self.show(bgColour)
        self.x += dx
        self.y += dy
        self.show(fgColour)
        
playBall = Ball(X,Y,VelX,VelY)

running = True

while running:
    
    playBall.update(VelX, VelY)            
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                VelX -= dVx
            if event.key == pygame.K_RIGHT:
                VelX += dVx
            if event.key == pygame.K_UP:
                VelY -= dVy
            if event.key == pygame.K_DOWN:
                VelY += dVy
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                VelX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                VelY = 0
                
    
    
pygame.quit()