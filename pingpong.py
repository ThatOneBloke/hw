import pgzrun

WIDTH = 800
HEIGHT = 500

score = 0

ball = Actor("moon.png")
ball.pos = (300, 300)
bat = Rect((400, 450), (60, 30))

speedx = 2
speedy = 2

def draw():
    screen.fill("black")
    ball.draw()
    screen.draw.filled_rect(bat, "white")
    screen.draw.text("score = " + str(score),  (200, 125), color = "white")

def update():
    global speedx, speedy, score
    ball.x += speedx
    ball.y += speedy
    
    if keyboard.right:
        bat.x += 2
    if keyboard.left:
        bat.x -= 2
    
    if ball.right > WIDTH or ball.left < 0:
        speedx = -speedx
    if ball.top < 0:
        speedy = -speedy
    if ball.colliderect(bat):
        speedy = -speedy
        score += 1
    if ball.bottom > HEIGHT:
        exit()

pgzrun.go()