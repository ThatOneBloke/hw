import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800, 600))

bg1 = pygame.image.load("HW/images/road.jpg")
bg = pygame.transform.scale(bg1, (800, 600))
player1 = pygame.image.load("HW/images/car.png")
player = pygame.transform.scale(player1, (60, 70))

playerx = 400
playery = 300

keys = [False, False, False, False]

run = True
while run:
    screen.blit(bg, (0, 0))
    screen.blit(player, (playerx, playery))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        
        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                keys[0] = True
            elif i.key == K_RIGHT:
                keys[1] = True
            elif i.key == K_DOWN:
                keys[2] = True
            elif i.key == K_LEFT:
                keys[3]= True

        if i.type == pygame.KEYUP:
            if i.key == K_UP:
                keys[0] = False
            elif i.key == K_RIGHT:
                keys[1] = False
            elif i.key == K_DOWN:
                keys[2] = False
            elif i.key == K_LEFT:
                keys[3] = False
    if keys[0] == True:
        playery -= 2
    if keys[1] == True:
        playerx += 2
    if keys[2] == True:
        playery += 2
    if keys[3] == True:
        playerx -= 2
    
    playery += 0.5

    if playery > 600:
        exit()
    pygame.display.update()