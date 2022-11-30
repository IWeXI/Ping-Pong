import pygame
from random import *



win_w = 1200
win_h = 650

fps = 60

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imageSrc, x, y, width, height, speed=0):
        super().__init__()
        self.image = pygame.image.load(imageSrc)
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update(self):
        wind.blit(self.image, self.rect)

    
pygame.init()

class Player (GameSprite):
    move_left = False
    move_right = False
    

    def control(self, events):
        
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    self.move_left = True
                    
                if e.key == pygame.K_RIGHT:
                    self.move_right = True
                    
                
                    
                    

            if e.type == pygame.KEYUP:        
                if e.key == pygame.K_LEFT:  
                    self.move_left = False
                    
                if e.key == pygame.K_RIGHT:
                    self.move_right = False 
                    

        
        if self.move_left == True:
            self.rect.x -= 7
        if self.move_right == True:
            self.rect.x += 7

        if self.rect.x >= 1125:
            self.move_right = False
        if self.rect.x <= 0:
            self.move_left = False
        

wind = pygame.display.set_mode((win_w, win_h))
background = GameSprite("фон.png", 0, 0, win_w, win_h)
background.update()

clock = pygame.time.Clock()


game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

    background.update()

    pygame.display.update()
    clock.tick(60)
    pygame.display.flip()
