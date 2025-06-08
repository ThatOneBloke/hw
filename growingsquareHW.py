import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

class Rectangle():
    def __init__ (self, color, width, height, pos):
        self.color = color
        self.width = width
        self.height = height
        self.pos = pos
        self.surface = screen
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, (*self.pos , self.width, self.height))

    def grow(self, W, H):
        self.width = self.width + W
        self.height = self.height + H
        pygame.draw.rect(self.surface, self.color, (*self.pos , self.width, self.height))

bluesquare = Rectangle("blue", (250, 250), 50, 50)

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            bluesquare.draw()
            pygame.display.update()
        if i.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            bluesquare.grow(10, 10)
            pygame.display.update()
