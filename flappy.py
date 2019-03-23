import pgzrun
import random

TITLE = 'Flappy bird'
WIDTH = 400
HEIGHT = 708
SPEED = 3
GAP = 130
FLAP = 6.5
GRAVITY = 0.6

bird = Actor('bird1', (75, 200))
bird.dead = False
bird.score = 0
bird.vy = 0

pipe_top = Actor('top', anchor=('left', 'bottom'), pos=(-100, 0))
pipe_bottom = Actor('bottom', anchor=('left', 'top'), pos=(-100, 0))

def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)
    
def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        bird.score += 1

def update_bird():
    bird.vy += GRAVITY
    bird.x = 75
    uv = bird.vy
    bird.y += (uv + bird.vy)/2
    bird.x = 75

def update():
    update_pipes()
    update_bird()

def on_key_down():
    if not bird.dead:
        bird.vy = -FLAP

def draw():
    screen.blit('background', (0, 0))
    bird.draw()
    pipe_top.draw()
    pipe_bottom.draw()













    

pgzrun.go()
