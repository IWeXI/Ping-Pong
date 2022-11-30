import pygame
from time import *
from random import *



win_w = 1200
win_h = 650

fps = 60



class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imageSrc, x, y, width, height, speed_x = 0, speed_y = 0):
        super().__init__()
        self.image = pygame.image.load(imageSrc)
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        wind.blit(self.image, self.rect)

    
pygame.init()

class Player (GameSprite):
    move_up1 = False
    move_down1 = False

    

    def control(self, events):
        
        for e in events:
            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_w:
                    self.move_up1 = True

                if e.key == pygame.K_s:
                    self.move_down1 = True
                    

            if e.type == pygame.KEYUP:        
                if e.key == pygame.K_w:  
                    self.move_up1 = False
                    
                if e.key == pygame.K_s:
                    self.move_down1 = False 

        
        if self.move_up1 == True:
            self.rect.y -= self.speed_y
        if self.move_down1 == True:
            self.rect.y += self.speed_y

        if self.rect.y >= 480:
            self.move_down1 = False
        if self.rect.y <= 70:
            self.move_up1 = False

class Player2 (GameSprite):
    move_up2 = False
    move_down2 = False
    

    def control(self, events):
        
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.move_up2 = True

                if e.key == pygame.K_DOWN:
                    self.move_down2 = True


            if e.type == pygame.KEYUP:        

                if e.key == pygame.K_UP:  
                    self.move_up2 = False
                    
                if e.key == pygame.K_DOWN:
                    self.move_down2 = False 
                    

        
        if self.move_up2 == True:
            self.rect.y -= self.speed_y
        if self.move_down2 == True:
            self.rect.y += self.speed_y

        if self.rect.y >= 480:
            self.move_down2 = False
        if self.rect.y <= 70:
            self.move_up2 = False


class Ball(GameSprite):
    def move_ball(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 80 or self.rect.y >= 550:
            self.speed_y = self.speed_y * -1
        
        

        

wind = pygame.display.set_mode((win_w, win_h))
background = GameSprite("фон.png", 0, 0, win_w, win_h)
background.update()

win1 = GameSprite("win1.png", 0, 0, win_w, win_h)
win2 = GameSprite("win2.png", 0, 0, win_w, win_h)
win_freands = GameSprite("win_f.png", 0, 0, win_w, win_h)

player1 = Player("player.jpg", 0, 300, 7, 100, 0, 10)
player2 = Player2("player.jpg", 1193, 300, 7, 100, 0, 10)

count1 = player1.speed_x
count2 = player2.speed_x

ball_w = 25
ball_h = 25
ball_speed_x = 10
ball_speed_y = 10

ball = Ball('ball.png', 587, 312, ball_w, ball_h, ball_speed_x, ball_speed_y)

clock = pygame.time.Clock()

f2 = pygame.font.Font(None, 40)

f1 = pygame.font.Font(None, 60)

win_tick = 90

goals1 = 0
goals2 = 0
g1 = f2.render(str(goals1), True, (255, 255, 255))
g2 = f2.render(str(goals2), True, (255, 255, 255))


tics = 7100
tic = 60
min = 1
sec = 59
time = f1.render(str(min) + ':' + str(sec), True, (0, 0, 0))

game = True
while game:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game = False
        

    player1.control(events)
    player2.control(events)

    ball.move_ball()

    col = pygame.sprite.collide_rect(player2, ball)
    if col == True:
        ball.speed_x *= -1
        ball.speed_x -= 1
        ball.speed_y = 1
        ball.speed_y *= randint(-5, 5)

    col2 = pygame.sprite.collide_rect(player1, ball)
    if col2 == True:
        ball.speed_x *= -1
        ball.speed_x += 1
        ball.speed_y = 1
        ball.speed_y *= randint(-5, 5)

    if ball.rect.x <= 0 - ball_w:
        ball.rect.x = 587
        ball.rect.y = 312
        ball.speed_x = ball_speed_x
        ball.speed_x = ball.speed_x * -1
        int(goals2)
        goals2 += 1
        g2 = f2.render(str(goals2), True, (255, 255, 255))
        
    
    if ball.rect.x >= win_w:
        ball.rect.x = 587
        ball.rect.y = 312
        ball.speed_x = ball_speed_x
        ball.speed_x = ball.speed_x * -1
        int(goals1)
        goals1 += 1
        g1 = f2.render(str(goals1), True, (255, 255, 255))
        

    

    if tic <= 0:
        int(sec)
        sec -= 1
        time = f1.render(str(min) + ':' + str(sec), True, (0, 0, 0))
        tic = 60

    if sec <= 0:
        int(min)
        min -= 1
        time = f1.render(str(min) + ':' + str(sec), True, (0, 0, 0))
        int(sec)
        sec = 59
        str(sec)

    


    background.update()

    wind.blit(time, (555, 8))
    wind.blit(g1, (25, 23))
    wind.blit(g2, (1160, 23))

    player1.update()
    player2.update()

    ball.update()

    if tics <= 0:
        if goals1 > goals2 and win_tick >= 0:
            win1.update()
            win_tick -= 1
            if win_tick <= -1:
                game = False
            
        if goals1 < goals2 and win_tick >= 0:
            win2.update()
            win_tick -= 1
            if win_tick <= -1:
                game = False
        
        if goals1 == goals2 and win_tick >= 0:
            win_freands.update()
            win_tick -= 1
            if win_tick <= -1:
                game = False
            

    if goals1 >= 10 and win_tick >= 0:
        win1.update()
        win_tick -= 1
        if win_tick <= -1:
            game = False

    if goals2 >= 10 and win_tick >= 0:
        win2.update()
        win_tick -= 1
        if win_tick <= -1:
            game = False
        

    tics -= 1
    tic -= 1
    pygame.display.update()
    clock.tick(60)
    pygame.display.flip()