import pgzrun
import random

TITLE = "good shot game by xavier"
WIDTH = 500
HEIGHT = 500
message = ""
score = 0

skelly = Actor("badtotheboneskelly.png")
def draw():
    screen.clear()
    screen.fill("black")
    skelly.draw()
    screen.draw.text(message, (300, 100), color = "white", fontsize = 40)
    screen.draw.text(str(score), (300, 150), color = "white", fontsize = 40)

def placeskelly():
    skelly.x = random.randint(50, 450)
    skelly.y = random.randint(50, 450)

def on_mouse_down(pos):
    global message
    global score
    if skelly.collidepoint(pos):
        placeskelly()
        message = "good shot"
        score = score + 1
    else:
        message = "missed shot"
        score = score - 1

placeskelly()
pgzrun.go()