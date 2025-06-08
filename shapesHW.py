import pygame
pygame.init()
#this will initialise the pygame library
screen = pygame.display.set_mode((500, 500))

class Circle():
    def __init__ (self, radius, color, pos, width):
        self.radius = radius
        self.color = color
        self.pos = pos
        self.width = width
        self.surface = screen
    
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)
    
bluecircle = Circle(40, "blue", (160, 250), 5)
blackcircle = Circle(40, "black", (250, 250), 5)
yellowcircle = Circle(40, "yellow", (205, 290), 5)
greencircle = Circle(40, "green", (295, 290), 5)
redcircle = Circle(40, "red", (340, 250), 5)
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("white")
    bluecircle.draw()
    blackcircle.draw()
    yellowcircle.draw()
    greencircle.draw()
    redcircle.draw()
    pygame.display.update()