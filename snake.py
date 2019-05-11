import pgzrun
from random import randint
from time import sleep

TITLE = 'Snake'
WIDTH = 800
HEIGHT = 600
STEP = 50
direction = 'l'
fail = False

snake = [Actor('snake_element',(WIDTH/2, HEIGHT/2))]
apple = Actor('apple', (100, (randint(1,11)*STEP)))

def draw():
    screen.fill('black')
    for s in snake:
        s.draw()
    apple.draw()

    if fail:
        screen.fill('black')
        

def on_key_down():
    global direction
    if keyboard.right and direction != 'l':
        direction = 'r'
    if keyboard.left and direction != 'r':
        direction = 'l'
    if keyboard.up and direction != 'd':
        direction = 'u'
    if keyboard.down and direction != 'u':
        direction = 'd'

def update():
    global direction
    if direction == 'l':
        snake.insert(0, Actor('snake_element',(snake[0].x - STEP, snake[0].y)))
    if direction == 'r':
        snake.insert(0, Actor('snake_element',(snake[0].x + STEP, snake[0].y)))
    if direction == 'u':
        snake.insert(0, Actor('snake_element',(snake[0].x, snake[0].y - STEP)))
    if direction == 'd':
        snake.insert(0, Actor('snake_element',(snake[0].x, snake[0].y + STEP)))

    if len(snake) > 10:
        snake.remove(snake[len(snake) - 1])

    for i in range(2, len(snake)):
        if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
            fail = True
    
    sleep(0.2)


pgzrun.go()
