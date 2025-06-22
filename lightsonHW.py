import pygame
import time
pygame.init()
screen = pygame.display.set_mode((500, 500))

img = pygame.image.load("HW/images/lightbulbon.png")
image = pygame.transform.scale(img, (500, 500))

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("white")
    screen.blit(image, (0, 0))
    pygame.display.update()
    time.sleep(0.2)

    img2 = pygame.image.load("HW/images/lightbulboff.png")
    image2 = pygame.transform.scale(img2, (500, 500))
    screen.fill("white")
    screen.blit(image2, (0, 0))
    pygame.display.update()
    time.sleep(0.2)