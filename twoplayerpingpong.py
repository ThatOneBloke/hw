import pgzrun

WIDTH = 680
HEIGHT = 500

ball = Actor("moon.png")
ball.pos = (340, 250)
bat1 = Rect((40, 220), (30, 60))
bat2 = Rect((640, 220), (30, 60))

speedx = 2
speedy = 2

def draw():
    screen.fill("black")
    ball.draw()
    screen.draw.filled_rect(bat1, "white")
    screen.draw.filled_rect(bat2, "white")

def update():
    global speedx, speedy, score
    ball.x += speedx
    ball.y += speedy
    
    if keyboard.s:
        bat1.y += 2
    if keyboard.w:
        bat1.y -= 2
    
    if keyboard.down:
        bat2.y += 2
    if keyboard.up:
        bat2.y -= 2
    
    if ball.bottom > HEIGHT or ball.top < 0:
        speedy = -speedy
    if ball.right > WIDTH or ball.left < 0:
        exit()
    if ball.colliderect(bat1):
        speedx = -speedx
    if ball.colliderect(bat2):
        speedx = -speedx

pgzrun.go()